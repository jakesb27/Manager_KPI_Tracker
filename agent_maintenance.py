# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Files\agent_maintenance.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_agentMaintenance(object):
    def setupUi(self, agentMaintenance):
        agentMaintenance.setObjectName("agentMaintenance")
        agentMaintenance.resize(714, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        agentMaintenance.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(agentMaintenance)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(agentMaintenance)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.agentDesc3 = QtWidgets.QComboBox(self.groupBox)
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
        self.agentGoal3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal3.sizePolicy().hasHeightForWidth())
        self.agentGoal3.setSizePolicy(sizePolicy)
        self.agentGoal3.setObjectName("agentGoal3")
        self.gridLayout_3.addWidget(self.agentGoal3, 3, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.agentGoal1 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal1.sizePolicy().hasHeightForWidth())
        self.agentGoal1.setSizePolicy(sizePolicy)
        self.agentGoal1.setObjectName("agentGoal1")
        self.gridLayout_3.addWidget(self.agentGoal1, 1, 5, 1, 1)
        self.agentGoal2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal2.sizePolicy().hasHeightForWidth())
        self.agentGoal2.setSizePolicy(sizePolicy)
        self.agentGoal2.setObjectName("agentGoal2")
        self.gridLayout_3.addWidget(self.agentGoal2, 2, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 2, 1, 1)
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
        self.agentBase3 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase3.sizePolicy().hasHeightForWidth())
        self.agentBase3.setSizePolicy(sizePolicy)
        self.agentBase3.setObjectName("agentBase3")
        self.gridLayout_3.addWidget(self.agentBase3, 3, 3, 1, 1)
        self.agentBase1 = QtWidgets.QLineEdit(self.groupBox)
        self.agentBase1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase1.sizePolicy().hasHeightForWidth())
        self.agentBase1.setSizePolicy(sizePolicy)
        self.agentBase1.setObjectName("agentBase1")
        self.gridLayout_3.addWidget(self.agentBase1, 1, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)
        self.agentBase2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentBase2.sizePolicy().hasHeightForWidth())
        self.agentBase2.setSizePolicy(sizePolicy)
        self.agentBase2.setObjectName("agentBase2")
        self.gridLayout_3.addWidget(self.agentBase2, 2, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.agentDesc1 = QtWidgets.QComboBox(self.groupBox)
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
        self.agentDesc2 = QtWidgets.QComboBox(self.groupBox)
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
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 1, 1, 8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 5, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(agentMaintenance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setMinimumSize(QtCore.QSize(80, 0))
        self.cancelButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout_2.addWidget(self.cancelButton, 3, 8, 1, 1)
        self.undoButton = QtWidgets.QPushButton(agentMaintenance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undoButton.sizePolicy().hasHeightForWidth())
        self.undoButton.setSizePolicy(sizePolicy)
        self.undoButton.setMinimumSize(QtCore.QSize(80, 0))
        self.undoButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.undoButton.setAutoDefault(False)
        self.undoButton.setObjectName("undoButton")
        self.gridLayout_2.addWidget(self.undoButton, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 7, 1, 1)
        self.agentDetails = QtWidgets.QGroupBox(agentMaintenance)
        self.agentDetails.setObjectName("agentDetails")
        self.gridLayout = QtWidgets.QGridLayout(self.agentDetails)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("QLabel{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 8, 1, 3)
        self.agentExt = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentExt.sizePolicy().hasHeightForWidth())
        self.agentExt.setSizePolicy(sizePolicy)
        self.agentExt.setObjectName("agentExt")
        self.gridLayout.addWidget(self.agentExt, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 8, 1, 1)
        self.agentGroup = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGroup.sizePolicy().hasHeightForWidth())
        self.agentGroup.setSizePolicy(sizePolicy)
        self.agentGroup.setObjectName("agentGroup")
        self.gridLayout.addWidget(self.agentGroup, 4, 4, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.agentFirstName = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentFirstName.sizePolicy().hasHeightForWidth())
        self.agentFirstName.setSizePolicy(sizePolicy)
        self.agentFirstName.setObjectName("agentFirstName")
        self.gridLayout.addWidget(self.agentFirstName, 2, 1, 1, 4)
        self.agentGoal = QtWidgets.QLineEdit(self.agentDetails)
        self.agentGoal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentGoal.sizePolicy().hasHeightForWidth())
        self.agentGoal.setSizePolicy(sizePolicy)
        self.agentGoal.setReadOnly(True)
        self.agentGoal.setObjectName("agentGoal")
        self.gridLayout.addWidget(self.agentGoal, 8, 1, 1, 3)
        self.agentDesk = QtWidgets.QLineEdit(self.agentDetails)
        self.agentDesk.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDesk.sizePolicy().hasHeightForWidth())
        self.agentDesk.setSizePolicy(sizePolicy)
        self.agentDesk.setReadOnly(True)
        self.agentDesk.setObjectName("agentDesk")
        self.gridLayout.addWidget(self.agentDesk, 8, 5, 1, 1)
        self.saveLabel = QtWidgets.QLabel(self.agentDetails)
        self.saveLabel.setStyleSheet("QLabel{\n"
"    color: rgba(255, 0, 0, 0);\n"
"}")
        self.saveLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saveLabel.setWordWrap(True)
        self.saveLabel.setObjectName("saveLabel")
        self.gridLayout.addWidget(self.saveLabel, 0, 10, 2, 1)
        self.label_20 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)
        self.agentLastName = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentLastName.sizePolicy().hasHeightForWidth())
        self.agentLastName.setSizePolicy(sizePolicy)
        self.agentLastName.setObjectName("agentLastName")
        self.gridLayout.addWidget(self.agentLastName, 3, 1, 1, 4)
        self.label_8 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.agentDetails)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 8, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 2)
        self.agentManager = QtWidgets.QComboBox(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentManager.sizePolicy().hasHeightForWidth())
        self.agentManager.setSizePolicy(sizePolicy)
        self.agentManager.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.agentManager.setObjectName("agentManager")
        self.agentManager.addItem("")
        self.gridLayout.addWidget(self.agentManager, 4, 10, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 5, 1, 1)
        self.agentEmail = QtWidgets.QLineEdit(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentEmail.sizePolicy().hasHeightForWidth())
        self.agentEmail.setSizePolicy(sizePolicy)
        self.agentEmail.setObjectName("agentEmail")
        self.gridLayout.addWidget(self.agentEmail, 3, 8, 1, 3)
        self.activeEmpBox = QtWidgets.QCheckBox(self.agentDetails)
        self.activeEmpBox.setObjectName("activeEmpBox")
        self.gridLayout.addWidget(self.activeEmpBox, 1, 1, 1, 1)
        self.employeeSelect = QtWidgets.QComboBox(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeSelect.sizePolicy().hasHeightForWidth())
        self.employeeSelect.setSizePolicy(sizePolicy)
        self.employeeSelect.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.employeeSelect.setObjectName("employeeSelect")
        self.gridLayout.addWidget(self.employeeSelect, 0, 1, 1, 4)
        self.gridLayout_2.addWidget(self.agentDetails, 1, 1, 1, 8)
        self.clearButton = QtWidgets.QPushButton(agentMaintenance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(80, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.clearButton.setAutoDefault(False)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 3, 6, 1, 1)
        self.saveButton = QtWidgets.QPushButton(agentMaintenance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(80, 0))
        self.saveButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.saveButton.setAutoDefault(False)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_2.addWidget(self.saveButton, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 4, 1, 1)

        self.retranslateUi(agentMaintenance)
        QtCore.QMetaObject.connectSlotsByName(agentMaintenance)
        agentMaintenance.setTabOrder(self.employeeSelect, self.activeEmpBox)
        agentMaintenance.setTabOrder(self.activeEmpBox, self.agentFirstName)
        agentMaintenance.setTabOrder(self.agentFirstName, self.agentLastName)
        agentMaintenance.setTabOrder(self.agentLastName, self.agentEmail)
        agentMaintenance.setTabOrder(self.agentEmail, self.agentExt)
        agentMaintenance.setTabOrder(self.agentExt, self.agentGroup)
        agentMaintenance.setTabOrder(self.agentGroup, self.agentManager)
        agentMaintenance.setTabOrder(self.agentManager, self.agentGoal)
        agentMaintenance.setTabOrder(self.agentGoal, self.agentDesk)
        agentMaintenance.setTabOrder(self.agentDesk, self.agentDesc1)
        agentMaintenance.setTabOrder(self.agentDesc1, self.agentBase1)
        agentMaintenance.setTabOrder(self.agentBase1, self.agentGoal1)
        agentMaintenance.setTabOrder(self.agentGoal1, self.agentDesc2)
        agentMaintenance.setTabOrder(self.agentDesc2, self.agentBase2)
        agentMaintenance.setTabOrder(self.agentBase2, self.agentGoal2)
        agentMaintenance.setTabOrder(self.agentGoal2, self.agentDesc3)
        agentMaintenance.setTabOrder(self.agentDesc3, self.agentBase3)
        agentMaintenance.setTabOrder(self.agentBase3, self.agentGoal3)
        agentMaintenance.setTabOrder(self.agentGoal3, self.saveButton)
        agentMaintenance.setTabOrder(self.saveButton, self.undoButton)
        agentMaintenance.setTabOrder(self.undoButton, self.clearButton)
        agentMaintenance.setTabOrder(self.clearButton, self.cancelButton)

    def retranslateUi(self, agentMaintenance):
        _translate = QtCore.QCoreApplication.translate
        agentMaintenance.setWindowTitle(_translate("agentMaintenance", "Employee Maintenance"))
        self.groupBox.setTitle(_translate("agentMaintenance", "KPI Goals"))
        self.agentDesc3.setItemText(0, _translate("agentMaintenance", " - Select A Goal - "))
        self.agentDesc3.setItemText(1, _translate("agentMaintenance", "Connects (Total)"))
        self.agentDesc3.setItemText(2, _translate("agentMaintenance", "Connects (Per Hour)"))
        self.agentDesc3.setItemText(3, _translate("agentMaintenance", "RPC (Total)"))
        self.agentDesc3.setItemText(4, _translate("agentMaintenance", "RPC (Per Hour)"))
        self.agentDesc3.setItemText(5, _translate("agentMaintenance", "Promises Conv%"))
        self.agentDesc3.setItemText(6, _translate("agentMaintenance", "Conversions Per Hour"))
        self.agentDesc3.setItemText(7, _translate("agentMaintenance", "Secured (%)"))
        self.agentDesc3.setItemText(8, _translate("agentMaintenance", "Secured (Avg Payment)"))
        self.agentDesc3.setItemText(9, _translate("agentMaintenance", "Fees (Total)"))
        self.agentDesc3.setItemText(10, _translate("agentMaintenance", "Fees (Per Hour)"))
        self.agentDesc3.setItemText(11, _translate("agentMaintenance", "Overall Totals"))
        self.agentDesc3.setItemText(12, _translate("agentMaintenance", "Payment Plan"))
        self.agentDesc3.setItemText(13, _translate("agentMaintenance", "Category Review"))
        self.label_11.setText(_translate("agentMaintenance", "Productivity Goal 1:"))
        self.label_15.setText(_translate("agentMaintenance", "Base Value*:"))
        self.label_4.setText(_translate("agentMaintenance", "*Please note that all percentages must be input as a whole number and should not contain the \"%\" symbol. For example 20% should be input as \"20\" and not \".20\", \"0.20\". Monetary values should not contain a comma seperator or the \"$\" symbol. For example $1,654.23 should be input as \"1654.23\"."))
        self.label_14.setText(_translate("agentMaintenance", "Base Value*:"))
        self.label_18.setText(_translate("agentMaintenance", "Goal*:"))
        self.label_19.setText(_translate("agentMaintenance", "Goal*:"))
        self.label_12.setText(_translate("agentMaintenance", "Productivity Goal 2:"))
        self.label_13.setText(_translate("agentMaintenance", "Productivity Goal 3:"))
        self.agentDesc1.setItemText(0, _translate("agentMaintenance", " - Select A Goal - "))
        self.agentDesc1.setItemText(1, _translate("agentMaintenance", "Connects (Total)"))
        self.agentDesc1.setItemText(2, _translate("agentMaintenance", "Connects (Per Hour)"))
        self.agentDesc1.setItemText(3, _translate("agentMaintenance", "RPC (Total)"))
        self.agentDesc1.setItemText(4, _translate("agentMaintenance", "RPC (Per Hour)"))
        self.agentDesc1.setItemText(5, _translate("agentMaintenance", "Promises Conv%"))
        self.agentDesc1.setItemText(6, _translate("agentMaintenance", "Conversions Per Hour"))
        self.agentDesc1.setItemText(7, _translate("agentMaintenance", "Secured (%)"))
        self.agentDesc1.setItemText(8, _translate("agentMaintenance", "Secured (Avg Payment)"))
        self.agentDesc1.setItemText(9, _translate("agentMaintenance", "Fees (Total)"))
        self.agentDesc1.setItemText(10, _translate("agentMaintenance", "Fees (Per Hour)"))
        self.agentDesc1.setItemText(11, _translate("agentMaintenance", "Overall Totals"))
        self.agentDesc1.setItemText(12, _translate("agentMaintenance", "Payment Plan"))
        self.agentDesc1.setItemText(13, _translate("agentMaintenance", "Category Review"))
        self.agentDesc2.setItemText(0, _translate("agentMaintenance", " - Select A Goal - "))
        self.agentDesc2.setItemText(1, _translate("agentMaintenance", "Connects (Total)"))
        self.agentDesc2.setItemText(2, _translate("agentMaintenance", "Connects (Per Hour)"))
        self.agentDesc2.setItemText(3, _translate("agentMaintenance", "RPC (Total)"))
        self.agentDesc2.setItemText(4, _translate("agentMaintenance", "RPC (Per Hour)"))
        self.agentDesc2.setItemText(5, _translate("agentMaintenance", "Promises Conv%"))
        self.agentDesc2.setItemText(6, _translate("agentMaintenance", "Conversions Per Hour"))
        self.agentDesc2.setItemText(7, _translate("agentMaintenance", "Secured (%)"))
        self.agentDesc2.setItemText(8, _translate("agentMaintenance", "Secured (Avg Payment)"))
        self.agentDesc2.setItemText(9, _translate("agentMaintenance", "Fees (Total)"))
        self.agentDesc2.setItemText(10, _translate("agentMaintenance", "Fees (Per Hour)"))
        self.agentDesc2.setItemText(11, _translate("agentMaintenance", "Overall Totals"))
        self.agentDesc2.setItemText(12, _translate("agentMaintenance", "Payment Plan"))
        self.agentDesc2.setItemText(13, _translate("agentMaintenance", "Category Review"))
        self.label_16.setText(_translate("agentMaintenance", "Base Value*:"))
        self.label_17.setText(_translate("agentMaintenance", "Goal*:"))
        self.cancelButton.setText(_translate("agentMaintenance", "Cl&ose"))
        self.undoButton.setText(_translate("agentMaintenance", "&Undo"))
        self.agentDetails.setTitle(_translate("agentMaintenance", "Agent Information"))
        self.label_10.setText(_translate("agentMaintenance", "* Desk and goal can only be changed in CollectOne via the \"User ID Sub-Maintenance\" and \"Desks\" tables."))
        self.label_9.setText(_translate("agentMaintenance", "Manager:"))
        self.label_7.setText(_translate("agentMaintenance", "Last Name:"))
        self.saveLabel.setText(_translate("agentMaintenance", "Changes have been made. Please click \"Save\" before exiting or all changes will be lost."))
        self.label_20.setText(_translate("agentMaintenance", "Employee:"))
        self.label_8.setText(_translate("agentMaintenance", "Ext:"))
        self.label_21.setText(_translate("agentMaintenance", "Desk*:"))
        self.label.setText(_translate("agentMaintenance", "First Name:"))
        self.label_3.setText(_translate("agentMaintenance", "Goal*:"))
        self.label_5.setText(_translate("agentMaintenance", "Group:"))
        self.agentManager.setItemText(0, _translate("agentMaintenance", " - Select A Manager - "))
        self.label_6.setText(_translate("agentMaintenance", "Email:"))
        self.activeEmpBox.setText(_translate("agentMaintenance", "Active Employee"))
        self.clearButton.setText(_translate("agentMaintenance", "&Clear"))
        self.saveButton.setText(_translate("agentMaintenance", "&Save"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    agentMaintenance = QtWidgets.QDialog()
    ui = Ui_agentMaintenance()
    ui.setupUi(agentMaintenance)
    agentMaintenance.show()
    sys.exit(app.exec_())
