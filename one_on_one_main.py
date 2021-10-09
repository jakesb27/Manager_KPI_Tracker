# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Files\one_on_one_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_oneOnOneMain(object):
    def setupUi(self, oneOnOneMain):
        oneOnOneMain.setObjectName("oneOnOneMain")
        oneOnOneMain.resize(788, 423)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/Images/Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        oneOnOneMain.setWindowIcon(icon)
        oneOnOneMain.setStyleSheet("QMainWindow{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));\n"
"}\n"
"QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));\n"
"}\n"
"QWidget{\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QPlainTextEdit{\n"
"    border: 1px solid black;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPlainTextEdit[readOnly=\"true\"]{\n"
"    background-color: rgb(225, 225, 225);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(80, 80, 80);\n"
"}\n"
"QDateEdit{\n"
"    background-color: rgb(223, 223, 223);\n"
"    border: 1px solid rgb(95, 158, 195);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(95, 158, 195);\n"
"    border-right: 2px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(95, 158, 195);\n"
"    border-radius: 3px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"QDateEdit::drop-down{\n"
"    background-color: rgb(215, 215, 215);\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(95, 158, 195);\n"
"    border-right: 2px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(95, 158, 195);\n"
"    border-radius: 3px;\n"
"    subcontrol-origin: margin;\n"
"    width: 18px;\n"
"}\n"
"QDateEdit::down-arrow{\n"
"    image: url(:/arrows/Images/arrow-dwn.png);\n"
"    width: 14 px;\n"
"    height:14 px;\n"
"}\n"
"QGroupBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex;\n"
"    padding-top: 18;\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QGroupBox::title{\n"
"    background-color: qlineargradient(spread:pad, x1:0.50035, y1:1, x2:0.5, y2:0, stop:0 rgba(151, 151, 151, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"    padding: 2 10px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid rgb(95, 158, 195);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit[readOnly=\"true\"]{\n"
"    background-color: rgb(200, 200, 200);\n"
"    border: 1px solid rgb(95, 158, 195);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTextEdit{\n"
"    font: 12pt \"Corbel\";\n"
"}\n"
"QStatusBar{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(95, 158, 195);\n"
"    border-right: 2px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(95, 158, 195);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    padding-left: 13px;\n"
"    padding-right: 13px;\n"
"    background-color: rgb(225, 225, 225);\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton::hover{\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(95, 158, 195);\n"
"    border-right: 2px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(95, 158, 195);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    padding-left: 13px;\n"
"    padding-right: 13px;\n"
"    background-color: rgb(215, 215, 215);\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton::pressed{\n"
"    border-bottom: 1px solid rgb(75, 124, 154);\n"
"    border-top: 2px solid rgb(95, 158, 195);\n"
"    border-right: 1px solid rgb(75, 124, 154);\n"
"    border-left: 2px solid rgb(95, 158, 195);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    width: 80px;\n"
"    background-color: rgb(225, 225, 225);\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QComboBox{\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(75, 124, 154);\n"
"    border-right: 1px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(75, 124, 154);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"QComboBox::drop-down{\n"
"    background-color: rgb(215, 215, 215);\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(95, 158, 195);\n"
"    border-right: 2px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(95, 158, 195);\n"
"    border-radius: 3px;\n"
"    subcontrol-origin: margin;\n"
"    width: 16px;\n"
"}\n"
"QComboBox::drop-down::hover{\n"
"    background-color: rgb(205, 205, 205);\n"
"    border-bottom: 2px solid rgb(75, 124, 154);\n"
"    border-top: 1px solid rgb(95, 158, 195);\n"
"    border-right: 2px solid rgb(75, 124, 154);\n"
"    border-left: 1px solid rgb(95, 158, 195);\n"
"    border-radius: 3px;\n"
"    subcontrol-origin: margin;\n"
"    width: 16px;\n"
"}\n"
"QComboBox::drop-down::pressed{\n"
"    background-color: rgb(215, 215, 215);\n"
"    border-bottom: 1px solid rgb(75, 124, 154);\n"
"    border-top: 2px solid rgb(95, 158, 195);\n"
"    border-right: 1px solid rgb(75, 124, 154);\n"
"    border-left: 2px solid rgb(95, 158, 195);\n"
"    border-radius: 3px;\n"
"    subcontrol-origin: margin;\n"
"    width: 16px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(:/arrows/Images/arrow-dwn.png);\n"
"    width: 14 px;\n"
"    height:14 px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"    background-color: qlineargradient(spread:pad, x1:0.50035, y1:1, x2:0.5, y2:0, stop:0 rgba(151, 151, 151, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top: 1px solid black;\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QCalendarWidget QToolButton{\n"
"    color: rgb(0, 0, 0);\n"
"      icon-size: 20px, 20px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth{\n"
"    qproperty-icon: url(:/arrows/Images/arrow-left.png);\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth{\n"
"    qproperty-icon: url(:/arrows/Images/arrow-right.png);\n"
"}\n"
"QCalendarWidget QSpinBox{ \n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QCalendarWidget QMenu{\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QCalendarWidget QWidget{\n"
"    alternate-background-color: rgb(234, 234, 234);\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"    font: 12pt \"Corbel\";\n"
"    font-weight: bold;\n"
"    background-color: rgb(214, 214, 214);\n"
"      selection-background-color: rgb(64, 64, 64);\n"
"    selection-color: rgb(255, 255, 255);\n"
"    border: 1px solid black;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"    color: rgb(64, 64, 64); \n"
"}")
        self.centralwidget = QtWidgets.QWidget(oneOnOneMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.managerCombo = QtWidgets.QComboBox(self.centralwidget)
        self.managerCombo.setMinimumSize(QtCore.QSize(150, 0))
        self.managerCombo.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.managerCombo.setObjectName("managerCombo")
        self.managerCombo.addItem("")
        self.gridLayout.addWidget(self.managerCombo, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 93))
        self.label_2.setMaximumSize(QtCore.QSize(200, 93))
        self.label_2.setStyleSheet("image: url(:/logos/Images/Meduit Email.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 4, 1, 1)
        self.agentTableView = QtWidgets.QTableView(self.centralwidget)
        self.agentTableView.setMinimumSize(QtCore.QSize(770, 0))
        self.agentTableView.setStyleSheet("QTableView{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.agentTableView.setAlternatingRowColors(True)
        self.agentTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.agentTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.agentTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.agentTableView.setSortingEnabled(True)
        self.agentTableView.setObjectName("agentTableView")
        self.gridLayout.addWidget(self.agentTableView, 5, 0, 1, 5)
        oneOnOneMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(oneOnOneMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 24))
        self.menubar.setObjectName("menubar")
        oneOnOneMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(oneOnOneMain)
        self.statusbar.setObjectName("statusbar")
        oneOnOneMain.setStatusBar(self.statusbar)
        self.actionUpdate_Employee = QtWidgets.QAction(oneOnOneMain)
        self.actionUpdate_Employee.setObjectName("actionUpdate_Employee")
        self.actionRun_Desk_Goal_Update = QtWidgets.QAction(oneOnOneMain)
        self.actionRun_Desk_Goal_Update.setObjectName("actionRun_Desk_Goal_Update")
        self.actionAdd_Employee = QtWidgets.QAction(oneOnOneMain)
        self.actionAdd_Employee.setObjectName("actionAdd_Employee")
        self.actionTrending_Graphs = QtWidgets.QAction(oneOnOneMain)
        self.actionTrending_Graphs.setObjectName("actionTrending_Graphs")
        self.actionAdd_Employee_2 = QtWidgets.QAction(oneOnOneMain)
        self.actionAdd_Employee_2.setObjectName("actionAdd_Employee_2")
        self.actionSettings = QtWidgets.QAction(oneOnOneMain)
        self.actionSettings.setObjectName("actionSettings")
        self.actionManager_Review = QtWidgets.QAction(oneOnOneMain)
        self.actionManager_Review.setObjectName("actionManager_Review")
        self.actionEmployee_Review = QtWidgets.QAction(oneOnOneMain)
        self.actionEmployee_Review.setObjectName("actionEmployee_Review")
        self.actionDistribution_Lists = QtWidgets.QAction(oneOnOneMain)
        self.actionDistribution_Lists.setObjectName("actionDistribution_Lists")

        self.retranslateUi(oneOnOneMain)
        QtCore.QMetaObject.connectSlotsByName(oneOnOneMain)

    def retranslateUi(self, oneOnOneMain):
        _translate = QtCore.QCoreApplication.translate
        oneOnOneMain.setWindowTitle(_translate("oneOnOneMain", "One On One Tracker"))
        self.managerCombo.setItemText(0, _translate("oneOnOneMain", "All"))
        self.label.setText(_translate("oneOnOneMain", "Manager Select"))
        self.label_3.setText(_translate("oneOnOneMain", "Double Click user to see additional details."))
        self.actionUpdate_Employee.setText(_translate("oneOnOneMain", "&Update Employee"))
        self.actionRun_Desk_Goal_Update.setText(_translate("oneOnOneMain", "&Run CDS Desk Update"))
        self.actionAdd_Employee.setText(_translate("oneOnOneMain", "&Add Employee"))
        self.actionTrending_Graphs.setText(_translate("oneOnOneMain", "Trending Graphs"))
        self.actionAdd_Employee_2.setText(_translate("oneOnOneMain", "Add Employee"))
        self.actionSettings.setText(_translate("oneOnOneMain", "Settings"))
        self.actionManager_Review.setText(_translate("oneOnOneMain", "Add Review"))
        self.actionEmployee_Review.setText(_translate("oneOnOneMain", "Employee Reviews"))
        self.actionDistribution_Lists.setText(_translate("oneOnOneMain", "Distribution Lists"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    oneOnOneMain = QtWidgets.QMainWindow()
    ui = Ui_oneOnOneMain()
    ui.setupUi(oneOnOneMain)
    oneOnOneMain.show()
    sys.exit(app.exec_())
