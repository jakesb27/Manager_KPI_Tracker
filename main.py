import sys
import time
import getpass

from datetime import datetime, timedelta, date
from math import ceil
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QResizeEvent, QIcon, QPixmap, QPainter, QFont, QKeyEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal

import cds_sql
import kpidb as cmredb
import cds_sql as cds
import my_styles
import msgbox
from manager_main import Ui_managerMain
from agent_details import Ui_agentDetailsMain
from agent_maintenance import Ui_agentMaintenance

# Column headers used to build QStandardItemModel
headers = ['User ID', 'Collector', 'Start Time', "RPC's Per Hour", 'Conversion Rate', 'Last Update']
managers = cmredb.managers()


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
                # Kills loop if the current time is past 5:40 PM
                # Sends signal to main thread's slot connected to 'update_status' function
                self.updt_main_stsbar.emit(datetime.strftime(curr_time, '%I:%M:%S %p'), '0:00 min')
                self.close_app.emit()
                time.sleep(10)
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

    def update_desks(self):
        results = cds.get_act_desks()
        for result in results:
            cmredb.update_desks(result)


class EmployeeMaintenance(QDialog, Ui_agentMaintenance):
    """Employee Maintenance screen used to update and change employee information."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Obtains all users from the CMRE database
        self.users = cmredb.all_collectors()
        # Set default flags
        self.user_changed = False
        self.saved = True
        self.primary_key = ''

        # Adds employees to combo box
        self.employeeSelect.addItem(f'- Select Employee -')
        for item in sorted(self.users):
            self.employeeSelect.addItem(f'{item[0]} - {item[1]}')

        # Connectes signals to slots for push buttons
        self.employeeSelect.currentIndexChanged.connect(self.update_window)
        self.clearButton.clicked.connect(self.clear_window)
        self.cancelButton.clicked.connect(self.cancel_update)
        self.saveButton.clicked.connect(self.save_window)
        self.undoButton.clicked.connect(self.undo_changes)

        # Connects signals to slots for all metadata objects
        self.agentFirstName.textChanged.connect(self.save_enabled)
        self.agentLastName.textChanged.connect(self.save_enabled)
        self.agentExt.textChanged.connect(self.save_enabled)
        self.agentManager.currentIndexChanged.connect(self.save_enabled)
        self.agentGroup.textChanged.connect(self.save_enabled)
        self.agentEmail.textChanged.connect(self.save_enabled)
        self.activeEmpBox.clicked.connect(self.active_changed)
        self.agentDesc1.currentIndexChanged.connect(self.save_enabled)
        self.agentDesc2.currentIndexChanged.connect(self.save_enabled)
        self.agentDesc3.currentIndexChanged.connect(self.save_enabled)
        self.agentBase1.textChanged.connect(self.save_enabled)
        self.agentBase2.textChanged.connect(self.save_enabled)
        self.agentBase3.textChanged.connect(self.save_enabled)
        self.agentGoal1.textChanged.connect(self.save_enabled)
        self.agentGoal2.textChanged.connect(self.save_enabled)
        self.agentGoal3.textChanged.connect(self.save_enabled)

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        key = a0.nativeVirtualKey()
        if key == 13:
            widget = QApplication.focusWidget()
            if isinstance(widget, QComboBox):
                widget.showPopup()

    def save_enabled(self):
        """Detects a value has changed but not saved and warns user to save before exiting.
        Once saved the flag will return to True."""
        if self.user_changed:
            self.active_emp_check()
            self.saveLabel.setStyleSheet("QLabel{color: rgba(255, 0, 0, 255);}")
            self.saved = False
        else:
            self.saveLabel.setStyleSheet("QLabel{color: rgba(255, 0, 0, 0);}")

    def update_window(self):
        """Updates the window with the employees current data."""

        if self.employeeSelect.currentIndex() != 0:
            # Sets user changed flag to false since loading default employee info
            self.user_changed = False
            # Obtains employee data from CMRE database
            user_id = self.employeeSelect.currentText().split(' - ')[0]
            coll_details = cmredb.coll_details(user_id)

            # Updates all available fields with data
            self.primary_key = coll_details[0]
            self.agentFirstName.setText(coll_details[2])
            self.agentLastName.setText(coll_details[1])
            self.agentExt.setText(str(coll_details[5]))
            self.agentDesk.setText(coll_details[6])
            desk_totals = cds.get_desk_totals(coll_details[6])
            self.agentGoal.setText('${:,.2f}'.format(desk_totals[0][0]))
            self.agentManager.setCurrentText(coll_details[7])
            self.agentGroup.setText(coll_details[8])
            self.agentEmail.setText(coll_details[4])

            self.agentDesc1.setCurrentText(coll_details[9])
            self.agentDesc2.setCurrentText(coll_details[12])
            self.agentDesc3.setCurrentText(coll_details[15])

            self.agentBase1.setText(str(coll_details[10]))
            self.agentBase2.setText(str(coll_details[13]))
            self.agentBase3.setText(str(coll_details[16]))

            self.agentGoal1.setText(str(coll_details[11]))
            self.agentGoal2.setText(str(coll_details[14]))
            self.agentGoal3.setText(str(coll_details[17]))

            # Sets "Employee Active" checkbox flag and sets new stylesheet
            if coll_details[18] == 'Y':
                self.activeEmpBox.setChecked(True)
            else:
                self.activeEmpBox.setChecked(False)

            # Return user changed flag to True to track any changes to the employee
            self.user_changed = True
            self.active_emp_check()
        else:
            self.clear_window()

    def active_emp_check(self):
        if self.activeEmpBox.checkState() == 2:
            self.setStyleSheet(my_styles.active_emp)
            self.agentFirstName.setReadOnly(False)
            self.agentLastName.setReadOnly(False)
            self.agentEmail.setReadOnly(False)
            self.agentExt.setReadOnly(False)
            self.agentGroup.setReadOnly(False)
            self.agentManager.setDisabled(False)
            self.agentDesc1.setDisabled(False)
            self.agentBase1.setReadOnly(False)
            self.agentGoal1.setReadOnly(False)
            self.agentDesc2.setDisabled(False)
            self.agentBase2.setReadOnly(False)
            self.agentGoal2.setReadOnly(False)
            self.agentDesc3.setDisabled(False)
            self.agentBase3.setReadOnly(False)
            self.agentGoal3.setReadOnly(False)
        else:
            self.setStyleSheet(my_styles.inactive_emp)
            self.agentFirstName.setReadOnly(True)
            self.agentLastName.setReadOnly(True)
            self.agentEmail.setReadOnly(True)
            self.agentExt.setReadOnly(True)
            self.agentGroup.setReadOnly(True)
            self.agentManager.setDisabled(True)
            self.agentDesc1.setDisabled(True)
            self.agentBase1.setReadOnly(True)
            self.agentGoal1.setReadOnly(True)
            self.agentDesc2.setDisabled(True)
            self.agentBase2.setReadOnly(True)
            self.agentGoal2.setReadOnly(True)
            self.agentDesc3.setDisabled(True)
            self.agentBase3.setReadOnly(True)
            self.agentGoal3.setReadOnly(True)

    def active_changed(self):
        if self.activeEmpBox.checkState() == 0:
            msg = msgbox.inactive_warning()
            selection = msg.exec()
            if selection != QMessageBox.Ok:
                self.activeEmpBox.setChecked(True)
                self.active_emp_check()
            else:
                self.save_enabled()
        else:
            self.save_enabled()

    def undo_changes(self):
        """Resets screen to employee defaults and erases any unsaved changes."""
        index = self.employeeSelect.currentIndex()
        self.clear_window()
        self.employeeSelect.setCurrentIndex(index)

    def clear_window(self):
        """Clears entire screen including the previously selected employee."""
        self.user_changed = False
        self.employeeSelect.setCurrentIndex(0)
        self.agentFirstName.clear()
        self.agentLastName.clear()
        self.agentExt.clear()
        self.agentDesk.clear()
        self.agentGoal.clear()
        self.agentManager.setCurrentIndex(0)
        self.agentGroup.clear()
        self.agentEmail.clear()
        self.activeEmpBox.setChecked(False)

        self.agentDesc1.setCurrentIndex(0)
        self.agentDesc2.setCurrentIndex(0)
        self.agentDesc3.setCurrentIndex(0)

        self.agentBase1.clear()
        self.agentBase2.clear()
        self.agentBase3.clear()

        self.agentGoal1.clear()
        self.agentGoal2.clear()
        self.agentGoal3.clear()
        self.user_changed = True

    def save_window(self):
        """Saves any unsaved changes made to an employee."""

        def check_value(value):
            """Attempts to convert string to int or float type."""
            try:
                # Attempts to convert to integer
                new_value = int(value)
            except ValueError:
                try:
                    # If unable to convert to integer, converts to float
                    new_value = float(value)
                except ValueError:
                    new_value = None
            return new_value

        def clear_goals():
            if active == "N":
                self.agentDesc1.setCurrentIndex(0)
                self.agentBase1.clear()
                self.agentGoal1.clear()
                self.agentDesc2.setCurrentIndex(0)
                self.agentBase2.clear()
                self.agentGoal2.clear()
                self.agentDesc3.setCurrentIndex(0)
                self.agentBase3.clear()
                self.agentGoal3.clear()

        def confirm_msg():
            msg = msgbox.confirm_save()
            selection = msg.exec()
            return selection

        if confirm_msg() == QMessageBox.Save:
            if not self.saved:
                self.user_changed = False
                index = self.employeeSelect.currentIndex()
                # Checks employee's active flag.
                if self.activeEmpBox.checkState() == 2:
                    active = "Y"
                else:
                    active = "N"
                clear_goals()
                # Creates list of employee data to be saved to CMRE db
                updated_details = [
                    self.agentLastName.text(),
                    self.agentFirstName.text(),
                    self.agentEmail.text(),
                    check_value(self.agentExt.text()),
                    self.agentManager.currentText(),
                    self.agentGroup.text(),
                    self.agentDesc1.currentText(),
                    check_value(self.agentBase1.text()),
                    check_value(self.agentGoal1.text()),
                    self.agentDesc2.currentText(),
                    check_value(self.agentBase2.text()),
                    check_value(self.agentGoal2.text()),
                    self.agentDesc3.currentText(),
                    check_value(self.agentBase3.text()),
                    check_value(self.agentGoal3.text()),
                    active,
                    self.primary_key
                ]
                cmredb.update_coll(updated_details)
                self.save_enabled()
                window.refresh_manager_lists()
                self.clear_window()
                self.employeeSelect.setCurrentIndex(index)

    def cancel_update(self):
        self.close()


class EmployeeGraph:
    """Class used to create a graph template for the Employee Details."""

    def __init__(self, title):
        """Initialize the graph object and add it to the Employee Details GUI."""
        self.chart = QChart()
        self.chart.setTitle(title)
        self.title_font = QFont("MS Shell Dig 2", 12, 1)
        self.chart.setTitleFont(self.title_font)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().setVisible(False)
        self.chartview = QChartView(self.chart)

        self.axisY = QValueAxis()
        self.axisX = QBarCategoryAxis()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.chartview)

    def build_graph(self, user_id, month, rpc):
        """Builds the graph axes and series with the employee's data."""

        def bar_hover(active, index):
            """Slot for the mouse hover signal on the QBarSet."""
            # If mouse is hovering over the bar, active is "True"
            if active:
                value = bar_values.at(index)
                # Determines the correct formatting for rpc or conv graph
                if rpc == "yes":
                    self.chart.setToolTip(str(value))
                if rpc == "no":
                    self.chart.setToolTip('{0:.0f}%'.format(value))
            else:
                self.chart.setToolTip("")

        # Resets the axes and series of the graph
        self.chart.removeAllSeries()
        self.axisX.clear()
        self.chart.removeAxis(self.axisY)
        self.chart.removeAxis(self.axisX)

        # Global variables
        x_values = []
        y_max = 0
        coll_data = None

        # Creates QBarSet and connects the hover signal to the slot
        bar_values = QBarSet("")
        bar_values.hovered.connect(bar_hover)

        # Determines the type of graph and fetches the correct data from the CMREDB
        if month == "yes" and rpc == "yes":
            coll_data = cmredb.monthly_rpcs(user_id)
        elif month == "no" and rpc == "yes":
            coll_data = cmredb.weekly_rpcs(user_id)
        elif month == "yes" and rpc == "no":
            coll_data = cmredb.monthly_conv(user_id)
        elif month == "no" and rpc == "no":
            coll_data = cmredb.weekly_conv(user_id)

        # Iterate over results and update variables with correctly formatted data
        for item in coll_data:
            if item[1] > y_max:
                y_max = item[1]
            # Determines the correct date format; monthly or weekly
            if month == "yes":
                frmt_date = datetime.strptime(item[0], '%Y-%m-%d').strftime('%b-%y')
                x_values.append(frmt_date)
            elif month == "no":
                frmt_date = datetime.strptime(item[0], '%Y-%m-%d').strftime('%b-%d')
                x_values.append(frmt_date)
            # Determines the correct graph type; RPC or Conversions
            if rpc == "yes":
                bar_values.append(item[1])
            if rpc == "no":
                bar_values.append(item[1] * 100)

        # Create series object and set axes to series and chart
        series = QBarSeries()
        series.append(bar_values)
        self.chart.addSeries(series)
        self.axisX.append(x_values)
        # Determines the correct graph type; RPC or Conversions and applies correct format
        if rpc == "yes":
            self.axisY.setRange(0, ceil(y_max) + 1)
            self.axisY.setTickCount(1)
        elif rpc == "no":
            self.axisY.setRange(0, (y_max + .1) * 100)
            self.axisY.setLabelFormat("%0.0f %%")
        self.chart.setAxisX(self.axisX)
        self.chart.setAxisY(self.axisY)
        series.attachAxis(self.axisX)
        series.attachAxis(self.axisY)


class AgentDetails(QDialog, Ui_agentDetailsMain):
    """Class that displays an agents details not shown in the MainWindow."""

    def __init__(self, coll):
        super().__init__()
        # Initialize class attributes
        self.setupUi(self)
        self.user_id = ""

        # Build graph objects
        self.month_rpc_gp = EmployeeGraph("Monthly RPC's")
        self.monthRPCbox.setLayout(self.month_rpc_gp.layout)
        self.week_rpc_gp = EmployeeGraph("Weekly RPC's")
        self.weekRPCbox.setLayout(self.week_rpc_gp.layout)
        self.month_conv_gp = EmployeeGraph("Monthly Conv. Rate")
        self.monthConvBox.setLayout(self.month_conv_gp.layout)
        self.week_conv_gp = EmployeeGraph("Weekly Conv. Rate")
        self.weekConvBox.setLayout(self.week_conv_gp.layout)

        self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(window.all_users)])
        self.employeeSelect.currentIndexChanged.connect(self.update_info)

        # Triggers the currentIndexChanged event when initializing with the index
        # that matches the employee selected from the main window.
        index = self.employeeSelect.findText(coll)
        if index == 0:
            self.update_info()
        else:
            self.employeeSelect.setCurrentIndex(index)

    def update_info(self):
        """Updates the GUI with the newly selected employee's information."""
        coll = self.employeeSelect.currentText().split(' - ')
        self.user_id = coll[0]
        self.coll_info()
        self.month_rpc_gp.build_graph(self.user_id, month="yes", rpc="yes")
        self.week_rpc_gp.build_graph(self.user_id, month="no", rpc="yes")
        self.month_conv_gp.build_graph(self.user_id, month="yes", rpc="no")
        self.week_conv_gp.build_graph(self.user_id, month="no", rpc="no")

    def coll_info(self):
        # Obtain agent details by calling function in kpidb.py
        details = cmredb.coll_details(self.user_id)
        # Obtain agent's current KPI's
        curr_kpis = cmredb.daily_kpis(self.user_id)
        # Converts results from a tuple to a list
        coll_details = list(details)
        # Obtain desk details from Oracle DB
        desk_totals = cds.get_desk_totals(coll_details[6])

        self.employeeMisc.setText(f'Email: <a href="mailto:{coll_details[4]}">{coll_details[4]}</a>')

        self.agentName.setText(f'{coll_details[2]} {coll_details[1]}')
        self.agentDesk.setText(coll_details[6])
        self.agentExt.setText(str(coll_details[5]))
        self.agentGoal.setText('${:,.2f}'.format(desk_totals[0][0]))

        self.agentPrinc.setText('${:,.2f}'.format(desk_totals[0][1]))
        self.agentInt.setText('${:,.2f}'.format(desk_totals[0][2]))
        self.agentTotal.setText('${:,.2f}'.format(desk_totals[0][3]))
        self.agentComm.setText('${:,.2f}'.format(desk_totals[0][4]))

        try:
            self.agentRPC.setText('{:.2f}'.format(float(curr_kpis[0][3])))
            self.agentConv.setText('{0:.0%}'.format(float(curr_kpis[0][4])))
        except IndexError:
            self.agentRPC.setText('Not Logged In')
            self.agentConv.setText('Not Logged In')

        self.agentDesc1.setText(coll_details[9])
        self.agentDesc2.setText(coll_details[12])
        self.agentDesc3.setText(coll_details[15])

        self.agentBase1.setText(str(coll_details[10]))
        self.agentBase2.setText(str(coll_details[13]))
        self.agentBase3.setText(str(coll_details[16]))

        self.agentGoal1.setText(str(coll_details[11]))
        self.agentGoal2.setText(str(coll_details[14]))
        self.agentGoal3.setText(str(coll_details[17]))

        # Checks if total collected is greater then the collector's goal
        if desk_totals[0][3] > desk_totals[0][0]:
            self.agentTotal.setStyleSheet("""
            QLineEdit{
                background-color: rgb(10, 211, 0);
            }""")
        else:
            self.agentTotal.setStyleSheet("""
            QLineEdit{
                background-color: rgb(223, 223, 223);
            }""")
        

class Window(QMainWindow, Ui_managerMain):
    """Main tracker window that Managers use to track Agent's current KPI's"""

    def __init__(self):
        super().__init__()
        # Creates the main window UI and initialize class attributes
        self.setupUi(self)

        # Import users from CMRE database
        self.all_users = cmredb.all_act_collectors()
        self.pattys_team = cmredb.my_collectors('Patty')
        self.roberts_team = cmredb.my_collectors('Robert')
        self.shanas_team = cmredb.my_collectors('Shana')
        self.stephanies_team = cmredb.my_collectors('Stephanie')

        # Default sort is set to RPC's
        self.user_sort_col = 3
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
        self.actionUpdate_Employee.triggered.connect(self.employee_maintenance)
        self.actionRun_Desk_Goal_Update.triggered.connect(self.update_desks)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Method used for handling column width when the user resizes the main UI"""
        super().resizeEvent(event)
        table_width = self.agentTableView.width()
        set_width = 700
        # Takes table width * column's min possible width / table's min possible width
        # If a column is added, add the min column width to the total table width
        self.agentTableView.setColumnWidth(0, int(table_width * 60 / set_width))
        self.agentTableView.setColumnWidth(1, int(table_width * 170 / set_width))
        self.agentTableView.setColumnWidth(2, int(table_width * 115 / set_width))
        self.agentTableView.setColumnWidth(3, int(table_width * 110 / set_width))
        self.agentTableView.setColumnWidth(4, int(table_width * 125 / set_width))
        self.agentTableView.setColumnWidth(5, int(table_width * 90 / set_width))

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

    def refresh_manager_lists(self):
        self.all_users = cmredb.all_collectors()
        self.pattys_team = cmredb.my_collectors('Patty')
        self.roberts_team = cmredb.my_collectors('Robert')
        self.shanas_team = cmredb.my_collectors('Shana')
        self.stephanies_team = cmredb.my_collectors('Stephanie')

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

        # Determine which users to add to QStandardItemModel based on manager
        # selected then calls 'build_model' function passing said users.
        if self.managerCombo.currentText() == 'Patty':
            self.build_model(self.pattys_team)
        elif self.managerCombo.currentText() == 'Robert':
            self.build_model(self.roberts_team)
        elif self.managerCombo.currentText() == 'Shana':
            self.build_model(self.shanas_team)
        elif self.managerCombo.currentText() == 'Stephanie':
            self.build_model(self.stephanies_team)
        else:
            self.build_model(self.all_users)

    def build_model(self, collectors):
        """Function used to build the QStandardItemModel based on user selection."""

        # Users is a nested list of user ID and name [['JSB', 'Jake Boden'], ]
        for coll in collectors:
            # Get user specific stats calling function from kpidb.py passing the User ID
            agent_stats = cmredb.daily_kpis(coll[0])
            # Check if result is null
            if len(agent_stats) > 0:
                # Convert tuple to list
                list_stats = list(agent_stats[0])
                # Format RPC's
                rpcs = '{:.2f}'.format(float(list_stats[3]))
                # Update list with formatted RPC's
                list_stats[3] = rpcs
                # Format conversion rate
                conv = '{0:.0%}'.format(float(list_stats[4]))
                # Uodate list with formatted conversion rate
                list_stats[4] = conv
                # Remove DAY from index 2
                list_stats.pop(2)
                # Insert collectors name. (User ID, Name, Start Time, RPC's, Conv, Last Update)
                list_stats.insert(1, coll[1])
            else:
                # Query returned no results which indicates user has not logged into Agent Tracker
                list_stats = [coll[0], coll[1], 'Not Logged In', '0.0', '0.0%', 'N/A']

            # Converts items in list to a QStandardItem which is required for PyQt5
            # All number and text formatting should be done PRIOR to converting
            for index, item in enumerate(list_stats):
                # Creates the QStandardItem from string object
                data_obj = QStandardItem(item)

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
        self.agentModel.sort(self.user_sort_col, self.user_sort_order)

        # Sets column widths based on current table width
        if self.agentTableView.width() == 541:
            self.agentTableView.resizeColumnsToContents()
        self.agentTableView.resizeRowsToContents()

    def update_status(self, time, count_down):
        """Simple function used to update status bar message."""
        self.statusbar.showMessage(f'Last updated at {time}. Next update in {count_down}.')

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

        # Creates the agent details window
        agent_window = AgentDetails(collector)
        agent_window.exec_()

    def employee_maintenance(self):
        """Function used to initialize the employee maintenance window"""
        emp_main = EmployeeMaintenance()
        emp_main.exec_()

    def update_desks(self):
        """Function used to update the desk and goals for all employees in the CMRE db."""

        # Create thread object
        thread = QThread()
        # Create worker object
        worker = Worker()
        # Pass worker to thread for handling
        worker.moveToThread(thread)
        # Connect default signals and slots
        thread.started.connect(worker.update_desks)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)

        # Start the thread
        thread.start()

    def closing_time(self):
        """Function is called when user tries to run app after 5:40 pm. Will
        also force close the app if left open overnight."""
        msg = QMessageBox()
        icon = QIcon()
        icon.addPixmap(QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"),
                       QIcon.Normal, QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Question)
        msg.setText("It's now 5:40 and time to stop working.\nDon't you agree?")
        msg.setWindowTitle("Closing Time")
        msg.setStandardButtons(QMessageBox.Ok)
        return_value = msg.exec()
        if return_value == QMessageBox.Ok:
            app.quit()


if __name__ == "__main__":
    if getpass.getuser().lower() in managers:
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
    else:
        app = QApplication(sys.argv)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("You do not have access to this application.\n To gain access, please reach out Jake Boden x104.")
        msg.setWindowTitle("Access Denied")
        msg.show()
        sys.exit(app.exec_())
