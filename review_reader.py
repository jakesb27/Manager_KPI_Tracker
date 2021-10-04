# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Files\review_reader.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reviewReader(object):
    def setupUi(self, reviewReader):
        reviewReader.setObjectName("reviewReader")
        reviewReader.resize(788, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        reviewReader.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(reviewReader)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(reviewReader)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem, 0, 0, 1, 1)
        self.managerNotes = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.managerNotes.setReadOnly(True)
        self.managerNotes.setPlainText("")
        self.managerNotes.setTabStopWidth(40)
        self.managerNotes.setObjectName("managerNotes")
        self.gridLayout_11.addWidget(self.managerNotes, 1, 0, 1, 3)
        self.discFrame_2 = QtWidgets.QFrame(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discFrame_2.sizePolicy().hasHeightForWidth())
        self.discFrame_2.setSizePolicy(sizePolicy)
        self.discFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.discFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.discFrame_2.setObjectName("discFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.discFrame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_19 = QtWidgets.QLabel(self.discFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.discTypeEdit = QtWidgets.QLineEdit(self.discFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discTypeEdit.sizePolicy().hasHeightForWidth())
        self.discTypeEdit.setSizePolicy(sizePolicy)
        self.discTypeEdit.setReadOnly(True)
        self.discTypeEdit.setObjectName("discTypeEdit")
        self.horizontalLayout_3.addWidget(self.discTypeEdit)
        self.gridLayout_11.addWidget(self.discFrame_2, 0, 2, 1, 1)
        self.tempTypeEdit = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempTypeEdit.sizePolicy().hasHeightForWidth())
        self.tempTypeEdit.setSizePolicy(sizePolicy)
        self.tempTypeEdit.setStyleSheet("QLabel{\n"
"    color: rgb(43, 87, 130);\n"
"    font: 16pt \"Corbel\";\n"
"    font-weight: bold;\n"
"    text-decoration: underline;\n"
"}")
        self.tempTypeEdit.setObjectName("tempTypeEdit")
        self.gridLayout_11.addWidget(self.tempTypeEdit, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.buttonStack = QtWidgets.QStackedWidget(reviewReader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStack.sizePolicy().hasHeightForWidth())
        self.buttonStack.setSizePolicy(sizePolicy)
        self.buttonStack.setObjectName("buttonStack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editReview = QtWidgets.QPushButton(self.page)
        self.editReview.setMinimumSize(QtCore.QSize(119, 0))
        self.editReview.setMaximumSize(QtCore.QSize(119, 16777215))
        self.editReview.setObjectName("editReview")
        self.horizontalLayout.addWidget(self.editReview)
        self.closeButton = QtWidgets.QPushButton(self.page)
        self.closeButton.setMinimumSize(QtCore.QSize(119, 0))
        self.closeButton.setMaximumSize(QtCore.QSize(119, 16777215))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.buttonStack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteReview = QtWidgets.QPushButton(self.page_2)
        self.deleteReview.setMinimumSize(QtCore.QSize(125, 0))
        self.deleteReview.setMaximumSize(QtCore.QSize(125, 16777215))
        self.deleteReview.setObjectName("deleteReview")
        self.horizontalLayout_2.addWidget(self.deleteReview)
        self.saveButton = QtWidgets.QPushButton(self.page_2)
        self.saveButton.setMinimumSize(QtCore.QSize(125, 0))
        self.saveButton.setMaximumSize(QtCore.QSize(125, 16777215))
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.exitEdit = QtWidgets.QPushButton(self.page_2)
        self.exitEdit.setMinimumSize(QtCore.QSize(125, 0))
        self.exitEdit.setMaximumSize(QtCore.QSize(125, 16777215))
        self.exitEdit.setObjectName("exitEdit")
        self.horizontalLayout_2.addWidget(self.exitEdit)
        self.buttonStack.addWidget(self.page_2)
        self.gridLayout.addWidget(self.buttonStack, 2, 0, 1, 1)
        self.agentDetailsEdit = QtWidgets.QGroupBox(reviewReader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.agentDetailsEdit.sizePolicy().hasHeightForWidth())
        self.agentDetailsEdit.setSizePolicy(sizePolicy)
        self.agentDetailsEdit.setObjectName("agentDetailsEdit")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.agentDetailsEdit)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.agentDetailsEdit)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)
        self.issueDate = QtWidgets.QLineEdit(self.frame_3)
        self.issueDate.setReadOnly(True)
        self.issueDate.setObjectName("issueDate")
        self.gridLayout_8.addWidget(self.issueDate, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)
        self.meetLocation = QtWidgets.QLineEdit(self.frame_3)
        self.meetLocation.setReadOnly(True)
        self.meetLocation.setObjectName("meetLocation")
        self.gridLayout_8.addWidget(self.meetLocation, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 2, 0, 1, 1)
        self.mainTopic = QtWidgets.QLineEdit(self.frame_3)
        self.mainTopic.setText("")
        self.mainTopic.setReadOnly(True)
        self.mainTopic.setObjectName("mainTopic")
        self.gridLayout_8.addWidget(self.mainTopic, 2, 1, 1, 3)
        self.issuedBy = QtWidgets.QLineEdit(self.frame_3)
        self.issuedBy.setReadOnly(True)
        self.issuedBy.setObjectName("issuedBy")
        self.gridLayout_8.addWidget(self.issuedBy, 1, 1, 1, 2)
        self.gridLayout_7.addWidget(self.frame_3, 0, 9, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.agentDetailsEdit)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 2, 0, 1, 1)
        self.agentDesk = QtWidgets.QLineEdit(self.frame_4)
        self.agentDesk.setReadOnly(True)
        self.agentDesk.setObjectName("agentDesk")
        self.gridLayout_9.addWidget(self.agentDesk, 2, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 1, 0, 1, 1)
        self.agentUserID = QtWidgets.QLineEdit(self.frame_4)
        self.agentUserID.setMinimumSize(QtCore.QSize(50, 0))
        self.agentUserID.setReadOnly(True)
        self.agentUserID.setObjectName("agentUserID")
        self.gridLayout_9.addWidget(self.agentUserID, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 1, 2, 1, 1)
        self.agentExt = QtWidgets.QLineEdit(self.frame_4)
        self.agentExt.setReadOnly(True)
        self.agentExt.setObjectName("agentExt")
        self.gridLayout_9.addWidget(self.agentExt, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 2, 2, 1, 1)
        self.agentGroup = QtWidgets.QLineEdit(self.frame_4)
        self.agentGroup.setReadOnly(True)
        self.agentGroup.setObjectName("agentGroup")
        self.gridLayout_9.addWidget(self.agentGroup, 2, 3, 1, 1)
        self.employee = QtWidgets.QLineEdit(self.frame_4)
        self.employee.setReadOnly(True)
        self.employee.setObjectName("employee")
        self.gridLayout_9.addWidget(self.employee, 0, 1, 1, 3)
        self.gridLayout_7.addWidget(self.frame_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.agentDetailsEdit, 0, 0, 1, 1)

        self.retranslateUi(reviewReader)
        self.buttonStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(reviewReader)

    def retranslateUi(self, reviewReader):
        _translate = QtCore.QCoreApplication.translate
        reviewReader.setWindowTitle(_translate("reviewReader", "Employee Review Reader"))
        self.groupBox_4.setTitle(_translate("reviewReader", "Document Notes"))
        self.label_19.setText(_translate("reviewReader", "Disciplinary Type:"))
        self.tempTypeEdit.setText(_translate("reviewReader", "One on One Review"))
        self.editReview.setText(_translate("reviewReader", "&Edit Review"))
        self.closeButton.setText(_translate("reviewReader", "Close"))
        self.deleteReview.setText(_translate("reviewReader", "Delete Review"))
        self.saveButton.setText(_translate("reviewReader", "Save Changes"))
        self.exitEdit.setText(_translate("reviewReader", "Exit Editor"))
        self.agentDetailsEdit.setTitle(_translate("reviewReader", "Document Information"))
        self.label_9.setText(_translate("reviewReader", "Issue Date:"))
        self.label_11.setText(_translate("reviewReader", "Location:"))
        self.label_12.setText(_translate("reviewReader", "Issued By:"))
        self.label_13.setText(_translate("reviewReader", "Main Topic:"))
        self.label_14.setText(_translate("reviewReader", "Employee:"))
        self.label_15.setText(_translate("reviewReader", "Desk:"))
        self.label_16.setText(_translate("reviewReader", "User ID:"))
        self.label_17.setText(_translate("reviewReader", "Ext:"))
        self.label_18.setText(_translate("reviewReader", "Group:"))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reviewReader = QtWidgets.QDialog()
    ui = Ui_reviewReader()
    ui.setupUi(reviewReader)
    reviewReader.show()
    sys.exit(app.exec_())