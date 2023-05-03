from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtWidgets


class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 475)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 521, 91))
        self.label.setStyleSheet("\n"
"    color:white;\n"
"    border: 3px solid #ff5500;\n"
"    border-radius: 12;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 390, 451, 61))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: white ;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 3px solid #ff5500;\n"
"    border-radiius:12;}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 127);}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(20, 170, 671, 181))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEdit.setFont(font)
        self.pushButton.pressed.connect(self.getinfo)
        self.dateTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Sans Serif\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.dateTimeEdit.setDate(QtCore.QDate.currentDate())
        self.dateTimeEdit.setTime(QtCore.QTime.currentTime())
        self.dateTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 9, 30), QtCore.QTime(23, 59, 59)))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(10, 0, 0)))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.dateTimeEdit.setCurrentSectionIndex(3)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.TimeZone)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Выберете дату и время</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))



    def getinfo(self):
        # dat = self.dateTimeEdit.date()
        # ti = self.dateTimeEdit.time()
        al = self.dateTimeEdit.dateTime()
        self.insert(al)

    def insert(self, x):
        print(x)











if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
