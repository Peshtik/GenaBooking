from PyQt5 import QtCore, QtGui, QtWidgets
from otherWindow import Ui_OtherWindow


class Ui_MainWindow(object):
    def openWindow(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 572)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(53, 3, 127);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 320, 271, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
" \n"
"    background-color: rgb(85, 170, 255);\n"
"    color:white;\n"
"    border: 3px solid #ff5500;\n"
"    border-radius: 12;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(115, 255, 239);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 255);}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 420, 171, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
" \n"
"    background-color: rgb(85, 170, 255);\n"
"    color:white;\n"
"    border: 3px solid #ff5500;\n"
"    border-radius: 12;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(115, 255, 239);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 85, 255);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 170, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:12;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 240, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(0, 0, 0);\n"
"border-radius:12;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 331, 51))
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 500, 301, 41))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "EGOR BOOKING.COM"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">TextLabel</span></p></body></html>"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())