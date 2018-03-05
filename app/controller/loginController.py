# -*- coding: utf-8 -*-

from PyQt4 import QtGui

import requests
import json
from view import loginView


class Main(QtGui.QDialog, loginView.Ui_LoginDialog):
    def __init__(self, tray, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.tray = tray

        self.btn_login.clicked.connect(self.login)

    def login(self):
        username = str(self.le_username.text())
        password = str(self.le_password.text())

        if not username or not password:
            QtGui.QMessageBox.critical(self, 'Campos não preenchidos'.decode('utf-8'), 'Preencha todos os campos corretamente!', QtGui.QMessageBox.Ok)
            return

        try:
            r = requests.post('http://localhost:8000/api/user', {'username': username, 'password': password})
        except requests.ConnectionError:
            QtGui.QMessageBox.critical(self, 'Erro'.decode('utf-8'), 'Erro ao se conectar com o servidor!', QtGui.QMessageBox.Ok)
            return

        if not json.loads(r.content)['auth']:
            QtGui.QMessageBox.critical(self, 'Erro', 'Usuário ou senha incorreto!'.decode('utf-8'), QtGui.QMessageBox.Ok)
            return

        self.tray.show()
        self.parent.show()
        self.close()
