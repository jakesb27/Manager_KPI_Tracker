active_style = """
QMainWindow{
	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));
}
QDialog{
	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0.011, stop:0 rgba(255, 218, 144, 200), stop:1 rgba(129, 213, 255, 126));
}
QWidget{
	font: 11pt "Corbel";
	font-weight: bold;
}
QPlainTextEdit{
	border: 1px solid black;
	font: 10pt "MS Shell Dlg 2";
}
QPlainTextEdit[readOnly="true"]{
	background-color: rgb(225, 225, 225);
	font: 10pt "MS Shell Dlg 2";
	color: rgb(80, 80, 80);
}
QDateEdit{
	background-color: rgb(223, 223, 223);
	border: 1px solid rgb(95, 158, 195);
	font: 10pt "MS Shell Dlg 2";
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(95, 158, 195);
	border-right: 2px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(95, 158, 195);
	border-radius: 3px;
	padding-left: 3px;
	padding-right: 3px;
	background-color: rgb(225, 225, 225);
}
QDateEdit::drop-down{
	background-color: rgb(215, 215, 215);
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(95, 158, 195);
	border-right: 2px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(95, 158, 195);
	border-radius: 3px;
	subcontrol-origin: margin;
	width: 18px;
}
QDateEdit::down-arrow{
	image: url(:/arrows/Images/arrow-dwn.png);
	width: 14 px;
	height:14 px;
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
	background-color: qlineargradient(spread:pad, x1:0.50035, y1:1, x2:0.5, y2:0, stop:0 rgba(151, 151, 151, 255), stop:1 rgba(255, 255, 255, 255));
	border: 1px solid black;
	border-radius: 3px;
	padding: 2 10px;
	subcontrol-origin: margin;
	subcontrol-position: top;
	font: 11pt "Corbel";
	font-weight: bold;
}
QLineEdit{
	border: 1px solid rgb(95, 158, 195);
	font: 10pt "MS Shell Dlg 2";
}
QLineEdit[readOnly="true"]{
	background-color: rgb(200, 200, 200);
	border: 1px solid rgb(95, 158, 195);
	font: 10pt "MS Shell Dlg 2";
}
QTextEdit{
	font: 12pt "Corbel";
}
QStatusBar{
	font: 10pt "MS Shell Dlg 2";
}
QPushButton{
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(95, 158, 195);
	border-right: 2px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(95, 158, 195);
	border-radius: 4px;
	padding: 2px;
	padding-left: 13px;
	padding-right: 13px;
	background-color: rgb(225, 225, 225);
	font: 11pt "Corbel";
	font-weight: bold;
}
QPushButton::hover{
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(95, 158, 195);
	border-right: 2px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(95, 158, 195);
	border-radius: 4px;
	padding: 2px;
	padding-left: 13px;
	padding-right: 13px;
	background-color: rgb(215, 215, 215);
	font: 11pt "Corbel";
	font-weight: bold;
}
QPushButton::pressed{
	border-bottom: 1px solid rgb(75, 124, 154);
	border-top: 2px solid rgb(95, 158, 195);
	border-right: 1px solid rgb(75, 124, 154);
	border-left: 2px solid rgb(95, 158, 195);
	border-radius: 4px;
	padding: 2px;
	padding-left: 10px;
	padding-right: 10px;
	width: 80px;
	background-color: rgb(225, 225, 225);
	font: 11pt "Corbel";
	font-weight: bold;
}
QComboBox{
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(75, 124, 154);
	border-right: 1px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(75, 124, 154);
	border-radius: 3px;
	background-color: rgb(225, 225, 225);
}
QComboBox::drop-down{
	background-color: rgb(215, 215, 215);
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(95, 158, 195);
	border-right: 2px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(95, 158, 195);
	border-radius: 3px;
	subcontrol-origin: margin;
	width: 16px;
}
QComboBox::drop-down::hover{
	background-color: rgb(205, 205, 205);
	border-bottom: 2px solid rgb(75, 124, 154);
	border-top: 1px solid rgb(95, 158, 195);
	border-right: 2px solid rgb(75, 124, 154);
	border-left: 1px solid rgb(95, 158, 195);
	border-radius: 3px;
	subcontrol-origin: margin;
	width: 16px;
}
QComboBox::drop-down::pressed{
	background-color: rgb(215, 215, 215);
	border-bottom: 1px solid rgb(75, 124, 154);
	border-top: 2px solid rgb(95, 158, 195);
	border-right: 1px solid rgb(75, 124, 154);
	border-left: 2px solid rgb(95, 158, 195);
	border-radius: 3px;
	subcontrol-origin: margin;
	width: 16px;
}
QComboBox::down-arrow{
	image: url(:/arrows/Images/arrow-dwn.png);
	width: 14 px;
	height:14 px;
}
QCalendarWidget QWidget#qt_calendar_navigationbar{
	background-color: qlineargradient(spread:pad, x1:0.50035, y1:1, x2:0.5, y2:0, stop:0 rgba(151, 151, 151, 255), stop:1 rgba(255, 255, 255, 255));
	border-top: 1px solid black;
	border-left: 1px solid black;
	border-right: 1px solid black;
	border-top-left-radius: 3px;
	border-top-right-radius: 3px;
	font: 11pt "Corbel";
	font-weight: bold;
}
QCalendarWidget QToolButton{
	color: rgb(0, 0, 0);
  	icon-size: 20px, 20px;
}
QCalendarWidget QWidget#qt_calendar_prevmonth{
	qproperty-icon: url(:/arrows/Images/arrow-left.png);
}

QCalendarWidget QWidget#qt_calendar_nextmonth{
	qproperty-icon: url(:/arrows/Images/arrow-right.png);
}
QCalendarWidget QSpinBox{ 
	font: 11pt "Corbel";
	font-weight: bold;
}
QCalendarWidget QMenu{
	font: 11pt "Corbel";
	font-weight: bold;
}
QCalendarWidget QWidget{
	alternate-background-color: rgb(234, 234, 234);
}
QCalendarWidget QAbstractItemView:enabled{
	font: 12pt "Corbel";
	font-weight: bold;
	background-color: rgb(214, 214, 214);
  	selection-background-color: rgb(64, 64, 64);
	selection-color: rgb(255, 255, 255);
	border: 1px solid black;
	border-bottom-left-radius: 3px;
	border-bottom-right-radius: 3px;
}
QCalendarWidget QAbstractItemView:disabled{
	color: rgb(64, 64, 64); 
}
"""
