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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_upload = QtGui.QPushButton(self.centralwidget)
        self.btn_upload.setGeometry(QtCore.QRect(330, 210, 99, 27))
        self.btn_upload.setDefault(True)
        self.btn_upload.setObjectName(_fromUtf8("btn_upload"))
        self.lb_selecione = QtGui.QLabel(self.centralwidget)
        self.lb_selecione.setGeometry(QtCore.QRect(210, 90, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_selecione.setFont(font)
        self.lb_selecione.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_selecione.setObjectName(_fromUtf8("lb_selecione"))
        self.lb_title = QtGui.QLabel(self.centralwidget)
        self.lb_title.setGeometry(QtCore.QRect(190, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_title.setFont(font)
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_title.setObjectName(_fromUtf8("lb_title"))
        self.bt_open = QtGui.QToolButton(self.centralwidget)
        self.bt_open.setGeometry(QtCore.QRect(240, 120, 30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../instaquiet/docs/logo/open_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_open.setIcon(icon)
        self.bt_open.setObjectName(_fromUtf8("bt_open"))
        self.lb_filename = QtGui.QLabel(self.centralwidget)
        self.lb_filename.setGeometry(QtCore.QRect(280, 120, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_filename.setFont(font)
        self.lb_filename.setText(_fromUtf8(""))
        self.lb_filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_filename.setObjectName(_fromUtf8("lb_filename"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(177, 170, 261, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btn_cancelar = QtGui.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(190, 210, 99, 27))
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        APP_ICON = QtGui.QIcon()
        BT_ICON = QtGui.QIcon()
        APP_ICON.addFile(self.resource_path('docs/icon/fav.ico'), QtCore.QSize(60, 60))
        BT_ICON.addPixmap(QtGui.QPixmap(self.resource_path("docs/icon/open_file.png")), QtGui.QIcon.Normal,
                          QtGui.QIcon.Off)

        MainWindow.setWindowTitle(_translate("MainWindow", "Decorado", None))
        MainWindow.setWindowIcon(APP_ICON)
        self.bt_open.setIcon(BT_ICON)

        self.btn_upload.setText(_translate("MainWindow", "Upload", None))
        self.btn_upload.setShortcut(_translate("MainWindow", "Return", None))
        self.lb_selecione.setText(_translate("MainWindow", "Selecione o arquivo", None))
        self.lb_title.setText(_translate("MainWindow", "Decorado App", None))
        self.bt_open.setText(_translate("MainWindow", "...", None))
        self.btn_cancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = ''

        return os.path.join(base_path, relative_path)

