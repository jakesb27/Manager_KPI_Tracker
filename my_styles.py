inactive_emp = """
QDialog{
	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));
}
QWidget{
	font: 11pt "Corbel";
	font-weight: bold;
}
QWidget::disabled{
	font: 11pt "Corbel";
	font-weight: bold;
}
QGroupBox{
	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));
	border: 1px solid black;
	border-radius: 3px;
	margin-top: 1ex;
	padding-top: 18;
	font: 11pt "Corbel";
	font-weight: bold;
}
QGroupBox::title{
	background-color: rgb(195, 195, 195);
	border: 1px solid black;
	border-radius: 3px;
	padding: 2 10px;
	subcontrol-origin: margin;
	subcontrol-position: top;
	font: 11pt "Corbel";
	font-weight: bold;
}
QLineEdit{
	background-color: rgb(225, 225, 225);
	color: rgb(100, 100, 100);
	border: 1px solid black;
	font: 10pt "MS Shell Dlg 2";
}
QTextEdit{
	font: 12pt "Corbel";
}
QStatusBar{
	font: 10pt "MS Shell Dlg 2";
}
QPushButton{
	border: 1px solid black;
	border-radius: 3px;
	padding: 2px;
	padding-left: 13px;
	padding-right: 13px;
	background-color: rgb(195, 195, 195);
	font: 11pt "Corbel";
	font-weight: bold;
}
QPushButton::hover{
	border: 2px solid black;
	border-radius: 3px;
	padding: 2px;
	padding-left: 10px;
	padding-right: 10px;
	width: 80px;
	background-color: rgb(215, 215, 215);
	font: 11pt "Corbel";
	font-weight: bold;
}
QPushButton::pressed{
	border: 2px solid black;
	border-radius: 3px;
	padding: 2px;
	padding-left: 8px;
	padding-right: 8px;
	background-color: rgb(175, 175, 175);
	font: 11pt "Corbel";
	font-weight: bold;
}
"""

active_emp = """
QDialog{
	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));
}
QWidget{
	font: 11pt "Corbel";
	font-weight: bold;
}
QGroupBox{
	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 209), stop:0.485876 rgba(181, 207, 220, 239), stop:1 rgba(85, 199, 255, 196));
	border: 1px solid black;
	border-radius: 3px;
	margin-top: 1ex;
	padding-top: 18;
	font: 11pt "Corbel";
	font-weight: bold;
}
QGroupBox::title{
	background-color: rgb(195, 195, 195);
	border: 1px solid black;
	border-radius: 3px;
	padding: 2 10px;
	subcontrol-origin: margin;
	subcontrol-position: top;
	font: 11pt "Corbel";
	font-weight: bold;
}
QComboBox{
	background-color: rgb(223, 223, 223);
}
QLineEdit{
	border: 1px solid black;
	font: 10pt "MS Shell Dlg 2";
}
QTextEdit{
	font: 12pt "Corbel";
}
QStatusBar{
	font: 10pt "MS Shell Dlg 2";
}
QPushButton{
	border: 1px solid black;
	border-radius: 3px;
	padding: 2px;
	padding-left: 13px;
	padding-right: 13px;
	background-color: rgb(195, 195, 195);
	font: 11pt "Corbel";
	font-weight: bold;
}
QPushButton::hover{
	border: 2px solid black;
	border-radius: 3px;
	padding: 2px;
	padding-left: 10px;
	padding-right: 10px;
	width: 80px;
	background-color: rgb(215, 215, 215);
	font: 11pt "Corbel";
	font-weight: bold;
}
QPushButton::pressed{
	border: 2px solid black;
	border-radius: 3px;
	padding: 2px;
	padding-left: 8px;
	padding-right: 8px;
	background-color: rgb(175, 175, 175);
	font: 11pt "Corbel";
	font-weight: bold;
}
"""