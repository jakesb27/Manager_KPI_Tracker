# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_managerMain(object):
    def setupUi(self, managerMain):
        managerMain.setObjectName("managerMain")
        managerMain.resize(718, 423)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        managerMain.setWindowIcon(icon)
        managerMain.setStyleSheet("QMainWindow{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));\n"
"}\n"
"QWidget{\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
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
"    background-color: rgb(195, 195, 195);\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"    padding: 2 10px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    font: 11pt \"Corbel\";\n"
"    font-weight: bold;\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgb(223, 223, 223);\n"
"    border: 1px solid black;\n"
"    font: 11pt \"Corbel\";\n"
"}\n"
"QTextEdit{\n"
"    font: 30pt \"Corbel\";\n"
"}\n"
"QStatusBar{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableView{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(managerMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 93))
        self.label_2.setMaximumSize(QtCore.QSize(200, 93))
        self.label_2.setStyleSheet("image: url(:/images/Meduit Email.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.agentTableView = QtWidgets.QTableView(self.centralwidget)
        self.agentTableView.setMinimumSize(QtCore.QSize(700, 0))
        self.agentTableView.setAlternatingRowColors(True)
        self.agentTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.agentTableView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.agentTableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.agentTableView.setSortingEnabled(True)
        self.agentTableView.setObjectName("agentTableView")
        self.gridLayout.addWidget(self.agentTableView, 5, 0, 1, 6)
        self.managerCombo = QtWidgets.QComboBox(self.centralwidget)
        self.managerCombo.setObjectName("managerCombo")
        self.managerCombo.addItem("")
        self.managerCombo.addItem("")
        self.managerCombo.addItem("")
        self.managerCombo.addItem("")
        self.managerCombo.addItem("")
        self.gridLayout.addWidget(self.managerCombo, 2, 1, 1, 1)
        self.managerRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.managerRefresh.setObjectName("managerRefresh")
        self.gridLayout.addWidget(self.managerRefresh, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 3)
        managerMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(managerMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        managerMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(managerMain)
        self.statusbar.setObjectName("statusbar")
        managerMain.setStatusBar(self.statusbar)
        self.actionEmployee_Maintenance = QtWidgets.QAction(managerMain)
        self.actionEmployee_Maintenance.setObjectName("actionEmployee_Maintenance")
        self.menuFile.addAction(self.actionEmployee_Maintenance)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(managerMain)
        QtCore.QMetaObject.connectSlotsByName(managerMain)

    def retranslateUi(self, managerMain):
        _translate = QtCore.QCoreApplication.translate
        managerMain.setWindowTitle(_translate("managerMain", "Manager KPI Tracker"))
        self.label.setText(_translate("managerMain", "Manager Select"))
        self.managerCombo.setItemText(0, _translate("managerMain", "All"))
        self.managerCombo.setItemText(1, _translate("managerMain", "Patty"))
        self.managerCombo.setItemText(2, _translate("managerMain", "Robert"))
        self.managerCombo.setItemText(3, _translate("managerMain", "Shana"))
        self.managerCombo.setItemText(4, _translate("managerMain", "Stephanie"))
        self.managerRefresh.setText(_translate("managerMain", "Refresh"))
        self.label_3.setText(_translate("managerMain", "Double Click user to see additional details."))
        self.menuFile.setTitle(_translate("managerMain", "File"))
        self.actionEmployee_Maintenance.setText(_translate("managerMain", "Employee Maintenance"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    managerMain = QtWidgets.QMainWindow()
    ui = Ui_managerMain()
    ui.setupUi(managerMain)
    managerMain.show()
    sys.exit(app.exec_())
