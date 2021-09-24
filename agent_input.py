# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agent_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_agentInput(object):
    def setupUi(self, agentInput):
        agentInput.setObjectName("agentInput")
        agentInput.resize(735, 413)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        agentInput.setWindowIcon(icon)
        agentInput.setStyleSheet("QDialog{\n"
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
"    border: 1px solid rgb(75, 124, 154);;\n"
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
"    image: url(:/meduit/arrow-dwn.png);\n"
"    width: 14 px;\n"
"    height:14 px;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(agentInput)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addButton = QtWidgets.QPushButton(agentInput)
        self.addButton.setMinimumSize(QtCore.QSize(125, 0))
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout_2.addWidget(self.addButton, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 4, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(agentInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("QLabel{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 6)
        self.agentBase1 = QtWidgets.QLineEdit(self.groupBox)
        self.agentBase1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase1.sizePolicy().hasHeightForWidth())
        self.agentBase1.setSizePolicy(sizePolicy)
        self.agentBase1.setObjectName("agentBase1")
        self.gridLayout_3.addWidget(self.agentBase1, 1, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)
        self.agentGoal3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal3.sizePolicy().hasHeightForWidth())
        self.agentGoal3.setSizePolicy(sizePolicy)
        self.agentGoal3.setObjectName("agentGoal3")
        self.gridLayout_3.addWidget(self.agentGoal3, 3, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.agentGoal1 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal1.sizePolicy().hasHeightForWidth())
        self.agentGoal1.setSizePolicy(sizePolicy)
        self.agentGoal1.setObjectName("agentGoal1")
        self.gridLayout_3.addWidget(self.agentGoal1, 1, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.agentDesc3 = QtWidgets.QComboBox(self.groupBox)
        self.agentDesc3.setMinimumSize(QtCore.QSize(200, 0))
        self.agentDesc3.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.agentDesc3.setObjectName("agentDesc3")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.agentDesc3.addItem("")
        self.gridLayout_3.addWidget(self.agentDesc3, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 4, 1, 1)
        self.agentBase3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase3.sizePolicy().hasHeightForWidth())
        self.agentBase3.setSizePolicy(sizePolicy)
        self.agentBase3.setObjectName("agentBase3")
        self.gridLayout_3.addWidget(self.agentBase3, 3, 3, 1, 1)
        self.agentGoal2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal2.sizePolicy().hasHeightForWidth())
        self.agentGoal2.setSizePolicy(sizePolicy)
        self.agentGoal2.setObjectName("agentGoal2")
        self.gridLayout_3.addWidget(self.agentGoal2, 2, 5, 1, 1)
        self.agentDesc1 = QtWidgets.QComboBox(self.groupBox)
        self.agentDesc1.setMinimumSize(QtCore.QSize(200, 0))
        self.agentDesc1.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.agentDesc1.setObjectName("agentDesc1")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.agentDesc1.addItem("")
        self.gridLayout_3.addWidget(self.agentDesc1, 1, 1, 1, 1)
        self.agentBase2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase2.sizePolicy().hasHeightForWidth())
        self.agentBase2.setSizePolicy(sizePolicy)
        self.agentBase2.setObjectName("agentBase2")
        self.gridLayout_3.addWidget(self.agentBase2, 2, 3, 1, 1)
        self.agentDesc2 = QtWidgets.QComboBox(self.groupBox)
        self.agentDesc2.setMinimumSize(QtCore.QSize(200, 0))
        self.agentDesc2.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.agentDesc2.setObjectName("agentDesc2")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.agentDesc2.addItem("")
        self.gridLayout_3.addWidget(self.agentDesc2, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 1, 1, 7)
        self.agentDetails = QtWidgets.QGroupBox(agentInput)
        self.agentDetails.setObjectName("agentDetails")
        self.gridLayout = QtWidgets.QGridLayout(self.agentDetails)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.agentDetails)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.agentUltiPro = QtWidgets.QLineEdit(self.agentDetails)
        self.agentUltiPro.setObjectName("agentUltiPro")
        self.gridLayout.addWidget(self.agentUltiPro, 0, 1, 1, 1)
        self.agentLastName = QtWidgets.QLineEdit(self.agentDetails)
        self.agentLastName.setObjectName("agentLastName")
        self.gridLayout.addWidget(self.agentLastName, 2, 1, 1, 4)
        self.agentUserID = QtWidgets.QLineEdit(self.agentDetails)
        self.agentUserID.setObjectName("agentUserID")
        self.gridLayout.addWidget(self.agentUserID, 1, 5, 1, 1)
        self.agentGroup = QtWidgets.QLineEdit(self.agentDetails)
        self.agentGroup.setObjectName("agentGroup")
        self.gridLayout.addWidget(self.agentGroup, 2, 6, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.agentDetails)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.agentDetails)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.agentDetails)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.agentManager = QtWidgets.QComboBox(self.agentDetails)
        self.agentManager.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.agentManager.setObjectName("agentManager")
        self.agentManager.addItem("")
        self.gridLayout.addWidget(self.agentManager, 4, 1, 1, 6)
        self.agentFirstName = QtWidgets.QLineEdit(self.agentDetails)
        self.agentFirstName.setObjectName("agentFirstName")
        self.gridLayout.addWidget(self.agentFirstName, 1, 1, 1, 3)
        self.label_20 = QtWidgets.QLabel(self.agentDetails)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.agentDetails)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.agentExt = QtWidgets.QLineEdit(self.agentDetails)
        self.agentExt.setObjectName("agentExt")
        self.gridLayout.addWidget(self.agentExt, 1, 8, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.agentDetails)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 5, 1, 1)
        self.agentEmail = QtWidgets.QLineEdit(self.agentDetails)
        self.agentEmail.setObjectName("agentEmail")
        self.gridLayout.addWidget(self.agentEmail, 0, 4, 1, 5)
        self.label_8 = QtWidgets.QLabel(self.agentDetails)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.agentDetails)
        self.label_10.setStyleSheet("QLabel{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 9)
        self.gridLayout_2.addWidget(self.agentDetails, 1, 2, 1, 5)
        self.clearButton = QtWidgets.QPushButton(agentInput)
        self.clearButton.setMinimumSize(QtCore.QSize(125, 0))
        self.clearButton.setAutoDefault(False)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 3, 3, 1, 1)
        self.closeButton = QtWidgets.QPushButton(agentInput)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 3, 6, 1, 1)

        self.retranslateUi(agentInput)
        self.closeButton.clicked.connect(agentInput.close)
        QtCore.QMetaObject.connectSlotsByName(agentInput)
        agentInput.setTabOrder(self.agentUltiPro, self.agentEmail)
        agentInput.setTabOrder(self.agentEmail, self.agentFirstName)
        agentInput.setTabOrder(self.agentFirstName, self.agentUserID)
        agentInput.setTabOrder(self.agentUserID, self.agentExt)
        agentInput.setTabOrder(self.agentExt, self.agentLastName)
        agentInput.setTabOrder(self.agentLastName, self.agentGroup)
        agentInput.setTabOrder(self.agentGroup, self.agentManager)
        agentInput.setTabOrder(self.agentManager, self.agentDesc1)
        agentInput.setTabOrder(self.agentDesc1, self.agentBase1)
        agentInput.setTabOrder(self.agentBase1, self.agentGoal1)
        agentInput.setTabOrder(self.agentGoal1, self.agentDesc2)
        agentInput.setTabOrder(self.agentDesc2, self.agentBase2)
        agentInput.setTabOrder(self.agentBase2, self.agentGoal2)
        agentInput.setTabOrder(self.agentGoal2, self.agentDesc3)
        agentInput.setTabOrder(self.agentDesc3, self.agentBase3)
        agentInput.setTabOrder(self.agentBase3, self.agentGoal3)
        agentInput.setTabOrder(self.agentGoal3, self.addButton)
        agentInput.setTabOrder(self.addButton, self.clearButton)
        agentInput.setTabOrder(self.clearButton, self.closeButton)

    def retranslateUi(self, agentInput):
        _translate = QtCore.QCoreApplication.translate
        agentInput.setWindowTitle(_translate("agentInput", "Add Employee"))
        self.addButton.setText(_translate("agentInput", "&Add Employee"))
        self.groupBox.setTitle(_translate("agentInput", "KPI Goals"))
        self.label_4.setText(_translate("agentInput", "*Please note that all percentages must be input as a whole number and should not contain the \"%\" symbol. For example 20% should be input as \"20\" and not \".20\", \"0.20\". Monetary values should not contain a comma seperator or the \"$\" symbol. For example $1,654.23 should be input as \"1654.23\"."))
        self.label_15.setText(_translate("agentInput", "Base Value*:"))
        self.label_17.setText(_translate("agentInput", "Goal*:"))
        self.label_14.setText(_translate("agentInput", "Base Value*:"))
        self.label_13.setText(_translate("agentInput", "Productivity Goal 3:"))
        self.label_19.setText(_translate("agentInput", "Goal*:"))
        self.label_16.setText(_translate("agentInput", "Base Value*:"))
        self.label_11.setText(_translate("agentInput", "Productivity Goal 1:"))
        self.label_12.setText(_translate("agentInput", "Productivity Goal 2:"))
        self.agentDesc3.setItemText(0, _translate("agentInput", " - Select A Goal - "))
        self.agentDesc3.setItemText(1, _translate("agentInput", "Connects (Total)"))
        self.agentDesc3.setItemText(2, _translate("agentInput", "Connects (Per Hour)"))
        self.agentDesc3.setItemText(3, _translate("agentInput", "RPC (Total)"))
        self.agentDesc3.setItemText(4, _translate("agentInput", "RPC (Per Hour)"))
        self.agentDesc3.setItemText(5, _translate("agentInput", "Promises Conv%"))
        self.agentDesc3.setItemText(6, _translate("agentInput", "Conversions Per Hour"))
        self.agentDesc3.setItemText(7, _translate("agentInput", "Secured (%)"))
        self.agentDesc3.setItemText(8, _translate("agentInput", "Secured (Avg Payment)"))
        self.agentDesc3.setItemText(9, _translate("agentInput", "Fees (Total)"))
        self.agentDesc3.setItemText(10, _translate("agentInput", "Fees (Per Hour)"))
        self.agentDesc3.setItemText(11, _translate("agentInput", "Overall Totals"))
        self.agentDesc3.setItemText(12, _translate("agentInput", "Payment Plan"))
        self.agentDesc3.setItemText(13, _translate("agentInput", "Category Review"))
        self.label_18.setText(_translate("agentInput", "Goal*:"))
        self.agentDesc1.setItemText(0, _translate("agentInput", " - Select A Goal - "))
        self.agentDesc1.setItemText(1, _translate("agentInput", "Connects (Total)"))
        self.agentDesc1.setItemText(2, _translate("agentInput", "Connects (Per Hour)"))
        self.agentDesc1.setItemText(3, _translate("agentInput", "RPC (Total)"))
        self.agentDesc1.setItemText(4, _translate("agentInput", "RPC (Per Hour)"))
        self.agentDesc1.setItemText(5, _translate("agentInput", "Promises Conv%"))
        self.agentDesc1.setItemText(6, _translate("agentInput", "Conversions Per Hour"))
        self.agentDesc1.setItemText(7, _translate("agentInput", "Secured (%)"))
        self.agentDesc1.setItemText(8, _translate("agentInput", "Secured (Avg Payment)"))
        self.agentDesc1.setItemText(9, _translate("agentInput", "Fees (Total)"))
        self.agentDesc1.setItemText(10, _translate("agentInput", "Fees (Per Hour)"))
        self.agentDesc1.setItemText(11, _translate("agentInput", "Overall Totals"))
        self.agentDesc1.setItemText(12, _translate("agentInput", "Payment Plan"))
        self.agentDesc1.setItemText(13, _translate("agentInput", "Category Review"))
        self.agentDesc2.setItemText(0, _translate("agentInput", " - Select A Goal - "))
        self.agentDesc2.setItemText(1, _translate("agentInput", "Connects (Total)"))
        self.agentDesc2.setItemText(2, _translate("agentInput", "Connects (Per Hour)"))
        self.agentDesc2.setItemText(3, _translate("agentInput", "RPC (Total)"))
        self.agentDesc2.setItemText(4, _translate("agentInput", "RPC (Per Hour)"))
        self.agentDesc2.setItemText(5, _translate("agentInput", "Promises Conv%"))
        self.agentDesc2.setItemText(6, _translate("agentInput", "Conversions Per Hour"))
        self.agentDesc2.setItemText(7, _translate("agentInput", "Secured (%)"))
        self.agentDesc2.setItemText(8, _translate("agentInput", "Secured (Avg Payment)"))
        self.agentDesc2.setItemText(9, _translate("agentInput", "Fees (Total)"))
        self.agentDesc2.setItemText(10, _translate("agentInput", "Fees (Per Hour)"))
        self.agentDesc2.setItemText(11, _translate("agentInput", "Overall Totals"))
        self.agentDesc2.setItemText(12, _translate("agentInput", "Payment Plan"))
        self.agentDesc2.setItemText(13, _translate("agentInput", "Category Review"))
        self.agentDetails.setTitle(_translate("agentInput", "New Agent Information"))
        self.label_7.setText(_translate("agentInput", "Last Name *"))
        self.agentUltiPro.setPlaceholderText(_translate("agentInput", "000000"))
        self.agentLastName.setPlaceholderText(_translate("agentInput", "Smith"))
        self.agentUserID.setPlaceholderText(_translate("agentInput", "JOS"))
        self.agentGroup.setPlaceholderText(_translate("agentInput", "Phone"))
        self.label_6.setText(_translate("agentInput", "Email"))
        self.label_9.setText(_translate("agentInput", "Manager"))
        self.label.setText(_translate("agentInput", "First Name *"))
        self.agentManager.setItemText(0, _translate("agentInput", " - Select A Manager - "))
        self.agentFirstName.setPlaceholderText(_translate("agentInput", "John"))
        self.label_20.setText(_translate("agentInput", "User ID *"))
        self.label_2.setText(_translate("agentInput", "UltiPro ID *"))
        self.agentExt.setPlaceholderText(_translate("agentInput", "123"))
        self.label_5.setText(_translate("agentInput", "Group:"))
        self.agentEmail.setPlaceholderText(_translate("agentInput", "john.smith@myemail.com"))
        self.label_8.setText(_translate("agentInput", "Ext:"))
        self.label_10.setText(_translate("agentInput", "* Denotes a required field."))
        self.clearButton.setText(_translate("agentInput", "&Clear Form"))
        self.closeButton.setText(_translate("agentInput", "Close"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    agentInput = QtWidgets.QDialog()
    ui = Ui_agentInput()
    ui.setupUi(agentInput)
    agentInput.show()
    sys.exit(app.exec_())
