# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from poster.encode import multipart_encode
import requests
from os import path
from view import mainView


class IterableToFileAdapter(object):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.length = iterable.total

    def read(self, size=-1):
        return next(self.iterator, b'')

    def __len__(self):
        return self.length


class Upload(QtCore.QThread):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.parent = parent
        self.file = parent.file
        self.stop_thread = False

    def multipart_encode_for_requests(self, params, boundary=None, cb=None):
        datagen, headers = multipart_encode(params, boundary, cb)
        return IterableToFileAdapter(datagen), headers

    def progress(self, param, current, total):
        if not param:
            return

        if self.stop_thread:
            self.setTerminationEnabled(True)
            self.emit(QtCore.SIGNAL('sigUPDATE(QString)'), '0')
            self.terminate()
            return

        percent = str(current * 100 / total)
        self.emit(QtCore.SIGNAL('sigUPDATE(QString)'), percent)

    def run(self):
        url = 'http://localhost:8000/api/upload'
        file = {'docfile': open(self.file['path'], 'rb')}
        datagen, headers = self.multipart_encode_for_requests(file, cb=self.progress)

        r = requests.post(url, data=datagen, headers=headers)

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
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Arquivo', '', '').toUtf8()
        filename = str(fname).decode('utf8', 'ignore')

        if not fname:
            return

        self.file['name'] = path.basename(filename)
        self.file['path'] = filename
        self.file['size'] = path.getsize(filename)

        self.lb_filename.setText(self.file['name'])

    def closeEvent(self, event):
        event.ignore()
        self.hide()
