# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(400, 300)
        LoginDialog.setMinimumSize(QtCore.QSize(400, 300))
        LoginDialog.setMaximumSize(QtCore.QSize(400, 300))
        LoginDialog.setModal(True)
        self.le_password = QtGui.QLineEdit(LoginDialog)
        self.le_password.setGeometry(QtCore.QRect(170, 160, 141, 25))
        self.le_password.setEchoMode(QtGui.QLineEdit.Password)
        self.le_password.setObjectName(_fromUtf8("le_password"))
        self.btn_login = QtGui.QPushButton(LoginDialog)
        self.btn_login.setGeometry(QtCore.QRect(150, 210, 99, 27))
        self.btn_login.setDefault(True)
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.lb_username = QtGui.QLabel(LoginDialog)
        self.lb_username.setGeometry(QtCore.QRect(50, 130, 101, 25))
        self.lb_username.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_username.setObjectName(_fromUtf8("lb_username"))
        self.lb_password = QtGui.QLabel(LoginDialog)
        self.lb_password.setGeometry(QtCore.QRect(50, 160, 101, 25))
        self.lb_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_password.setObjectName(_fromUtf8("lb_password"))
        self.le_username = QtGui.QLineEdit(LoginDialog)
        self.le_username.setGeometry(QtCore.QRect(170, 130, 141, 25))
        self.le_username.setObjectName(_fromUtf8("le_username"))
        self.lb_title = QtGui.QLabel(LoginDialog)
        self.lb_title.setGeometry(QtCore.QRect(80, 30, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_title.setFont(font)
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_title.setObjectName(_fromUtf8("lb_title"))
        self.lb_username.setBuddy(self.le_username)
        self.lb_password.setBuddy(self.le_password)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.le_username, self.le_password)
        LoginDialog.setTabOrder(self.le_password, self.btn_login)

    def retranslateUi(self, LoginDialog):
        APP_ICON = QtGui.QIcon()
        APP_ICON.addFile(self.resource_path('../docs/icon/fav.ico'), QtCore.QSize(60, 60))

        LoginDialog.setWindowTitle(_translate("MainWindow", "Decorado", None))
        LoginDialog.setWindowIcon(APP_ICON)

        self.btn_login.setText(_translate("LoginDialog", "Login", None))
        self.btn_login.setShortcut(_translate("LoginDialog", "Return", None))
        self.lb_username.setText(_translate("LoginDialog", "Username", None))
        self.lb_password.setText(_translate("LoginDialog", "Password", None))
        self.lb_title.setText(_translate("LoginDialog", "Decorado App", None))
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def resource_path(self, relative_path):
        CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = CURRENT_PATH

        return os.path.join(base_path, relative_path)

