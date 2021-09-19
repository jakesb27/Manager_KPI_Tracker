# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agent_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_agentDetailsMain(object):
    def setupUi(self, agentDetailsMain):
        agentDetailsMain.setObjectName("agentDetailsMain")
        agentDetailsMain.resize(714, 329)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        agentDetailsMain.setWindowIcon(icon)
        agentDetailsMain.setStyleSheet("QDialog{\n"
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
"    image: url(:/meduit/arrow.png);\n"
"    width: 14 px;\n"
"    height:14 px;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(agentDetailsMain)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(agentDetailsMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.employeeSelect = QtWidgets.QComboBox(self.groupBox_2)
        self.employeeSelect.setObjectName("employeeSelect")
        self.gridLayout_4.addWidget(self.employeeSelect, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)
        self.employeeMisc = QtWidgets.QTextBrowser(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeMisc.sizePolicy().hasHeightForWidth())
        self.employeeMisc.setSizePolicy(sizePolicy)
        self.employeeMisc.setMaximumSize(QtCore.QSize(16777215, 71))
        self.employeeMisc.setOpenExternalLinks(True)
        self.employeeMisc.setObjectName("employeeMisc")
        self.gridLayout_4.addWidget(self.employeeMisc, 1, 1, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(agentDetailsMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.agentBase1 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase1.sizePolicy().hasHeightForWidth())
        self.agentBase1.setSizePolicy(sizePolicy)
        self.agentBase1.setReadOnly(True)
        self.agentBase1.setObjectName("agentBase1")
        self.gridLayout_3.addWidget(self.agentBase1, 3, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 5, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.agentDesc3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDesc3.sizePolicy().hasHeightForWidth())
        self.agentDesc3.setSizePolicy(sizePolicy)
        self.agentDesc3.setReadOnly(True)
        self.agentDesc3.setObjectName("agentDesc3")
        self.gridLayout_3.addWidget(self.agentDesc3, 5, 1, 1, 2)
        self.agentGoal1 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal1.sizePolicy().hasHeightForWidth())
        self.agentGoal1.setSizePolicy(sizePolicy)
        self.agentGoal1.setReadOnly(True)
        self.agentGoal1.setObjectName("agentGoal1")
        self.gridLayout_3.addWidget(self.agentGoal1, 3, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 3, 3, 1, 1)
        self.agentGoal3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal3.sizePolicy().hasHeightForWidth())
        self.agentGoal3.setSizePolicy(sizePolicy)
        self.agentGoal3.setReadOnly(True)
        self.agentGoal3.setObjectName("agentGoal3")
        self.gridLayout_3.addWidget(self.agentGoal3, 5, 6, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 5, 1, 1)
        self.agentGoal2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal2.sizePolicy().hasHeightForWidth())
        self.agentGoal2.setSizePolicy(sizePolicy)
        self.agentGoal2.setReadOnly(True)
        self.agentGoal2.setObjectName("agentGoal2")
        self.gridLayout_3.addWidget(self.agentGoal2, 4, 6, 1, 1)
        self.agentBase3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase3.sizePolicy().hasHeightForWidth())
        self.agentBase3.setSizePolicy(sizePolicy)
        self.agentBase3.setReadOnly(True)
        self.agentBase3.setObjectName("agentBase3")
        self.gridLayout_3.addWidget(self.agentBase3, 5, 4, 1, 1)
        self.agentConv = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentConv.sizePolicy().hasHeightForWidth())
        self.agentConv.setSizePolicy(sizePolicy)
        self.agentConv.setReadOnly(True)
        self.agentConv.setObjectName("agentConv")
        self.gridLayout_3.addWidget(self.agentConv, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 4, 5, 1, 1)
        self.agentDesc1 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDesc1.sizePolicy().hasHeightForWidth())
        self.agentDesc1.setSizePolicy(sizePolicy)
        self.agentDesc1.setReadOnly(True)
        self.agentDesc1.setObjectName("agentDesc1")
        self.gridLayout_3.addWidget(self.agentDesc1, 3, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)
        self.agentDesc2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDesc2.sizePolicy().hasHeightForWidth())
        self.agentDesc2.setSizePolicy(sizePolicy)
        self.agentDesc2.setReadOnly(True)
        self.agentDesc2.setObjectName("agentDesc2")
        self.gridLayout_3.addWidget(self.agentDesc2, 4, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.agentBase2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase2.sizePolicy().hasHeightForWidth())
        self.agentBase2.setSizePolicy(sizePolicy)
        self.agentBase2.setReadOnly(True)
        self.agentBase2.setObjectName("agentBase2")
        self.gridLayout_3.addWidget(self.agentBase2, 4, 4, 1, 1)
        self.agentRPC = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentRPC.sizePolicy().hasHeightForWidth())
        self.agentRPC.setSizePolicy(sizePolicy)
        self.agentRPC.setReadOnly(True)
        self.agentRPC.setObjectName("agentRPC")
        self.gridLayout_3.addWidget(self.agentRPC, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 2, 7)
        self.employeeGraphs = QtWidgets.QPushButton(self.groupBox)
        self.employeeGraphs.setObjectName("employeeGraphs")
        self.gridLayout_3.addWidget(self.employeeGraphs, 0, 5, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)
        self.agentDetails = QtWidgets.QGroupBox(agentDetailsMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDetails.sizePolicy().hasHeightForWidth())
        self.agentDetails.setSizePolicy(sizePolicy)
        self.agentDetails.setObjectName("agentDetails")
        self.gridLayout = QtWidgets.QGridLayout(self.agentDetails)
        self.gridLayout.setObjectName("gridLayout")
        self.agentDesk = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDesk.sizePolicy().hasHeightForWidth())
        self.agentDesk.setSizePolicy(sizePolicy)
        self.agentDesk.setReadOnly(True)
        self.agentDesk.setObjectName("agentDesk")
        self.gridLayout.addWidget(self.agentDesk, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.agentExt = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentExt.sizePolicy().hasHeightForWidth())
        self.agentExt.setSizePolicy(sizePolicy)
        self.agentExt.setReadOnly(True)
        self.agentExt.setObjectName("agentExt")
        self.gridLayout.addWidget(self.agentExt, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.agentName = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentName.sizePolicy().hasHeightForWidth())
        self.agentName.setSizePolicy(sizePolicy)
        self.agentName.setReadOnly(True)
        self.agentName.setObjectName("agentName")
        self.gridLayout.addWidget(self.agentName, 0, 1, 1, 1)
        self.agentTotal = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentTotal.sizePolicy().hasHeightForWidth())
        self.agentTotal.setSizePolicy(sizePolicy)
        self.agentTotal.setReadOnly(True)
        self.agentTotal.setObjectName("agentTotal")
        self.gridLayout.addWidget(self.agentTotal, 3, 4, 1, 1)
        self.agentPrinc = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentPrinc.sizePolicy().hasHeightForWidth())
        self.agentPrinc.setSizePolicy(sizePolicy)
        self.agentPrinc.setReadOnly(True)
        self.agentPrinc.setObjectName("agentPrinc")
        self.gridLayout.addWidget(self.agentPrinc, 0, 4, 1, 1)
        self.agentInt = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentInt.sizePolicy().hasHeightForWidth())
        self.agentInt.setSizePolicy(sizePolicy)
        self.agentInt.setReadOnly(True)
        self.agentInt.setObjectName("agentInt")
        self.gridLayout.addWidget(self.agentInt, 2, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.agentComm = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentComm.sizePolicy().hasHeightForWidth())
        self.agentComm.setSizePolicy(sizePolicy)
        self.agentComm.setReadOnly(True)
        self.agentComm.setObjectName("agentComm")
        self.gridLayout.addWidget(self.agentComm, 4, 4, 1, 1)
        self.agentGoal = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal.sizePolicy().hasHeightForWidth())
        self.agentGoal.setSizePolicy(sizePolicy)
        self.agentGoal.setReadOnly(True)
        self.agentGoal.setObjectName("agentGoal")
        self.gridLayout.addWidget(self.agentGoal, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.agentDetails, 0, 1, 1, 1)

        self.retranslateUi(agentDetailsMain)
        QtCore.QMetaObject.connectSlotsByName(agentDetailsMain)

    def retranslateUi(self, agentDetailsMain):
        _translate = QtCore.QCoreApplication.translate
        agentDetailsMain.setWindowTitle(_translate("agentDetailsMain", "Agent Details"))
        self.label_20.setText(_translate("agentDetailsMain", "Employee Select:"))
        self.employeeMisc.setHtml(_translate("agentDetailsMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Corbel\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("agentDetailsMain", "KPI Goals"))
        self.label_14.setText(_translate("agentDetailsMain", "Base Value:"))
        self.label_16.setText(_translate("agentDetailsMain", "Base Value:"))
        self.label_19.setText(_translate("agentDetailsMain", "Goal:"))
        self.label_9.setText(_translate("agentDetailsMain", "Current RPC:"))
        self.label_11.setText(_translate("agentDetailsMain", "Productivity Goal 1:"))
        self.label_15.setText(_translate("agentDetailsMain", "Base Value:"))
        self.label_17.setText(_translate("agentDetailsMain", "Goal:"))
        self.label_10.setText(_translate("agentDetailsMain", "Current Conv:"))
        self.label_18.setText(_translate("agentDetailsMain", "Goal:"))
        self.label_13.setText(_translate("agentDetailsMain", "Productivity Goal 3:"))
        self.label_12.setText(_translate("agentDetailsMain", "Productivity Goal 2:"))
        self.employeeGraphs.setText(_translate("agentDetailsMain", "Trending Graphs"))
        self.agentDetails.setTitle(_translate("agentDetailsMain", "Agent Information"))
        self.label_7.setText(_translate("agentDetailsMain", "MTD Commission:"))
        self.label_6.setText(_translate("agentDetailsMain", "MTD Total:"))
        self.label.setText(_translate("agentDetailsMain", "Name:"))
        self.label_8.setText(_translate("agentDetailsMain", "Ext:"))
        self.label_4.setText(_translate("agentDetailsMain", "MTD Principal:"))
        self.label_5.setText(_translate("agentDetailsMain", "MTD Interest:"))
        self.label_2.setText(_translate("agentDetailsMain", "Desk:"))
        self.label_3.setText(_translate("agentDetailsMain", "Goal:"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    agentDetailsMain = QtWidgets.QDialog()
    ui = Ui_agentDetailsMain()
    ui.setupUi(agentDetailsMain)
    agentDetailsMain.show()
    sys.exit(app.exec_())
