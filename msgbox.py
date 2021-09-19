from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap


icon_path = r"\\172.16.33.31\collectone\COLLECTOR RESOURCES\KPI Tracker\cmredb\Meduit_logo.ico"


def closing_time():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("This application is only available during normal business hours.")
    msg.setWindowTitle("Closing Time")
    msg.setStandardButtons(QMessageBox.Ok)
    return msg


def confirm_save():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("Do you want to save the changes made to this employee?")
    msg.setWindowTitle("Save Changes")
    msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
    return msg


def inactive_warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    icon = QIcon()
    icon.addPixmap(
        QPixmap(icon_path),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText('WARNING: You are about to make this employee "Inactive".\n\n'
                'All KPI Goals & Base Values will be permanently erased. Please confirm\n'
                'you want to make this employee "Inactive".')
    msg.setWindowTitle("Update Employee")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg


def desk_update_complete():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    icon = QIcon()
    icon.addPixmap(
        QPixmap(icon_path),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText('CDS Desk update is complete!.')
    msg.setWindowTitle("Desk Update Complete")
    msg.setStandardButtons(QMessageBox.Ok)
    return msg


def unavailable():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    icon = QIcon()
    icon.addPixmap(
        QPixmap(icon_path),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText('This feature is currently unavailable at this time.')
    msg.setWindowTitle("Unavailable")
    msg.setStandardButtons(QMessageBox.Ok)
    return msg
