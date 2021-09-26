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
    msg.setIcon(QMessageBox.Question)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("Please confirm you want to save your changes.")
    msg.setWindowTitle("Save Changes")
    msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
    return msg


def confirm_close_unsaved():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("You are about to close without saving any changes.\n"
                "Please confirm you do not want to save your changes.")
    msg.setWindowTitle("Close Without Saving")
    msg.setStandardButtons(QMessageBox.Close | QMessageBox.Cancel)
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


def employee_added():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("Employee has been added successfully!")
    msg.setWindowTitle("Success")
    msg.setStandardButtons(QMessageBox.Ok)
    return msg


def employee_add_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("ERROR: Please fill out all the required fields and try again.")
    msg.setWindowTitle("Failed")
    msg.setStandardButtons(QMessageBox.Ok)
    return msg


def employee_add_dupe():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    icon = QIcon(icon_path)
    icon.addPixmap(
        QPixmap(),
        QIcon.Normal, QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setText("ERROR: An error occurred while trying to add this employee. Typically\n"
                "this happens if the UltiPro ID entered is already in use. Please confirm\n"
                "you have the correct UltiPro ID for the user you are entering and try again.")
    msg.setWindowTitle("Failed")
    msg.setStandardButtons(QMessageBox.Ok)
    return msg
