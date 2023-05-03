from PyQt5 import QtCore, QtGui, QtWidgets
from zap import Ui_MainWindow


class Ui_OtherWindow(object):

    def zapisi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        # self.hide()


    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(434, 517)
        OtherWindow.setStyleSheet("background-color: rgb(64, 74, 255);")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.pressed.connect(self.zapisi)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
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
        self.pushButton.setText("Записаться")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 340, 291, 101))
        self.pushButton_2.clicked.connect(OtherWindow.close)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 401, 41))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 230, 291, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Выбор"))
        self.pushButton_2.setText(_translate("OtherWindow", "Выход"))
        self.label.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">GenaBooking<br/></span></p></body></html>"))
        self.pushButton_3.setText(_translate("OtherWindow", "Мои Записи"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())