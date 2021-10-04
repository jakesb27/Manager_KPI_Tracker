# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Files\review_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reviewForm(object):
    def setupUi(self, reviewForm):
        reviewForm.setObjectName("reviewForm")
        reviewForm.resize(788, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        reviewForm.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(reviewForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.agentDetails = QtWidgets.QGroupBox(reviewForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDetails.sizePolicy().hasHeightForWidth())
        self.agentDetails.setSizePolicy(sizePolicy)
        self.agentDetails.setObjectName("agentDetails")
        self.gridLayout = QtWidgets.QGridLayout(self.agentDetails)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.agentDetails)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.agentExt = QtWidgets.QLineEdit(self.agentDetails)
        self.agentExt.setReadOnly(True)
        self.agentExt.setObjectName("agentExt")
        self.gridLayout.addWidget(self.agentExt, 0, 5, 1, 1)
        self.mainTopic = QtWidgets.QLineEdit(self.agentDetails)
        self.mainTopic.setObjectName("mainTopic")
        self.gridLayout.addWidget(self.mainTopic, 5, 1, 1, 5)
        self.issueDate = QtWidgets.QDateEdit(self.agentDetails)
        self.issueDate.setAlignment(QtCore.Qt.AlignCenter)
        self.issueDate.setCalendarPopup(True)
        self.issueDate.setObjectName("issueDate")
        self.gridLayout.addWidget(self.issueDate, 3, 4, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.agentDetails)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.agentUserID = QtWidgets.QLineEdit(self.agentDetails)
        self.agentUserID.setMinimumSize(QtCore.QSize(50, 0))
        self.agentUserID.setReadOnly(True)
        self.agentUserID.setObjectName("agentUserID")
        self.gridLayout.addWidget(self.agentUserID, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.agentDetails)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.agentDesk = QtWidgets.QLineEdit(self.agentDetails)
        self.agentDesk.setReadOnly(True)
        self.agentDesk.setObjectName("agentDesk")
        self.gridLayout.addWidget(self.agentDesk, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.agentDetails)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.agentGroup = QtWidgets.QLineEdit(self.agentDetails)
        self.agentGroup.setReadOnly(True)
        self.agentGroup.setObjectName("agentGroup")
        self.gridLayout.addWidget(self.agentGroup, 1, 1, 1, 2)
        self.meetLocation = QtWidgets.QLineEdit(self.agentDetails)
        self.meetLocation.setObjectName("meetLocation")
        self.gridLayout.addWidget(self.meetLocation, 1, 4, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.agentDetails)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.agentDetails)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.agentDetails)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.agentDetails)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.issuedBy = QtWidgets.QComboBox(self.agentDetails)
        self.issuedBy.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.issuedBy.setObjectName("issuedBy")
        self.gridLayout.addWidget(self.issuedBy, 3, 1, 1, 2)
        self.gridLayout_2.addWidget(self.agentDetails, 0, 2, 1, 1)
        self.saveReview = QtWidgets.QPushButton(reviewForm)
        self.saveReview.setMinimumSize(QtCore.QSize(119, 0))
        self.saveReview.setMaximumSize(QtCore.QSize(119, 16777215))
        self.saveReview.setObjectName("saveReview")
        self.gridLayout_2.addWidget(self.saveReview, 4, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(reviewForm)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tempType = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempType.sizePolicy().hasHeightForWidth())
        self.tempType.setSizePolicy(sizePolicy)
        self.tempType.setStyleSheet("QLabel{\n"
"    color: rgb(43, 87, 130);\n"
"    font: 16pt \"Corbel\";\n"
"    font-weight: bold;\n"
"    text-decoration: underline;\n"
"}")
        self.tempType.setObjectName("tempType")
        self.gridLayout_3.addWidget(self.tempType, 0, 1, 1, 1)
        self.discFrame = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discFrame.sizePolicy().hasHeightForWidth())
        self.discFrame.setSizePolicy(sizePolicy)
        self.discFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.discFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.discFrame.setObjectName("discFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.discFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.discFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.disciplineType = QtWidgets.QComboBox(self.discFrame)
        self.disciplineType.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.disciplineType.setObjectName("disciplineType")
        self.disciplineType.addItem("")
        self.disciplineType.addItem("")
        self.disciplineType.addItem("")
        self.disciplineType.addItem("")
        self.disciplineType.addItem("")
        self.horizontalLayout_2.addWidget(self.disciplineType)
        self.gridLayout_3.addWidget(self.discFrame, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.managerNotes = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.managerNotes.setReadOnly(True)
        self.managerNotes.setTabStopWidth(40)
        self.managerNotes.setObjectName("managerNotes")
        self.gridLayout_3.addWidget(self.managerNotes, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(reviewForm)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
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
        self.managerCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.managerCombo.setMinimumSize(QtCore.QSize(200, 0))
        self.managerCombo.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.managerCombo.setObjectName("managerCombo")
        self.managerCombo.addItem("")
        self.gridLayout_4.addWidget(self.managerCombo, 0, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioDisc = QtWidgets.QRadioButton(self.frame_2)
        self.radioDisc.setObjectName("radioDisc")
        self.gridLayout_5.addWidget(self.radioDisc, 1, 1, 1, 1)
        self.radio1on1 = QtWidgets.QRadioButton(self.frame_2)
        self.radio1on1.setChecked(True)
        self.radio1on1.setObjectName("radio1on1")
        self.gridLayout_5.addWidget(self.radio1on1, 0, 0, 1, 1)
        self.radioCoach = QtWidgets.QRadioButton(self.frame_2)
        self.radioCoach.setObjectName("radioCoach")
        self.gridLayout_5.addWidget(self.radioCoach, 1, 0, 1, 1)
        self.radioSbS = QtWidgets.QRadioButton(self.frame_2)
        self.radioSbS.setObjectName("radioSbS")
        self.gridLayout_5.addWidget(self.radioSbS, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 2, 1, 1, 2)
        self.employeeSelect = QtWidgets.QComboBox(self.groupBox_2)
        self.employeeSelect.setMinimumSize(QtCore.QSize(200, 0))
        self.employeeSelect.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.employeeSelect.setObjectName("employeeSelect")
        self.gridLayout_4.addWidget(self.employeeSelect, 1, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(reviewForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.employeeGraphs = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeGraphs.sizePolicy().hasHeightForWidth())
        self.employeeGraphs.setSizePolicy(sizePolicy)
        self.employeeGraphs.setObjectName("employeeGraphs")
        self.horizontalLayout.addWidget(self.employeeGraphs)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setMinimumSize(QtCore.QSize(119, 0))
        self.closeButton.setMaximumSize(QtCore.QSize(119, 16777215))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.gridLayout_2.addWidget(self.frame, 4, 2, 1, 1)

        self.retranslateUi(reviewForm)
        QtCore.QMetaObject.connectSlotsByName(reviewForm)
        reviewForm.setTabOrder(self.managerCombo, self.employeeSelect)

    def retranslateUi(self, reviewForm):
        _translate = QtCore.QCoreApplication.translate
        reviewForm.setWindowTitle(_translate("reviewForm", "Employee Review Form"))
        self.agentDetails.setTitle(_translate("reviewForm", "Document Information"))
        self.label.setText(_translate("reviewForm", "User ID:"))
        self.mainTopic.setPlaceholderText(_translate("reviewForm", "-Required-"))
        self.label_5.setText(_translate("reviewForm", "Issue Date:"))
        self.label_2.setText(_translate("reviewForm", "Desk:"))
        self.label_7.setText(_translate("reviewForm", "Main Topic:"))
        self.meetLocation.setPlaceholderText(_translate("reviewForm", "-Required-"))
        self.label_8.setText(_translate("reviewForm", "Ext:"))
        self.label_6.setText(_translate("reviewForm", "Issued By:"))
        self.label_3.setText(_translate("reviewForm", "Group:"))
        self.label_4.setText(_translate("reviewForm", "Location:"))
        self.saveReview.setText(_translate("reviewForm", "&Save Review"))
        self.groupBox_3.setTitle(_translate("reviewForm", "Document Notes"))
        self.tempType.setText(_translate("reviewForm", "One on One Review"))
        self.label_10.setText(_translate("reviewForm", "Disciplinary Type:"))
        self.disciplineType.setItemText(0, _translate("reviewForm", "1. Verbal"))
        self.disciplineType.setItemText(1, _translate("reviewForm", "2. Written"))
        self.disciplineType.setItemText(2, _translate("reviewForm", "3. Final Written"))
        self.disciplineType.setItemText(3, _translate("reviewForm", "4. PIP"))
        self.disciplineType.setItemText(4, _translate("reviewForm", "5. Term"))
        self.managerNotes.setPlaceholderText(_translate("reviewForm", "Select employee to begin..."))
        self.managerCombo.setItemText(0, _translate("reviewForm", "All"))
        self.radioDisc.setText(_translate("reviewForm", "Disciplinary"))
        self.radio1on1.setText(_translate("reviewForm", "One on One"))
        self.radioCoach.setText(_translate("reviewForm", "Coaching"))
        self.radioSbS.setText(_translate("reviewForm", "Side by Side"))
        self.label_20.setText(_translate("reviewForm", "Employee Select:"))
        self.label_21.setText(_translate("reviewForm", "Manager Filter:"))
        self.employeeGraphs.setText(_translate("reviewForm", "Trending Graphs"))
        self.closeButton.setText(_translate("reviewForm", "Close"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reviewForm = QtWidgets.QDialog()
    ui = Ui_reviewForm()
    ui.setupUi(reviewForm)
    reviewForm.show()
    sys.exit(app.exec_())