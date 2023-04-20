import sqlite3
from PyQt5 import QtWidgets
import mainWindow
from GenaBooking import perehod

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)''')
db.commit()

for i in cursor.execute('SELECT * FROM users'):
    print(i)


class Registration(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.label_3.setText('')
        self.label_2.setText('Регистрация')
        self.lineEdit.setPlaceholderText('Введите Логин')
        self.lineEdit_2.setPlaceholderText('Введите Пароль')
        self.pushButton.setText('Регистрация')
        self.pushButton_2.setText('Вход')
        self.setWindowTitle('Регистрация')

        self.pushButton.pressed.connect(self.reg)
        self.pushButton_2.pressed.connect(self.login)

    def login(self):
        self.login = Login()
        self.login.show()
        self.hide()

    def reg(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES ("{user_login}", "{user_password}")')
            self.label_3.setText(f'Аккаунт {user_login} успешно зарегистрирован!')
            db.commit()
        else:
            self.label_3.setText('Такой аккаунт уже имеется!')


class Login(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.label_3.setText('')
        self.label_2.setText('Вход в аккаунт')
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')
        self.pushButton.setText('Вход')
        self.pushButton_2.setText('Регистрация')
        self.setWindowTitle('Вход')

        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.reg)

    def reg(self):
        self.reg = Registration()
        self.reg.show()
        self.hide()

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
        check_pass = cursor.fetchall()

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()

        if check_pass[0][0] == user_password and check_login[0][0] == user_login:
            self.openWindow()
            # self.label_3.setText('Успешная авторизация!')


        else:
            self.label_3.setText('Неправельный логин или пароль...')


class Perehod(QtWidgets.QWidget, perehod.Ui_Form):
    def __init__(self):
        super(Perehod, self).__init__()
        self.pushButton.setText('Записаться')
        self.pushButton_2.setText('Мои Записи')
        self.pushButton_3.setText('Exit')
        self.setWindowTitle('GenaBooking')





App = QtWidgets.QApplication([])
window = Login()
window.show()
App.exec()