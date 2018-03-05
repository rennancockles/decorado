# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

import requests
from os import path
from view import mainView


class Upload(QtCore.QThread):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.parent = parent
        self.file = parent.file
        self.stop_thread = False

    def run(self):
        pgr = 0
        step = 10000
        url = 'http://localhost:8000/api/upload'
        files = {'docfile': open(self.file['path'], 'rb')}

        r = requests.post(url, files=files)

        while pgr < self.file['size']:
            if self.stop_thread:
                self.terminate()
                self.emit(QtCore.SIGNAL('sigUPDATE(QString)'), '0')

            pgr += step
            value = 100*pgr/self.file['size']

            if value >= 100:
                break

            self.emit(QtCore.SIGNAL('sigUPDATE(QString)'), str(value))
            self.sleep(1)

        self.emit(QtCore.SIGNAL('sigUPDATE(QString)'), '100')


class Main(QtGui.QMainWindow, mainView.Ui_MainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

        self.file = {}
        self.up_thread = None

        self.bt_open.clicked.connect(self.open_file)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_upload.clicked.connect(self.upload)

    def update_progress(self, value):
        self.progressBar.setProperty("value", value)

    def thread_done(self):
        self.lb_filename.clear()
        self.file = {}
        self.up_thread = None

    def upload(self):
        if not self.file:
            QtGui.QMessageBox.critical(self, 'Nenhum arquivo selecionado'.decode('utf-8'), 'Selecione um arquivo para fazer upload', QtGui.QMessageBox.Ok)
            return

        self.up_thread = Upload(parent=self)
        self.connect(self.up_thread, QtCore.SIGNAL('sigUPDATE(QString)'), self.update_progress)
        self.connect(self.up_thread, QtCore.SIGNAL('finished()'), self.thread_done)
        self.up_thread.start()

    def cancelar(self):
        if self.up_thread:
            self.up_thread.stop_thread = True
        self.lb_filename.clear()
        self.progressBar.setProperty("value", 0)
        self.file = {}

    def open_file(self):
        self.progressBar.setProperty("value", 0)
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Arquivo', '', '')

        if not fname:
            return

        self.file['name'] = path.basename(str(fname))
        self.file['path'] = str(fname)
        self.file['size'] = path.getsize(fname)

        self.lb_filename.setText(self.file['name'])

    def closeEvent(self, event):
        event.ignore()
        self.hide()
