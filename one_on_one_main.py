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
        oneOnOneMain.resize(698, 423)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        oneOnOneMain.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(oneOnOneMain)
        self.gridLayout.setObjectName("gridLayout")
        self.managerCombo = QtWidgets.QComboBox(oneOnOneMain)
        self.managerCombo.setMinimumSize(QtCore.QSize(150, 0))
        self.managerCombo.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));\n"
"}")
        self.managerCombo.setObjectName("managerCombo")
        self.managerCombo.addItem("")
        self.gridLayout.addWidget(self.managerCombo, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(oneOnOneMain)
        self.label_2.setMinimumSize(QtCore.QSize(200, 93))
        self.label_2.setMaximumSize(QtCore.QSize(200, 93))
        self.label_2.setStyleSheet("image: url(:/logos/Images/Meduit Email.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.557, y1:0, x2:0.511, y2:1, stop:0.528409 rgba(255, 255, 255, 174));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.oneXoneView = QtWidgets.QTableView(oneOnOneMain)
        self.oneXoneView.setStyleSheet("QTableView{\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.oneXoneView.setAlternatingRowColors(True)
        self.oneXoneView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.oneXoneView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.oneXoneView.setSortingEnabled(True)
        self.oneXoneView.setObjectName("oneXoneView")
        self.gridLayout.addWidget(self.oneXoneView, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(oneOnOneMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.557, y1:0, x2:0.511, y2:1, stop:0.528409 rgba(255, 255, 255, 174));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(oneOnOneMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.557, y1:0, x2:0.511, y2:1, stop:0.528409 rgba(255, 255, 255, 174));")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 4)

        self.retranslateUi(oneOnOneMain)
        QtCore.QMetaObject.connectSlotsByName(oneOnOneMain)

    def retranslateUi(self, oneOnOneMain):
        _translate = QtCore.QCoreApplication.translate
        oneOnOneMain.setWindowTitle(_translate("oneOnOneMain", "One On One Tracker"))
        self.managerCombo.setItemText(0, _translate("oneOnOneMain", "All"))
        self.label.setText(_translate("oneOnOneMain", "Manager Select"))
        self.label_3.setText(_translate("oneOnOneMain", "Double Click completion date to view details."))
import main_images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    oneOnOneMain = QtWidgets.QDialog()
    ui = Ui_oneOnOneMain()
    ui.setupUi(oneOnOneMain)
    oneOnOneMain.show()
    sys.exit(app.exec_())
