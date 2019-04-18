import sys
from pprint import pprint

from BD import Ui_MainBD
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class Index(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('EXADATA')
        self.statusBar().showMessage('Cargando')
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False) #only for MacOS

        file_menu = menuBar.addMenu('&Programas')
        menu = QAction('&BASE DE DATOS', self)
        menu.setStatusTip('Manejo de bases de datos')
        menu.triggered.connect(self.abrir)
        file_menu.addAction(menu)

        self.setGeometry(300, 300, 800, 600)

    def abrir(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_MainBD()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    index = Index()
    index.show()
    sys.exit(app.exec_())