import sys
import time
import getpass

from datetime import datetime, timedelta, date
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QResizeEvent, QBrush, QColor, QMovie, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLabel
from PyQt5.QtCore import Qt, QObject, QThread, QDate, QVariant, pyqtSignal

import kpidb as cmredb
import cds_sql as cds
import msgbox
import my_styles
from manager_main import Ui_managerMain
from email_distribution import Ui_distributionLists
from review_form import Ui_reviewForm
from review_search import Ui_reviewSearch
from review_reader import Ui_reviewReader
from one_on_one_main import Ui_oneOnOneMain
from top_five import Ui_top5Agents
from employee import AddEmployee, EmployeeMaintenance, EmployeeDetails, EmployeeGraphs

# Column headers used to build QStandardItemModel
headers = [
    'User ID', 'Collector', 'Group', 'Start Time', "RPC's Per Hour", 'Base Conversion', 'Conversion Rate', 'Last Update'
]
headers_rvw = ['Collector', 'Issue Date', 'Topic', 'Review Type', 'Level', 'Issued By', 'Review ID']
allowed_users = cmredb.users_with_access()


class Window(QMainWindow, Ui_managerMain):
    """Main tracker window that Managers use to track Agent's current KPI's"""

    def __init__(self):
        super().__init__()
        self.setStyleSheet(my_styles.active_style)
        # Creates the main window UI and initialize class attributes
        self.setupUi(self)
        self.current_bd_managers = cmredb.current_managers()

        self.movie = QMovie("snow_fall.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        self.myMessage = QLabel()
        self.myMessage.setStyleSheet("""
            QLabel{
                font: 10pt "MS Shell Dlg 2";
                font-weight: bold;
                color: rgb(255, 255, 255);
            }
            """)
        self.statusbar.addWidget(self.myMessage)

        # Get all users and add current managers to combobox
        self.all_users = cmredb.all_act_collectors()
        self.managers_agents = []
        self.managerCombo.addItems([mgr for mgr in sorted(self.current_bd_managers)])

        # Default sort is set to RPC's
        self.user_sort_col = 4
        # Default sorting order is descending
        self.user_sort_order = Qt.DescendingOrder

        # Build QStandardItemModel used to hold agent data to be placed in a table view
        self.agentModel = QStandardItemModel(self)
        self.agentModel.setHorizontalHeaderLabels(headers)
        self.agentTableView.setModel(self.agentModel)
        # Clear vertical headers
        self.agentTableView.verticalHeader().setVisible(False)
        # Last column will stretch to end of the table view
        self.agentTableView.horizontalHeader().setStretchLastSection(True)

        # Starts thread that loops to continuously update main window
        self.start_thread()

        # Connect main window's signals to slots
        self.managerRefresh.clicked.connect(self.manual_refresh)
        self.managerCombo.currentIndexChanged.connect(self.update_users)
        self.agentTableView.horizontalHeader().sortIndicatorChanged.connect(self.sort_order)
        self.agentTableView.doubleClicked.connect(self.agent_details)
        # Options under "File" in menu bar
        self.actionRun_Desk_Goal_Update.triggered.connect(self.update_desks)
        self.actionSettings.triggered.connect(self.user_settings)
        self.actionDistribution_Lists.triggered.connect(self.distribution_lists)
        self.actionTop_Five.triggered.connect(self.view_top_5)
        # Options under "Employees" in menu bar
        self.actionAdd_Employee.triggered.connect(self.add_employee)
        self.actionUpdate_Employee.triggered.connect(self.employee_maintenance)
        self.actionManager_Review.triggered.connect(self.employee_review)
        # Options under "View" in menu bar
        self.actionTrending_Graphs.triggered.connect(self.employee_graphs)
        self.actionEmployee_Review.triggered.connect(self.employee_review_search)
        self.actionOne_On_One_Tracker.triggered.connect(self.one_one_tracker)

    def paintEvent(self, event):
        current_frame = self.movie.currentPixmap()
        frame_rect = current_frame.rect()
        frame_rect.moveCenter(self.rect().center())
        if frame_rect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frame_rect.left(), frame_rect.top(), current_frame)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Method used for handling column width when the user resizes the main UI"""
        super().resizeEvent(event)
        table_width = self.agentTableView.width()
        set_width = 900
        # Takes table width * column's min possible width / table's min possible width
        # If a column is added, add the min column width to the total table width
        self.agentTableView.setColumnWidth(0, int(table_width * 70 / set_width))
        self.agentTableView.setColumnWidth(1, int(table_width * 130 / set_width))
        self.agentTableView.setColumnWidth(2, int(table_width * 75 / set_width))
        self.agentTableView.setColumnWidth(3, int(table_width * 115 / set_width))
        self.agentTableView.setColumnWidth(4, int(table_width * 120 / set_width))
        self.agentTableView.setColumnWidth(5, int(table_width * 130 / set_width))
        self.agentTableView.setColumnWidth(6, int(table_width * 130 / set_width))
        self.agentTableView.setColumnWidth(7, int(table_width * 100 / set_width))

    def start_thread(self):
        """Function that creates a worker thread that is used to refresh KPI's every 5 minuets on a loop."""

        # Create thread object
        self.thread = QThread()
        # Create worker object
        self.worker = Worker()
        # Pass worker to thread for handling
        self.worker.moveToThread(self.thread)
        # Connect default signals and slots
        self.thread.started.connect(self.worker.start_worker_loop)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Connect app specific signals and slots
        self.worker.refresh_main.connect(self.update_users)
        self.worker.updt_main_stsbar.connect(self.update_status)
        self.worker.close_app.connect(self.closing_time)

        # Start the thread
        self.thread.start()

    def manual_refresh(self):
        """Function used to manually refresh the KPI's before the automatic refresh takes place."""
        curr_time = datetime.strftime(datetime.now(), '%I:%M:%S %p')
        # Update status bar message and call function to update QStandardItemModel
        self.update_status(curr_time, '0:00 min')
        self.update_users()

    def update_users(self):
        """Function used to gather info necessary to update data in QStandardItemModel."""

        # Clear current data in QStandardItemModel except the headers
        self.agentModel.setRowCount(0)

        # Updates GUI based on the manager selected
        if self.managerCombo.currentIndex() == 0:
            self.build_model(self.all_users)
        else:
            sel_mgr = self.managerCombo.currentText()
            self.managers_agents = cmredb.my_collectors(sel_mgr)
            self.build_model(self.managers_agents)

    def build_model(self, collectors):
        """Function used to build the QStandardItemModel based on user selection."""

        # Users is a nested list of user ID and name [['JSB', 'Jake Boden'], ]
        for coll in collectors:
            # Get user specific stats calling function from kpidb.py passing the User ID
            agent_stats = cmredb.daily_kpis(coll[0])
            base_conv = cmredb.cont_base_data(coll[0])
            # Check if result is null
            if len(agent_stats) > 0:
                # Convert tuple to list
                list_stats = list(agent_stats[0])
                # Remove DAY from index 2
                list_stats.pop(3)
                # Insert collectors name. (User ID, Name, Group, Start Time, RPC's, Conv, Last Update)
                list_stats.insert(1, coll[1])
                list_stats.insert(5, base_conv[0])
            else:
                # Query returned no results which indicates user has not logged into Agent Tracker
                list_stats = [coll[0], coll[1], 'N/A', 'Not Logged In', '0', '0.0', '0.0', 'N/A']

            goal = float(list_stats[6]) - float(list_stats[5])

            # Converts items in list to a QStandardItem which is required for PyQt5
            for index, item in enumerate(list_stats):
                if index == 4:
                    # Format data as you want it displayed
                    rpcs = '{:.2f}'.format(float(item))
                    # Create Qt Object
                    data_obj = QStandardItem(rpcs)
                    # Sets the sort on 'value' of the object and assigns 'UserRole' as the sorting method
                    data_obj.setData(float(item), Qt.UserRole)
                elif index == 5:
                    # Format data as you want it displayed
                    conv = '{0:.0%}'.format(float(item))
                    # Create Qt Object
                    data_obj = QStandardItem(conv)
                    # Sets the sort on 'value' of the object and assigns 'UserRole' as the sorting method
                    data_obj.setData(float(item), Qt.UserRole)
                elif index == 6:
                    # Format data as you want it displayed
                    conv = '{0:.0%}'.format(float(item))
                    # Create Qt Object
                    data_obj = QStandardItem(conv)
                    # Sets the sort on 'value' of the object and assigns 'UserRole' as the sorting method
                    data_obj.setData(float(item), Qt.UserRole)
                    if goal > 0:
                        my_color = QColor(0, 170, 0, 50)
                        my_brush = QBrush(my_color)
                    else:
                        my_color = QColor(170, 0, 0, 50)
                        my_brush = QBrush(my_color)
                    data_obj.setData(my_brush, Qt.BackgroundRole)
                else:
                    if item == "N/A":
                        # Create Qt Object
                        data_obj = QStandardItem(item)
                        # Sets the sort on 'value' of the object and assigns 'UserRole' as the sorting method
                        data_obj.setData("Z", Qt.UserRole)
                    else:
                        # Create Qt Object
                        data_obj = QStandardItem(item)
                        # Sets the sort on 'value' of the object and assigns 'UserRole' as the sorting method
                        data_obj.setData(item, Qt.UserRole)

                # Set object attributes
                if index > 1:
                    # Aligns the text in columns 2 and above
                    data_obj.setTextAlignment(Qt.AlignCenter)
                # Set object flags
                data_obj.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                # Replace string item in list with newly created QStandardItem
                list_stats[index] = data_obj

            # Add user stats (list of QStandardItems) to QStandardItemModel
            self.agentModel.appendRow(list_stats)

        # Sort QStandardItemModel based on defaults or users current settings
        self.agentModel.setSortRole(Qt.UserRole)
        self.agentModel.sort(self.user_sort_col, self.user_sort_order)
        self.agentTableView.resizeRowsToContents()

    def update_status(self, up_time, count_down):
        """Simple function used to update status bar message."""
        self.myMessage.setText(f'Last updated at {up_time}. Next update in {count_down}.')

    def sort_order(self, col, order):
        """Simple function used to save the users sort column and sort order settings.
        Called from the 'sortIndicatorChanged' signal of the QTableView."""
        self.user_sort_col = col
        self.user_sort_order = order

    def agent_details(self, model):
        """Function used to initialize the agent details window.
        Called from the 'doubleClicked' signal of the QTableView."""

        # Gets collector's User ID from the QStandardItemModel
        user_id = self.agentModel.item(model.row(), 0).text()
        coll_name = self.agentModel.item(model.row(), 1).text()

        collector = f'{user_id} - {coll_name}'
        manager = self.managerCombo.currentText()

        # Creates the agent details window
        agent_window = EmployeeDetails(self.all_users, collector, manager)
        agent_window.addReview.clicked.connect(lambda: self.employee_review(collector))
        agent_window.employeeReviews.clicked.connect(lambda: self.employee_review_search(collector))
        agent_window.exec_()

    def update_desks(self):
        """Function used to update the desk and goals for all employees in the CMRE db."""
        results = cds.get_act_desks()
        for result in results:
            cmredb.update_desks(result)
        update_msg = msgbox.desk_update_complete()
        update_msg.exec()

    def add_employee(self):
        """Function used to call Add Employee GUI."""
        add_emp = AddEmployee()
        add_emp.exec_()
        self.update_users()

    def employee_maintenance(self):
        """Function used to initialize the employee maintenance window."""
        selection = self.agentTableView.selectionModel().selectedRows()

        if selection:
            user_id = self.agentModel.item(selection[0].row(), 0).text()
            coll_name = self.agentModel.item(selection[0].row(), 1).text()
            employee = f'{user_id} - {coll_name}'
        else:
            employee = ""
        emp_main = EmployeeMaintenance(employee)
        emp_main.exec_()
        self.update_users()

    def employee_graphs(self):
        """Function used to initialize the agent graphs window."""

        selection = self.agentTableView.selectionModel().selectedRows()

        if selection:
            user_id = self.agentModel.item(selection[0].row(), 0).text()
            coll_name = self.agentModel.item(selection[0].row(), 1).text()
            coll = f'{user_id} - {coll_name}'
        else:
            coll = ""

        mgr = self.managerCombo.currentText()
        agent_graphs = EmployeeGraphs(coll, mgr)
        agent_graphs.exec_()

    def employee_review(self, coll):
        """Function used to initialize the agent review window."""
        mgr = self.managerCombo.currentText()
        agent_rvw = ReviewForm(mgr, coll)
        agent_rvw.exec_()

    def employee_review_search(self, coll):
        """Function used to review employee reviews window."""
        employee_search = ReviewSearch(coll)
        employee_search.exec_()

    def user_settings(self):
        """Function used to initialize the manager settings window."""
        msg = msgbox.unavailable()
        msg.exec_()

    def distribution_lists(self):
        dist_win = DistributionLists()
        dist_win.exec_()

    def one_one_tracker(self):
        one_one = OneOnOneTracker()
        one_one.exec_()

    def view_top_5(self):
        top_five = TopFive()
        top_five.exec_()

    def closing_time(self):
        """Function is called when user tries to run app after 5:40 pm. Will
        also force close the app if left open overnight."""
        closing_msg = msgbox.closing_time()
        return_value = closing_msg.exec()
        if return_value == QMessageBox.Ok:
            app.quit()


class Worker(QObject):
    """Worker class that is threaded using QThread."""

    # Create signals to be passed to main thread
    finished = pyqtSignal()
    refresh_main = pyqtSignal()
    updt_main_stsbar = pyqtSignal(str, str)
    close_app = pyqtSignal()

    # Stop time used to kill loop at 5:40 PM
    stop_time = datetime.strptime(f'{date.today()} 17:40:00', '%Y-%m-%d %H:%M:%S')

    def start_worker_loop(self):
        """Function used to start loop to refresh app every 5 minutes"""

        business_hours = True
        while business_hours:
            curr_time = datetime.now()
            next_update = datetime.now() + timedelta(minutes=5)
            count_down = str(next_update - curr_time)

            # Check if the current time is past 5:40 PM
            if datetime.now() > self.stop_time:
                # Sends signal to main thread's slot connected to 'update_status' function
                self.updt_main_stsbar.emit(datetime.strftime(curr_time, '%I:%M:%S %p'), '0:00 min')
                # Sends signal to main thread's slot connected 'update_users' function which builds the model
                self.refresh_main.emit()
                business_hours = False
                time.sleep(3600)
                app.quit()
            else:
                # Sends signal to main thread's slot connected to 'update_status' function
                self.updt_main_stsbar.emit(datetime.strftime(curr_time, '%I:%M:%S %p'), f'{count_down[3:7]} min')
                # Sends signal to main thread's slot connected 'update_users' function which builds the model
                self.refresh_main.emit()

                # Starts nested loop to countdown number of minutes until next update
                x = 300
                while x != 0:
                    time.sleep(1)
                    lapse_time = datetime.now()
                    # Calculates time remaining using 'next_time' defined in outer loop minus current time
                    count_down = str(next_update - lapse_time)
                    # Sends signal to main thread's slot connected to 'update_status' function
                    self.updt_main_stsbar.emit(datetime.strftime(curr_time, '%I:%M:%S %p'), f'{count_down[3:7]} min')
                    x -= 1


class ReviewForm(QDialog, Ui_reviewForm):
    """Class that displays employee review form to be completed and saved."""

    def __init__(self, mgr, coll):
        super().__init__()
        self.setStyleSheet(my_styles.active_style)
        self.setupUi(self)
        self.emp_id = ""
        self.discFrame.hide()
        self.employee = 0
        self.radio_btns = [
            self.radio1on1,
            self.radioSbS,
            self.radioCoach,
            self.radioDisc
        ]
        today_date = date.today()
        sdate = QDate(today_date)
        self.issueDate.setDate(sdate)

        self.all_users = window.all_users
        self.managers_agents = []
        self.managerCombo.addItems([mgr for mgr in sorted(window.current_bd_managers)])
        self.issuedBy.addItems([mgr for mgr in sorted(window.current_bd_managers)])
        self.issuedBy.setCurrentIndex(-1)

        # Connect signals to slots
        self.managerCombo.currentIndexChanged.connect(self.update_combobox)
        self.employeeSelect.currentIndexChanged.connect(self.update_info)
        self.closeButton.clicked.connect(self.close_without_save)
        # self.editReview.clicked.connect(self.next_screen)
        self.saveReview.clicked.connect(self.save_review)
        self.employeeGraphs.clicked.connect(self.employee_graphs)
        self.radio1on1.toggled.connect(self.template_sel)
        self.radioSbS.toggled.connect(self.template_sel)
        self.radioCoach.toggled.connect(self.template_sel)
        self.radioDisc.toggled.connect(self.template_sel)

        # Sets manager to selected manager from main
        mgr_index = self.managerCombo.findText(mgr)
        if mgr_index == 0:
            self.update_combobox()
        else:
            self.managerCombo.setCurrentIndex(mgr_index)

        if coll:
            index = self.employeeSelect.findText(coll)
            self.employeeSelect.setCurrentIndex(index)

    def update_combobox(self):
        """Function used to update employee combobox based on the manager selected."""

        # Block signal temporarily
        self.employeeSelect.blockSignals(True)
        self.employeeSelect.clear()

        # If manager is 'All' then all employees are added
        if self.managerCombo.currentIndex() == 0:
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.all_users)])
        else:
            # Adds only the employees for the selected manager
            mgr = self.managerCombo.currentText()
            self.managers_agents = cmredb.my_collectors(mgr)
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.managers_agents)])

        self.employeeSelect.setCurrentIndex(-1)
        # Unblock the signal and update employee info
        self.employeeSelect.blockSignals(False)

        self.emp_id = ""
        self.agentUserID.clear()
        self.agentDesk.clear()
        self.agentExt.clear()
        self.agentGroup.clear()
        self.managerNotes.clear()
        self.meetLocation.clear()
        self.issuedBy.setCurrentIndex(-1)
        today_date = date.today()
        sdate = QDate(today_date)
        self.issueDate.setDate(sdate)
        self.mainTopic.clear()
        self.radio1on1.setChecked(True)
        self.managerNotes.setReadOnly(True)
        self.managerNotes.setPlaceholderText("Select employee to begin...")

    def update_info(self):
        """Updates the GUI with the newly selected employee's information."""

        self.managerNotes.clear()
        self.meetLocation.clear()
        self.issuedBy.setCurrentIndex(-1)
        self.mainTopic.clear()
        self.radio1on1.setChecked(True)
        coll = self.employeeSelect.currentText().split(' - ')
        user_id = coll[0]
        # Obtain agent details by calling function in kpidb.py
        details = cmredb.coll_details(user_id)
        # Converts results from a tuple to a list
        coll_details = list(details)
        self.emp_id = coll_details[0]
        self.agentUserID.setText(user_id)
        self.agentDesk.setText(coll_details[6])
        self.agentExt.setText(str(coll_details[5]))
        self.agentGroup.setText(coll_details[8])
        self.managerNotes.setReadOnly(False)
        self.setStyleSheet(my_styles.active_style)
        self.managerNotes.setPlaceholderText("-Required-")

    def template_sel(self):
        """Function used to detect template type and update GUI options accordingly."""
        for item in self.radio_btns:
            if item.isChecked():
                button = item.text()
                self.tempType.setText(button)
                if button == "Disciplinary":
                    self.discFrame.show()
                else:
                    self.discFrame.hide()

    def close_without_save(self):
        if len(self.managerNotes.toPlainText()) > 0:
            confirm_msg = msgbox.confirm_close_unsaved()
            confirm_close = confirm_msg.exec_()
            if confirm_close == QMessageBox.Close:
                self.close()
        else:
            self.close()

    def save_review(self):

        def field_check():
            passed = True
            check_fields = [self.meetLocation, self.mainTopic]

            if self.employeeSelect.currentIndex() > -1:
                if len(self.managerNotes.toPlainText()) != 0:
                    if self.issuedBy.currentIndex() > -1:
                        for field in check_fields:
                            if len(field.text()) == 0:
                                passed = False
                                break
                    else:
                        passed = False
                else:
                    passed = False
            else:
                passed = False

            return passed

        def gather_data():
            rvw_type = ""

            for btn in self.radio_btns:
                if btn.isChecked():
                    rvw_type = btn.text()
                    break

            if rvw_type == "Disciplinary":
                disc_type = f"{self.disciplineType.currentText()}"
            else:
                disc_type = ""

            rvw_id = f"{self.emp_id}-{self.issueDate.date().toPyDate()}-{rvw_type[:3]}"

            rvw_data = [
                rvw_id,
                self.emp_id,
                self.agentUserID.text(),
                self.agentDesk.text(),
                self.agentExt.text(),
                self.agentGroup.text(),
                self.meetLocation.text().title(),
                self.issuedBy.currentText(),
                str(self.issueDate.date().toPyDate()),
                self.mainTopic.text().title(),
                rvw_type,
                disc_type,
                self.managerNotes.toPlainText()
            ]

            return rvw_data

        if field_check():
            save_msg = msgbox.confirm_save()
            selection = save_msg.exec_()
            if selection == QMessageBox.Save:
                add_success = cmredb.add_review(gather_data())
                if add_success:
                    update_success = cmredb.o1o_coll_update([str(self.issueDate.date().toPyDate()), self.emp_id])
                    if update_success:
                        self.update_combobox()
                    else:
                        err_msg = msgbox.ask_jake()
                        err_msg.exec_()
                else:
                    err_msg = msgbox.action_error()
                    err_msg.exec_()
        else:
            error_msg = msgbox.add_data_error()
            error_msg.exec_()

    def employee_graphs(self):
        """Function used to initialize the agent graphs window."""
        coll = self.employeeSelect.currentText()
        mgr = self.managerCombo.currentText()
        agent_graphs = EmployeeGraphs(coll, mgr)
        agent_graphs.exec_()


class ReviewSearch(QDialog, Ui_reviewSearch):
    """Class that displays search form to locate employee reviews."""
    def __init__(self, coll):
        super().__init__()
        self.setStyleSheet(my_styles.active_style)
        self.setupUi(self)
        self.all_users = window.all_users
        self.managers_agents = []
        self.check_boxes = [
                self.check1on1,
                self.checkSbS,
                self.checkCoach,
                self.checkDisc
            ]
        self.managerCombo.addItems([mgr for mgr in sorted(window.current_bd_managers)])
        self.update_combobox()

        if coll:
            index = self.employeeSelect.findText(coll)
            self.employeeSelect.setCurrentIndex(index)

        self.issueStrtDate.setDate(QDate(datetime.today() - timedelta(days=30)))
        self.issueEndDate.setDate(QDate(datetime.today()))
        self.reviewModel = QStandardItemModel(self)
        self.reviewModel.setHorizontalHeaderLabels(headers_rvw)
        self.empReviewTable.setModel(self.reviewModel)
        # Clear vertical headers
        self.empReviewTable.verticalHeader().setVisible(False)
        # Last column will stretch to end of the table view
        self.empReviewTable.horizontalHeader().setStretchLastSection(True)
        self.search_reviews()

        self.managerCombo.currentIndexChanged.connect(self.update_combobox)
        self.searchButton.clicked.connect(self.search_reviews)
        self.clearButton.clicked.connect(self.clear_search)
        self.empReviewTable.doubleClicked.connect(self.look_up_review)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Method used for handling column width when the user resizes the main UI"""
        super().resizeEvent(event)
        table_width = self.empReviewTable.width()
        set_width = 750
        # Takes table width * column's min possible width / table's min possible width
        # If a column is added, add the min column width to the total table width
        self.empReviewTable.setColumnWidth(0, int(table_width * 120 / set_width))
        self.empReviewTable.setColumnWidth(1, int(table_width * 90 / set_width))
        self.empReviewTable.setColumnWidth(2, int(table_width * 160 / set_width))
        self.empReviewTable.setColumnWidth(3, int(table_width * 100 / set_width))
        self.empReviewTable.setColumnWidth(4, int(table_width * 80 / set_width))
        self.empReviewTable.setColumnWidth(5, int(table_width * 90 / set_width))
        self.empReviewTable.setColumnWidth(6, int(table_width * 90 / set_width))

    def update_combobox(self):
        """Function used to update employee combobox based on the manager selected."""

        self.employeeSelect.clear()
        # If manager is 'All' then all employees are added
        if self.managerCombo.currentIndex() == 0:
            self.employeeSelect.addItem("All")
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.all_users)])
        else:
            # Adds only the employees for the selected manager
            mgr = self.managerCombo.currentText()
            self.managers_agents = cmredb.my_collectors(mgr)
            self.employeeSelect.addItem("All")
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.managers_agents)])

    def search_reviews(self):

        def generate_sql():
            srch_1 = ""
            srch_2 = ""
            srch_3 = ""

            sdate = self.issueStrtDate.text().split("/")
            syear = sdate[2]
            smon = sdate[0].zfill(2)
            sday = sdate[1].zfill(2)
            edate = self.issueEndDate.text().split("/")
            eyear = edate[2]
            emon = edate[0].zfill(2)
            eday = edate[1].zfill(2)

            select_fields = """
                SELECT
                    (COLL.FIRST_NAME || " " || COLL.LAST_NAME) EMP_NAME,
                    RVW.ISSUE_DATE,
                    RVW.TOPIC,
                    RVW.RVW_TYPE,
                    RVW.DISC_TYPE,
                    RVW.ISSUED_BY,
                    RVW.REVIEW_ID
                FROM
                    REVIEWS RVW
                JOIN COLL ON RVW.EMP_USERID=COLL.USER_ID
                WHERE
                """
            date_sql = f"ISSUE_DATE BETWEEN '{syear}-{smon}-{sday}' AND '{eyear}-{emon}-{eday}'"

            if self.managerCombo.currentIndex() > 0:
                srch_1 = f"ISSUED_BY='{self.managerCombo.currentText()}'"
            if self.employeeSelect.currentIndex() > 0:
                srch_2 = f"EMP_USERID='{self.employeeSelect.currentText()[:3]}'"

            xcount = 0
            for item in self.check_boxes:
                if item.isChecked():
                    if xcount == 0:
                        srch_3 += f"'{item.text()}'"
                        xcount += 1
                    else:
                        srch_3 += f", '{item.text()}'"

            if len(srch_1) > 0:
                criteria_1 = f"{srch_1}"
                if len(srch_2) > 0:
                    criteria_2 = f"AND {srch_2}"
                    if xcount > 0:
                        final_sql = f"{select_fields} {criteria_1} {criteria_2} " \
                                    f"AND RVW_TYPE IN ({srch_3}) " \
                                    f"AND {date_sql}"
                    else:
                        final_sql = f"{select_fields} {criteria_1} {criteria_2} " \
                                    f"AND {date_sql}"
                else:
                    if xcount > 0:
                        final_sql = f"{select_fields} {criteria_1} " \
                                    f"AND RVW_TYPE IN ({srch_3}) " \
                                    f"AND {date_sql}"
                    else:
                        final_sql = f"{select_fields} {criteria_1} " \
                                    f"AND {date_sql}"
            else:
                if len(srch_2) > 0:
                    criteria_1 = f"{srch_2}"
                    if xcount > 0:
                        final_sql = f"{select_fields} {criteria_1} " \
                                    f"AND RVW_TYPE IN ({srch_3}) " \
                                    f"AND {date_sql}"
                    else:
                        final_sql = f"{select_fields} {criteria_1} " \
                                    f"AND {date_sql}"
                else:
                    if xcount > 0:
                        final_sql = f"{select_fields} RVW_TYPE IN ({srch_3}) " \
                                    f"AND {date_sql}"
                    else:
                        final_sql = f"{select_fields} {date_sql}"
            return final_sql

        self.reviewModel.setRowCount(0)
        search_sql = generate_sql()
        results = cmredb.agent_reviews(search_sql)

        for result in results:
            list_result = list(result)
            for index, item in enumerate(list_result):
                data_obj = QStandardItem(item)
                if index > 1:
                    data_obj.setTextAlignment(Qt.AlignCenter)
                data_obj.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                list_result[index] = data_obj

            self.reviewModel.appendRow(list_result)

        self.reviewModel.sort(0, Qt.AscendingOrder)

    def look_up_review(self, model):
        """Function used to initialize the agent review window."""
        rvw_id = self.reviewModel.item(model.row(), 6).text()
        reader = ReviewReader(rvw_id)
        reader.exec_()
        self.search_reviews()

    def clear_search(self):
        for item in self.check_boxes:
            item.setChecked(False)
        self.managerCombo.setCurrentIndex(0)
        self.update_combobox()
        self.issueStrtDate.setDate(QDate(datetime.today() - timedelta(days=30)))
        self.issueEndDate.setDate(QDate(datetime.today()))
        self.search_reviews()


class ReviewReader(QDialog, Ui_reviewReader):
    """Class that displays an employee's review."""

    def __init__(self, rvw_id):
        super().__init__()
        self.setStyleSheet(my_styles.active_style)
        self.setupUi(self)
        self.rvw_id = rvw_id
        self.temp_topic = ""
        self.temp_notes = ""

        self.closeButton.clicked.connect(self.close)
        self.editReview.clicked.connect(self.edit_review)
        self.saveButton.clicked.connect(self.save_and_close)
        self.exitEdit.clicked.connect(self.close_editor)
        self.deleteReview.clicked.connect(self.delete_review)

        self.load_review()

    def load_review(self):
        review = cmredb.read_review(self.rvw_id)[0]
        self.employee.setText(review[0])
        self.agentUserID.setText(review[1])
        self.agentDesk.setText(review[2])
        self.agentExt.setText(str(review[3]))
        self.agentGroup.setText(review[4])
        self.issueDate.setText(date.fromisoformat(review[5]).strftime('%m/%d/%Y'))
        self.meetLocation.setText(review[6])
        self.issuedBy.setText(review[7])
        self.mainTopic.setText(review[8])
        self.tempTypeEdit.setText(review[9] + " Review")
        self.discTypeEdit.setText(review[10])
        self.managerNotes.setPlainText(review[11])

    def edit_review(self):
        self.temp_topic = self.mainTopic.text()
        self.temp_notes = self.managerNotes.toPlainText()
        self.managerNotes.setReadOnly(False)
        self.mainTopic.setReadOnly(False)
        self.buttonStack.setCurrentIndex(1)
        self.setStyleSheet(my_styles.active_style)

    def save_and_close(self):
        save_msg = msgbox.confirm_save()
        response = save_msg.exec_()
        if response == QMessageBox.Save:
            data = [
                self.mainTopic.text(),
                self.managerNotes.toPlainText(),
                self.rvw_id
            ]
            success = cmredb.edit_review(data)
            if success:
                self.managerNotes.setReadOnly(True)
                self.mainTopic.setReadOnly(True)
                self.buttonStack.setCurrentIndex(0)
                self.setStyleSheet(my_styles.active_style)
            else:
                err_msg = msgbox.action_error()
                err_msg.exec_()

    def close_editor(self):
        if self.temp_topic != self.mainTopic.text() or self.temp_notes != self.managerNotes.toPlainText():
            warn_msg = msgbox.confirm_change_unsaved()
            response = warn_msg.exec_()
            if response == QMessageBox.Yes:
                self.mainTopic.setText(self.temp_topic)
                self.managerNotes.setPlainText(self.temp_notes)
                self.managerNotes.setReadOnly(True)
                self.mainTopic.setReadOnly(True)
                self.buttonStack.setCurrentIndex(0)
                self.setStyleSheet(my_styles.active_style)
        else:
            self.mainTopic.setText(self.temp_topic)
            self.managerNotes.setPlainText(self.temp_notes)
            self.managerNotes.setReadOnly(True)
            self.mainTopic.setReadOnly(True)
            self.buttonStack.setCurrentIndex(0)
            self.setStyleSheet(my_styles.active_style)

    def delete_review(self):
        del_msg = msgbox.permanently_delete()
        selection = del_msg.exec_()
        if selection == QMessageBox.Yes:
            cmredb.delete_review(self.rvw_id)
            self.close()


class DistributionLists(QDialog, Ui_distributionLists):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(my_styles.active_style)
        self.all_users = cmredb.all_act_collectors()
        self.managers = cmredb.current_managers()
        self.all_email_list = "mailto:"

        for employee in self.all_users:
            self.all_email_list += f'{employee[3]};'
        self.listBrowser.append(f"<a href='{self.all_email_list}'>All Collectors</a>")
        self.listBrowser.append("")

        self.create_group_lists()
        self.create_manager_lists()

    def create_group_lists(self):
        dist_lists = {}
        for employee in self.all_users:
            if employee[4] not in dist_lists.keys():
                dist_lists[employee[4]] = [employee[3]]
            else:
                for key, value in dist_lists.items():
                    if key == employee[4]:
                        value.append(employee[3])

        for key, value in dist_lists.items():
            email_list = "mailto:"
            for item in value:
                email_list += f'{item};'
            self.listBrowser.append(f"<a href='{email_list}'>{key} Collectors</a>")
            self.listBrowser.append("")

    def create_manager_lists(self):
        dist_lists = {}
        for manager in self.managers:
            dist_lists[manager] = []

        for employee in self.all_users:
            for key, value in dist_lists.items():
                if key == employee[2]:
                    value.append(employee[3])

        for key, value in dist_lists.items():
            email_list = "mailto:"
            for item in value:
                email_list += f'{item};'
            self.listBrowser.append(f"<a href='{email_list}'>{key}'s Collectors</a>")
            self.listBrowser.append("")


class OneOnOneTracker(QDialog, Ui_oneOnOneMain):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(my_styles.active_style)
        # Creates the main window UI and initialize class attributes
        self.setupUi(self)

        # Get all users and add current managers to combobox
        self.all_users = cmredb.all_act_collectors()
        self.current_bd_managers = cmredb.current_managers()
        self.managers_agents = []
        self.managerCombo.addItems([mgr for mgr in sorted(self.current_bd_managers)])

        self.vert_headers = []
        self.hor_headers = []
        self.oneXoneModel = QStandardItemModel()
        self.oneXoneView.setModel(self.oneXoneModel)
        self.oneXoneView.verticalHeader().setVisible(False)

        self.oneXoneView.doubleClicked.connect(self.view_details)
        self.managerCombo.currentIndexChanged.connect(self.combobox_changed)

        self.generate_headers(self.all_users)
        self.build_model()

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Method used for handling column width when the user resizes the main UI"""
        super().resizeEvent(event)
        table_width = self.oneXoneView.width()
        set_width = 680
        col_count = self.oneXoneModel.columnCount()
        # Takes table width * column's min possible width / table's min possible width
        # If a column is added, add the min column width to the total table width
        self.oneXoneView.setColumnWidth(0, int(table_width * 200 / set_width))
        for i in range(col_count):
            if i == 0:
                pass
            else:
                self.oneXoneView.setColumnWidth(i, int(table_width * 77 / set_width))

    def combobox_changed(self):
        self.oneXoneModel.clear()
        self.vert_headers.clear()
        self.hor_headers.clear()
        # Updates GUI based on the manager selected
        if self.managerCombo.currentIndex() == 0:
            self.generate_headers(self.all_users)
            self.build_model()
        else:
            sel_mgr = self.managerCombo.currentText()
            self.managers_agents = cmredb.my_collectors(sel_mgr)
            self.generate_headers(self.managers_agents)
            self.build_model()

    def generate_headers(self, users):
        for agent in users:
            self.vert_headers.append(f'{agent[0]} - {agent[1]}')
        for item in cmredb.horizontal_headers():
            issue_month = datetime.strptime(item[0], '%Y-%m-%d').strftime("%b-%Y")
            if issue_month not in self.hor_headers:
                self.hor_headers.append(issue_month)

    def build_model(self):
        reviews = cmredb.get_1on1_reviews()
        xcount = len(reviews)
        row = 0
        for agent in self.vert_headers:
            data_obj = QStandardItem(agent)
            data_obj.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            sort_data = agent.split("-")
            data_obj.setData(sort_data[0], Qt.UserRole + 1)

            new_row = [data_obj]
            for rvw_month in self.hor_headers:
                i = 0
                for item in reviews:
                    i += 1
                    if agent == item[0] and datetime.strptime(item[1], '%Y-%m-%d').strftime('%b-%Y') == rvw_month:
                        data_obj = QStandardItem(datetime.strptime(item[1], '%Y-%m-%d').strftime('%m/%d/%Y'))
                        data_obj.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        data_obj.setTextAlignment(Qt.AlignCenter)
                        data_obj.setData(item[2], Qt.UserRole)
                        data_obj.setData(item[1], Qt.UserRole + 1)

                        new_row.append(data_obj)
                        break
                    else:
                        if i == xcount:
                            data_obj = QStandardItem(" - ")
                            data_obj.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                            data_obj.setTextAlignment(Qt.AlignCenter)
                            new_row.append(data_obj)

            self.oneXoneModel.insertRow(row, new_row)
            row += 1
        self.hor_headers.insert(0, "Collector")
        self.oneXoneModel.setHorizontalHeaderLabels(self.hor_headers)
        self.oneXoneModel.setSortRole(Qt.UserRole + 1)
        self.oneXoneModel.sort(len(self.hor_headers) - 1, Qt.AscendingOrder)
        if self.oneXoneModel.columnCount() == 7:
            self.oneXoneView.horizontalHeader().setStretchLastSection(True)
        self.oneXoneView.resizeColumnsToContents()
        self.oneXoneView.resizeRowsToContents()

    def view_details(self, model):
        collector = self.oneXoneModel.item(model.row(), 0).text()
        if model.column() == 0:
            manager = self.managerCombo.currentText()
            # Creates the agent details window
            agent_window = EmployeeDetails(self.all_users, collector, manager)
            agent_window.addReview.clicked.connect(lambda: self.employee_review(collector))
            agent_window.employeeReviews.clicked.connect(lambda: self.employee_review_search(collector))
            agent_window.exec_()
            self.combobox_changed()
        else:
            rvw_id = model.data(Qt.UserRole)
            if rvw_id:
                rvw_reader = ReviewReader(rvw_id)
                rvw_reader.exec_()
                self.combobox_changed()
            else:
                self.employee_review(collector)
                self.combobox_changed()

    def employee_review(self, coll):
        """Function used to initialize the agent review window."""
        mgr = self.managerCombo.currentText()
        agent_rvw = ReviewForm(mgr, coll)
        agent_rvw.exec_()

    def employee_review_search(self, coll):
        """Function used to review employee reviews window."""
        employee_search = ReviewSearch(coll)
        employee_search.exec_()


class TopFive(QDialog, Ui_top5Agents):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.top_rpcs = cmredb.top_five_rpc()
        self.top_conv = cmredb.top_five_conv()

        self.ModelRPC = QStandardItemModel()
        self.listRPCView.setModel(self.ModelRPC)
        self.ModelConv = QStandardItemModel()
        self.listConvView.setModel(self.ModelConv)

        self.build_models()

    def build_models(self):
        rank = 1
        for item in self.top_rpcs:
            rpcs = '{:.2f}'.format(float(item[0]))
            data_obj = QStandardItem(f'{rank}.  {rpcs} - {item[1]}')
            data_obj.setFlags(Qt.ItemIsEnabled)
            self.ModelRPC.appendRow(data_obj)
            rank += 1
        rank = 1
        for item in self.top_conv:
            conv = '{0:.0%}'.format(float(item[0]))
            data_obj = QStandardItem(f'{rank}.  {conv} - {item[1]}')
            data_obj.setFlags(Qt.ItemIsEnabled)
            self.ModelConv.appendRow(data_obj)
            rank += 1


if __name__ == "__main__":
    if getpass.getuser().lower() in allowed_users:
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
    else:
        app = QApplication(sys.argv)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("You do not have access to this application.\n To gain access, please "
                    "reach out to Jake Boden at x104.")
        msg.setWindowTitle("Access Denied")
        msg.show()
        sys.exit(app.exec_())
