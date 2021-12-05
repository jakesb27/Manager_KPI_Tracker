# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Files\agent_graphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_agentGraphsMain(object):
    def setupUi(self, agentGraphsMain):
        agentGraphsMain.setObjectName("agentGraphsMain")
        agentGraphsMain.resize(971, 656)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        agentGraphsMain.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(agentGraphsMain)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(agentGraphsMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("image: url(:/logos/Images/Meduit Email.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.557, y1:0, x2:0.511, y2:1, stop:0.528409 rgba(255, 255, 255, 174));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(agentGraphsMain)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0.557, y1:0, x2:0.511, y2:1, stop:0.528409 rgba(255, 255, 255, 174));\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex;\n"
"    padding-top: 0;\n"
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
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.managerCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.managerCombo.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.managerCombo.setObjectName("managerCombo")
        self.managerCombo.addItem("")
        self.gridLayout_4.addWidget(self.managerCombo, 0, 2, 1, 2)
        self.employeeSelect = QtWidgets.QComboBox(self.groupBox_2)
        self.employeeSelect.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.employeeSelect.setObjectName("employeeSelect")
        self.gridLayout_4.addWidget(self.employeeSelect, 1, 2, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(agentGraphsMain)
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.557, y1:0, x2:0.511, y2:1, stop:0.528409 rgba(255, 255, 255, 174));\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"}")
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.graphData4 = QtWidgets.QComboBox(self.frame)
        self.graphData4.setObjectName("graphData4")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.graphData4.addItem("")
        self.horizontalLayout_4.addWidget(self.graphData4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.graphBox1 = QtWidgets.QWidget(self.frame)
        self.graphBox1.setObjectName("graphBox1")
        self.gridLayout.addWidget(self.graphBox1, 2, 0, 1, 1)
        self.graphBox2 = QtWidgets.QWidget(self.frame)
        self.graphBox2.setObjectName("graphBox2")
        self.gridLayout.addWidget(self.graphBox2, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.graphData2 = QtWidgets.QComboBox(self.frame)
        self.graphData2.setObjectName("graphData2")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.graphData2.addItem("")
        self.horizontalLayout_2.addWidget(self.graphData2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.graphData1 = QtWidgets.QComboBox(self.frame)
        self.graphData1.setObjectName("graphData1")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.graphData1.addItem("")
        self.horizontalLayout.addWidget(self.graphData1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("QFrame{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: 0px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.graphData3 = QtWidgets.QComboBox(self.frame)
        self.graphData3.setObjectName("graphData3")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.graphData3.addItem("")
        self.horizontalLayout_3.addWidget(self.graphData3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.graphBox3 = QtWidgets.QWidget(self.frame)
        self.graphBox3.setObjectName("graphBox3")
        self.gridLayout.addWidget(self.graphBox3, 4, 0, 1, 1)
        self.graphBox4 = QtWidgets.QWidget(self.frame)
        self.graphBox4.setObjectName("graphBox4")
        self.gridLayout.addWidget(self.graphBox4, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 4)

        self.retranslateUi(agentGraphsMain)
        self.graphData4.setCurrentIndex(-1)
        self.graphData2.setCurrentIndex(-1)
        self.graphData1.setCurrentIndex(-1)
        self.graphData3.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(agentGraphsMain)
        agentGraphsMain.setTabOrder(self.managerCombo, self.employeeSelect)
        agentGraphsMain.setTabOrder(self.employeeSelect, self.graphData1)
        agentGraphsMain.setTabOrder(self.graphData1, self.graphData2)
        agentGraphsMain.setTabOrder(self.graphData2, self.graphData3)
        agentGraphsMain.setTabOrder(self.graphData3, self.graphData4)

    def retranslateUi(self, agentGraphsMain):
        _translate = QtCore.QCoreApplication.translate
        agentGraphsMain.setWindowTitle(_translate("agentGraphsMain", "Agent Trending Graphs"))
        self.label_6.setText(_translate("agentGraphsMain", "Manager Filter:"))
        self.managerCombo.setItemText(0, _translate("agentGraphsMain", "All"))
        self.label_20.setText(_translate("agentGraphsMain", "Employee Select:"))
        self.label_5.setText(_translate("agentGraphsMain", "Select Graph Data:  "))
        self.graphData4.setItemText(0, _translate("agentGraphsMain", "Monthly - RPC\'s"))
        self.graphData4.setItemText(1, _translate("agentGraphsMain", "Monthly - RPC\'s Per Hour"))
        self.graphData4.setItemText(2, _translate("agentGraphsMain", "Monthly - Connects"))
        self.graphData4.setItemText(3, _translate("agentGraphsMain", "Monthly - Connects Per Hour"))
        self.graphData4.setItemText(4, _translate("agentGraphsMain", "Monthly - Conversions"))
        self.graphData4.setItemText(5, _translate("agentGraphsMain", "Monthly - Fees"))
        self.graphData4.setItemText(6, _translate("agentGraphsMain", "Monthly - Totals"))
        self.graphData4.setItemText(7, _translate("agentGraphsMain", "Weekly - RPC\'s"))
        self.graphData4.setItemText(8, _translate("agentGraphsMain", "Weekly - RPC\'s Per Hour"))
        self.graphData4.setItemText(9, _translate("agentGraphsMain", "Weekly - Connects"))
        self.graphData4.setItemText(10, _translate("agentGraphsMain", "Weekly - Connects Per Hour"))
        self.graphData4.setItemText(11, _translate("agentGraphsMain", "Weekly - Conversions"))
        self.graphData4.setItemText(12, _translate("agentGraphsMain", "Weekly - Fees"))
        self.label_3.setText(_translate("agentGraphsMain", "Select Graph Data:  "))
        self.graphData2.setItemText(0, _translate("agentGraphsMain", "Monthly - RPC\'s"))
        self.graphData2.setItemText(1, _translate("agentGraphsMain", "Monthly - RPC\'s Per Hour"))
        self.graphData2.setItemText(2, _translate("agentGraphsMain", "Monthly - Connects"))
        self.graphData2.setItemText(3, _translate("agentGraphsMain", "Monthly - Connects Per Hour"))
        self.graphData2.setItemText(4, _translate("agentGraphsMain", "Monthly - Conversions"))
        self.graphData2.setItemText(5, _translate("agentGraphsMain", "Monthly - Fees"))
        self.graphData2.setItemText(6, _translate("agentGraphsMain", "Monthly - Totals"))
        self.graphData2.setItemText(7, _translate("agentGraphsMain", "Weekly - RPC\'s"))
        self.graphData2.setItemText(8, _translate("agentGraphsMain", "Weekly - RPC\'s Per Hour"))
        self.graphData2.setItemText(9, _translate("agentGraphsMain", "Weekly - Connects"))
        self.graphData2.setItemText(10, _translate("agentGraphsMain", "Weekly - Connects Per Hour"))
        self.graphData2.setItemText(11, _translate("agentGraphsMain", "Weekly - Conversions"))
        self.graphData2.setItemText(12, _translate("agentGraphsMain", "Weekly - Fees"))
        self.label_2.setText(_translate("agentGraphsMain", "Select Graph Data:  "))
        self.graphData1.setItemText(0, _translate("agentGraphsMain", "Monthly - RPC\'s"))
        self.graphData1.setItemText(1, _translate("agentGraphsMain", "Monthly - RPC\'s Per Hour"))
        self.graphData1.setItemText(2, _translate("agentGraphsMain", "Monthly - Connects"))
        self.graphData1.setItemText(3, _translate("agentGraphsMain", "Monthly - Connects Per Hour"))
        self.graphData1.setItemText(4, _translate("agentGraphsMain", "Monthly - Conversions"))
        self.graphData1.setItemText(5, _translate("agentGraphsMain", "Monthly - Fees"))
        self.graphData1.setItemText(6, _translate("agentGraphsMain", "Monthly - Totals"))
        self.graphData1.setItemText(7, _translate("agentGraphsMain", "Weekly - RPC\'s"))
        self.graphData1.setItemText(8, _translate("agentGraphsMain", "Weekly - RPC\'s Per Hour"))
        self.graphData1.setItemText(9, _translate("agentGraphsMain", "Weekly - Connects"))
        self.graphData1.setItemText(10, _translate("agentGraphsMain", "Weekly - Connects Per Hour"))
        self.graphData1.setItemText(11, _translate("agentGraphsMain", "Weekly - Conversions"))
        self.graphData1.setItemText(12, _translate("agentGraphsMain", "Weekly - Fees"))
        self.label_4.setText(_translate("agentGraphsMain", "Select Graph Data:  "))
        self.graphData3.setItemText(0, _translate("agentGraphsMain", "Monthly - RPC\'s"))
        self.graphData3.setItemText(1, _translate("agentGraphsMain", "Monthly - RPC\'s Per Hour"))
        self.graphData3.setItemText(2, _translate("agentGraphsMain", "Monthly - Connects"))
        self.graphData3.setItemText(3, _translate("agentGraphsMain", "Monthly - Connects Per Hour"))
        self.graphData3.setItemText(4, _translate("agentGraphsMain", "Monthly - Conversions"))
        self.graphData3.setItemText(5, _translate("agentGraphsMain", "Monthly - Fees"))
        self.graphData3.setItemText(6, _translate("agentGraphsMain", "Monthly - Totals"))
        self.graphData3.setItemText(7, _translate("agentGraphsMain", "Weekly - RPC\'s"))
        self.graphData3.setItemText(8, _translate("agentGraphsMain", "Weekly - RPC\'s Per Hour"))
        self.graphData3.setItemText(9, _translate("agentGraphsMain", "Weekly - Connects"))
        self.graphData3.setItemText(10, _translate("agentGraphsMain", "Weekly - Connects Per Hour"))
        self.graphData3.setItemText(11, _translate("agentGraphsMain", "Weekly - Conversions"))
        self.graphData3.setItemText(12, _translate("agentGraphsMain", "Weekly - Fees"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    agentGraphsMain = QtWidgets.QDialog()
    ui = Ui_agentGraphsMain()
    ui.setupUi(agentGraphsMain)
    agentGraphsMain.show()
    sys.exit(app.exec_())
