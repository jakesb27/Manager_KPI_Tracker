from math import ceil
from datetime import datetime

from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QDialog, QMessageBox, QHBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis

from agent_input import Ui_agentInput
from agent_maintenance import Ui_agentMaintenance
from agent_details import Ui_agentDetailsMain
from agent_graphs import Ui_agentGraphsMain

import msgbox
import my_styles
import kpidb as cmredb
import cds_sql as cds

current_managers = cmredb.current_managers()


class AddEmployee(QDialog, Ui_agentInput):
    """Class that displays the add employee screen."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_bd_managers = current_managers
        self.all_req_fields = False
        self.agentManager.addItems([mgr for mgr in sorted(self.current_bd_managers)])

        self.ultipro_id = ""
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.user_id = ""
        self.ext = ""
        self.group = ""
        self.manager = ""
        self.desc1 = ""
        self.desc2 = ""
        self.desc3 = ""
        self.base1 = ""
        self.base2 = ""
        self.base3 = ""
        self.goal1 = ""
        self.goal2 = ""
        self.goal3 = ""

        self.addButton.clicked.connect(self.add_employee)
        self.clearButton.clicked.connect(self.clear_form)

    def add_employee(self):
        """Function used to add new employee to CMREDB database."""

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

        # Update class attributes with current values
        self.ultipro_id = self.agentUltiPro.text()
        self.email = self.agentEmail.text().lower()
        self.first_name = self.agentFirstName.text().title()
        self.last_name = self.agentLastName.text().title()
        self.user_id = self.agentUserID.text().upper()
        self.ext = self.agentExt.text()
        self.group = self.agentGroup.text().title()
        if self.agentManager.currentIndex() == 0:
            self.manager = ""
        else:
            self.manager = self.agentManager.currentText()
        self.desc1 = self.agentDesc1.currentText()
        self.desc2 = self.agentDesc2.currentText()
        self.desc3 = self.agentDesc3.currentText()
        self.base1 = self.agentBase1.text()
        self.base2 = self.agentBase2.text()
        self.base3 = self.agentBase3.text()
        self.goal1 = self.agentGoal1.text()
        self.goal2 = self.agentGoal2.text()
        self.goal3 = self.agentGoal3.text()

        # Checks to ensure all required fields are filled out
        if self.check_req_fields():
            msg_confirm = msgbox.confirm_save()
            selection = msg_confirm.exec_()

            # If "Save" was clicked
            if selection == QMessageBox.Save:
                emp_info = [
                    self.ultipro_id,
                    self.last_name,
                    self.first_name,
                    self.user_id,
                    self.email,
                    check_value(self.ext),
                    self.manager,
                    self.group,
                    self.desc1,
                    check_value(self.base1),
                    check_value(self.goal1),
                    self.desc2,
                    check_value(self.base2),
                    check_value(self.goal2),
                    self.desc3,
                    check_value(self.base3),
                    check_value(self.goal3),
                    "Y",
                ]

                # SQL function returns boolean and error
                add_emp_succeeded = cmredb.add_coll(emp_info)
                if add_emp_succeeded:
                    msg_emp_added = msgbox.employee_added()
                    msg_emp_added.exec_()
                    self.clear_form()
                else:
                    error_msg = msgbox.employee_add_dupe()
                    error_msg.exec_()
        else:
            msg_add_error = msgbox.add_data_error()
            msg_add_error.exec_()

    def check_req_fields(self):
        """Function used to check that all required fields are filled out."""
        req_fields = [self.ultipro_id, self.first_name, self.last_name, self.user_id]
        info_provided = False
        for field in req_fields:
            if len(field) < 1:
                info_provided = False
                break
            else:
                info_provided = True
        return info_provided

    def clear_form(self):
        """Function used to clear/reset form."""
        # Clear all text fields and resent comboboxes
        self.agentUltiPro.clear()
        self.agentEmail.clear()
        self.agentFirstName.clear()
        self.agentLastName.clear()
        self.agentUserID.clear()
        self.agentExt.clear()
        self.agentGroup.clear()
        self.agentManager.setCurrentIndex(0)
        self.agentDesc1.setCurrentIndex(0)
        self.agentDesc2.setCurrentIndex(0)
        self.agentDesc3.setCurrentIndex(0)
        self.agentBase1.clear()
        self.agentBase2.clear()
        self.agentBase3.clear()
        self.agentGoal1.clear()
        self.agentGoal2.clear()
        self.agentGoal3.clear()

        # Clear class attributes
        self.ultipro_id = ""
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.user_id = ""
        self.ext = ""
        self.group = ""
        self.manager = ""
        self.desc1 = ""
        self.desc2 = ""
        self.desc3 = ""
        self.base1 = ""
        self.base2 = ""
        self.base3 = ""
        self.goal1 = ""
        self.goal2 = ""
        self.goal3 = ""


class EmployeeMaintenance(QDialog, Ui_agentMaintenance):
    """Employee Maintenance screen used to update and change employee information."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_bd_managers = current_managers
        # Obtains all users from the CMRE database
        self.users = cmredb.all_collectors()
        # Set default flags
        self.user_changed = False
        self.saved = True
        self.primary_key = ''

        # Add managers to combobox
        self.agentManager.addItems([mgr for mgr in sorted(self.current_bd_managers)])

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
            try:
                self.agentGoal.setText('${:,.2f}'.format(desk_totals[0][0]))
            except IndexError:
                self.agentGoal.setText("$0.00")
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
            self.setStyleSheet(my_styles.active_style)
        else:
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
            self.setStyleSheet(my_styles.active_style)

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
        self.active_emp_check()

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

        if self.employeeSelect.currentIndex() > -1:
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
                        self.agentLastName.text().title(),
                        self.agentFirstName.text().title(),
                        self.agentEmail.text().lower(),
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
                    self.clear_window()
                    self.employeeSelect.setCurrentIndex(index)

    def cancel_update(self):
        self.close()


class EmployeeDetails(QDialog, Ui_agentDetailsMain):
    """Class that displays an agents details not shown in the MainWindow."""
    # TODO Add button to add employee review.

    def __init__(self, all_users, coll, mgr):
        super().__init__()
        # Initialize class attributes
        self.setupUi(self)
        self.user_id = ""
        self.all_users = all_users
        self.current_bd_managers = current_managers
        self.managers_agents = []
        self.managerCombo.addItems([mgr for mgr in sorted(self.current_bd_managers)])

        # Sets manager to selected manager from main
        mgr_index = self.managerCombo.findText(mgr)
        if mgr_index == 0:
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.all_users)])
        else:
            # Adds selected manager's employees only
            self.managerCombo.setCurrentIndex(mgr_index)
            self.managers_agents = cmredb.my_collectors(mgr)
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.managers_agents)])

        # Sets the selected employee
        index = self.employeeSelect.findText(coll)
        if index == 0:
            self.update_info()
        else:
            self.employeeSelect.setCurrentIndex(index)
            self.update_info()

        # Connect signals to slots
        self.managerCombo.currentIndexChanged.connect(self.update_combobox)
        self.employeeSelect.currentIndexChanged.connect(self.update_info)
        self.employeeGraphs.clicked.connect(self.employee_graphs)

    def update_combobox(self):
        """Function used to update employee combobox based on the manager selected."""

        coll = self.employeeSelect.currentText()
        # Block signal temporarily
        self.employeeSelect.blockSignals(True)
        self.employeeSelect.clear()

        # If manager is 'All' then all employees are added
        if self.managerCombo.currentIndex() == 0:
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.all_users)])
            index = self.employeeSelect.findText(coll)
            self.employeeSelect.setCurrentIndex(index)
        else:
            # Adds only the employees for the selected manager
            mgr = self.managerCombo.currentText()
            self.managers_agents = cmredb.my_collectors(mgr)
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.managers_agents)])
            index = self.employeeSelect.findText(coll)
            # If the employee cannot be found in the updated employee list
            if index != -1:
                self.employeeSelect.setCurrentIndex(index)

        # Unblock the signal and update employee info
        self.employeeSelect.blockSignals(False)
        self.update_info()

    def update_info(self):
        """Updates the GUI with the newly selected employee's information."""
        coll = self.employeeSelect.currentText().split(' - ')
        self.user_id = coll[0]
        # Obtain agent details by calling function in kpidb.py
        details = cmredb.coll_details(self.user_id)
        # Obtain agent's current KPI's
        curr_kpis = cmredb.daily_kpis(self.user_id)
        # Converts results from a tuple to a list
        coll_details = list(details)
        # Obtain desk details from Oracle DB
        desk_totals = cds.get_desk_totals(coll_details[6])

        self.employeeMisc.setText(f'Email: <a href="mailto:{coll_details[4]}">{coll_details[4]}</a>')

        self.agentName.setText(self.user_id)
        self.agentDesk.setText(coll_details[6])
        self.agentExt.setText(str(coll_details[5]))
        self.agentGoal.setText('${:,.2f}'.format(desk_totals[0][0]))

        self.agentPrinc.setText('${:,.2f}'.format(desk_totals[0][1]))
        self.agentInt.setText('${:,.2f}'.format(desk_totals[0][2]))
        self.agentTotal.setText('${:,.2f}'.format(desk_totals[0][3]))
        self.agentComm.setText('${:,.2f}'.format(desk_totals[0][4]))
        self.agentGroup.setText(coll_details[8])

        try:
            self.agentRPC.setText('{:.2f}'.format(float(curr_kpis[0][4])))
            self.agentConv.setText('{0:.0%}'.format(float(curr_kpis[0][5])))
        except IndexError:
            self.agentRPC.setText('N/A')
            self.agentConv.setText('N/A')

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

    def employee_graphs(self):
        """Function used to initialize the agent graphs window."""
        coll = self.employeeSelect.currentText()
        mgr = self.managerCombo.currentText()

        agent_graphs = EmployeeGraphs(coll, mgr)
        agent_graphs.exec_()


class EmployeeGraphs(QDialog, Ui_agentGraphsMain):
    """Class that displays trending graphs for the selected agent."""

    def __init__(self, coll, mgr):
        super().__init__()
        # Initialize class attributes
        self.setupUi(self)
        self.user_id = ""
        self.current_bd_managers = current_managers
        self.all_users = cmredb.all_collectors()
        self.managers_agents = []
        # Holds index value of selected graph
        self.g1_combo_index = 0
        self.g2_combo_index = 0
        self.g3_combo_index = 0
        self.g4_combo_index = 0

        # Build graph objects
        self.emp_graph_1 = MyGraphs()
        self.graphBox1.setLayout(self.emp_graph_1.layout)
        self.emp_graph_2 = MyGraphs()
        self.graphBox2.setLayout(self.emp_graph_2.layout)
        self.emp_graph_3 = MyGraphs()
        self.graphBox3.setLayout(self.emp_graph_3.layout)
        self.emp_graph_4 = MyGraphs()
        self.graphBox4.setLayout(self.emp_graph_4.layout)

        # Add managers to manager combobox
        self.managerCombo.addItems([mgr for mgr in sorted(self.current_bd_managers)])

        # Sets manager to selected manager from main
        mgr_index = self.managerCombo.findText(mgr)
        if mgr_index == 0:
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.all_users)])
        else:
            # Adds selected manager's employees only
            self.managerCombo.setCurrentIndex(mgr_index)
            self.managers_agents = cmredb.my_collectors(mgr)
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.managers_agents)])

        # Updates employee selection to prev. selected employee if applicable.
        index = self.employeeSelect.findText(coll)
        self.employeeSelect.setCurrentIndex(index)

        # Connect signals and slots
        self.managerCombo.currentIndexChanged.connect(self.update_combobox)
        self.employeeSelect.currentIndexChanged.connect(lambda: self.update_info(0))
        self.graphData1.currentIndexChanged.connect(lambda: self.update_info(1))
        self.graphData2.currentIndexChanged.connect(lambda: self.update_info(2))
        self.graphData3.currentIndexChanged.connect(lambda: self.update_info(3))
        self.graphData4.currentIndexChanged.connect(lambda: self.update_info(4))

        self.update_info(0)

    def update_combobox(self):
        """Function used to update employee combobox based on the manager selected."""

        coll = self.employeeSelect.currentText()
        # Block signal temporarily
        self.employeeSelect.blockSignals(True)
        self.employeeSelect.clear()

        # If manager is 'All' then all employees are added
        if self.managerCombo.currentIndex() == 0:
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.all_users)])
            index = self.employeeSelect.findText(coll)
            self.employeeSelect.setCurrentIndex(index)
        else:
            # Adds only the employees for the selected manager
            mgr = self.managerCombo.currentText()
            self.managers_agents = cmredb.my_collectors(mgr)
            self.employeeSelect.addItems([f'{agent[0]} - {agent[1]}' for agent in sorted(self.managers_agents)])
            index = self.employeeSelect.findText(coll)
            # If the employee cannot be found in the updated employee list
            if index != -1:
                self.employeeSelect.setCurrentIndex(index)

        # Unblock the signal and update employee info
        self.employeeSelect.blockSignals(False)
        self.update_info(0)

    def update_info(self, gp_trig):
        """Updates class attribute values when a combobox is changed."""
        coll = self.employeeSelect.currentText().split(' - ')
        self.user_id = coll[0]

        self.g1_combo_index = self.graphData1.currentIndex()
        self.g2_combo_index = self.graphData2.currentIndex()
        self.g3_combo_index = self.graphData3.currentIndex()
        self.g4_combo_index = self.graphData4.currentIndex()

        self.draw_graphs(gp_trig)

    def draw_graphs(self, gp_trig):
        """Builds the visual graph objects based on the signal that was triggered."""

        if gp_trig == 0:
            self.emp_graph_1.build_graph(self.user_id, self.g1_combo_index)
            self.emp_graph_2.build_graph(self.user_id, self.g2_combo_index)
            self.emp_graph_3.build_graph(self.user_id, self.g3_combo_index)
            self.emp_graph_4.build_graph(self.user_id, self.g4_combo_index)
        elif gp_trig == 1:
            self.emp_graph_1.build_graph(self.user_id, self.g1_combo_index)
        elif gp_trig == 2:
            self.emp_graph_2.build_graph(self.user_id, self.g2_combo_index)
        elif gp_trig == 3:
            self.emp_graph_3.build_graph(self.user_id, self.g3_combo_index)
        elif gp_trig == 4:
            self.emp_graph_4.build_graph(self.user_id, self.g4_combo_index)


class MyGraphs:
    """Class used to create a graph template for the trending graph GUI."""

    def __init__(self):
        """Initialize the graph object and add it to the trending graph GUI."""
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().setVisible(False)
        self.chartview = QChartView(self.chart)

        self.axisY = QValueAxis()
        self.axisX = QBarCategoryAxis()

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.chartview)

    def build_graph(self, user_id, combo_index):
        """Builds the graph axes and series with the employee's data."""

        def bar_hover(active, index):
            """Slot for the mouse hover signal on the QBarSet."""
            # If mouse is hovering over the bar, active is "True"
            if active:
                value = bar_values.at(index)
                # Determines the correct bar value formatting based on the graph type
                if combo_index in (4, 11):
                    self.chart.setToolTip('{0:.0f}%'.format(value))
                elif combo_index in (0, 2, 7, 9):
                    self.chart.setToolTip('{0:.0f}'.format(value))
                elif combo_index in (5, 6, 12):
                    self.chart.setToolTip('${0:,.2f}'.format(value))
                else:
                    self.chart.setToolTip('{0:.2f}'.format(value))
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
        coll_data = []

        # Creates QBarSet and connects the hover signal to the slot
        bar_values = QBarSet("")
        bar_values.hovered.connect(bar_hover)

        # Determines the type of graph and fetches the correct data from the CMREDB
        if combo_index == 0:
            coll_data = cmredb.monthly_rpcs(user_id)
        elif combo_index == 1:
            coll_data = cmredb.monthly_rpcs_ph(user_id)
        elif combo_index == 2:
            coll_data = cmredb.monthly_conn(user_id)
        elif combo_index == 3:
            coll_data = cmredb.monthly_conn_ph(user_id)
        elif combo_index == 4:
            coll_data = cmredb.monthly_conv(user_id)
        elif combo_index == 5:
            coll_data = cmredb.monthly_fees(user_id)
        elif combo_index == 6:
            coll_data = cmredb.monthly_totals(user_id)
        elif combo_index == 7:
            coll_data = cmredb.weekly_rpcs(user_id)
        elif combo_index == 8:
            coll_data = cmredb.weekly_rpcs_ph(user_id)
        elif combo_index == 9:
            coll_data = cmredb.weekly_conn(user_id)
        elif combo_index == 10:
            coll_data = cmredb.weekly_conn_ph(user_id)
        elif combo_index == 11:
            coll_data = cmredb.weekly_conv(user_id)
        elif combo_index == 12:
            coll_data = cmredb.weekly_fees(user_id)
        else:
            coll_data = []

        # Iterate over results and update variables with correctly formatted data
        if len(coll_data) > 0:
            self.chart.setTitle("")
            for item in coll_data:
                if item[1] > y_max:
                    y_max = item[1]
                # Determines the correct date format; monthly or weekly
                if combo_index < 7:
                    frmt_date = datetime.strptime(item[0], '%Y-%m-%d').strftime('%b-%y')
                    x_values.append(frmt_date)
                else:
                    frmt_date = datetime.strptime(item[0], '%Y-%m-%d').strftime('%b-%d')
                    x_values.append(frmt_date)
                # Converts conversion rate to whole number
                if combo_index in (4, 11):
                    bar_values.append(item[1] * 100)
                else:
                    bar_values.append(item[1])

            # Create series object and set axes to series and chart
            series = QBarSeries()
            series.append(bar_values)
            self.chart.addSeries(series)
            self.axisX.append(x_values)

            # Determines the correct graph type and applies correct label format
            if combo_index in (4, 11):  # Percentage format
                self.axisY.setRange(0, (y_max + .1) * 100)
                self.axisY.setLabelFormat("%0.0f %%")
            elif combo_index in (0, 2, 7, 9):  # Whole number format
                self.axisY.setRange(0, ceil(y_max / 100) * 100)
                self.axisY.setLabelFormat("%d")
            elif combo_index in (5, 6, 12):  # Currency format
                # Round number to nearest thousand or ten-thousand
                if combo_index == 6:
                    self.axisY.setRange(0, ceil(y_max / 10000) * 10000)
                else:
                    self.axisY.setRange(0, ceil(y_max / 1000) * 1000)
                self.axisY.setLabelFormat("$%0.0f")
            else:   # float format
                self.axisY.setRange(0, ceil(y_max) + 1)
                self.axisY.setTickCount(1)
                self.axisY.setLabelFormat("%0.2f")

            self.chart.setAxisX(self.axisX)
            self.chart.setAxisY(self.axisY)
            series.attachAxis(self.axisX)
            series.attachAxis(self.axisY)
        else:
            self.chart.setTitle("Missing Employee or Graph Data Selection")
