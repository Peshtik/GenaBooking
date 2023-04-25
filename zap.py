from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 445)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(10, 250, 321, 91))
        self.timeEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 4, 23), QtCore.QTime(10, 0, 0)))
        self.timeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2025, 4, 23), QtCore.QTime(18, 0, 0)))
        self.timeEdit.setMaximumTime(QtCore.QTime(18, 0, 0))
        self.timeEdit.setMinimumTime(QtCore.QTime(10, 0, 0))
        self.timeEdit.setTime(QtCore.QTime(10, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(10, 110, 321, 121))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Sans Serif\";\n"
"color: rgb(0, 0, 0);")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 9, 23), QtCore.QTime(10, 0, 0)))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2025, 12, 31), QtCore.QTime(18, 0, 0)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 9, 23), QtCore.QTime(10, 0, 0)))
        self.dateEdit.setMinimumTime(QtCore.QTime(10, 0, 0))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 271, 61))
        self.label.setStyleSheet("\n"
"    color:white;\n"
"    border: 3px solid #ff5500;\n"
"    border-radius: 12;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 380, 201, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border: 4px solid rgb(170, 0, 0) ;\n"
"border-color: 13;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 255, 255);}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 127);}\n"
"")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Выберете дату и время</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
