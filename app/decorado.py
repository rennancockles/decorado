#!/usr/bin/python -B
# -*- coding: utf-8 -*-

import ctypes
import platform
import sys
from ctypes.util import find_library

from PyQt4 import QtGui, QtCore

from controller import loginController, mainController


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.parent = main

        menu = QtGui.QMenu(parent)
        showAction = menu.addAction("Abrir Decorado App")
        menu.addSeparator()
        exitAction = menu.addAction("Sair")
        self.setContextMenu(menu)
        QtCore.QObject.connect(exitAction, QtCore.SIGNAL('triggered()'), self.exit)
        QtCore.QObject.connect(showAction, QtCore.SIGNAL('triggered()'), self.exibir)

    def exit(self):
        QtCore.QCoreApplication.exit()

    def exibir(self):
        if self.parent.isHidden():
            self.parent.show()


if __name__ == '__main__':

    if platform.system() == 'Windows':
        myappid = u'cockles.decorado'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    else:
        libc = ctypes.CDLL(find_library('c'))
        libc.prctl(15, 'decorado')

    app = QtGui.QApplication(sys.argv)

    main = mainController.Main()
    trayIcon = SystemTrayIcon(QtGui.QIcon("docs/icon/decora_512.png"), main)
    login = loginController.Main(trayIcon, main)

    login.show()
    trayIcon.hide()
    main.hide()

    sys.exit(app.exec_())
