from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction, qApp
from PyQt5 import QtCore, QtGui, QtWidgets
from pprint import pprint
from BD import Ui_MainBD
from Muestra import Ui_MainMUESTRA
from Cortarfecha import Ui_MainCortar
from Influyentes import Ui_MainInfluyentes
from Ayuda import Ui_MainAyuda
import logo_rc
import sys


class  Ui_MainWindow(QMainWindow):

    def setupUI(self):
        # TITULO DE VENTANA
        self.setObjectName("AYUDA")
        # TAMAÑO DE VENTANA
        self.setFixedSize(800,600)

        #LOGO
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 0, 435, 351))
        self.label.setStyleSheet("border-image: url(:/cct/logo.png);")
        self.setCentralWidget(self.centralwidget)

        # CUADRO TEXTO
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 285, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.setCentralWidget(self.centralwidget)

        # BARRA MENU
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        # BOTON PROGRAMAS
        self.Programas = QtWidgets.QMenu(self.menubar)
        self.BaseDeDatos = QtWidgets.QAction(self)
        self.Muestra_Programa = QtWidgets.QAction(self)
        self.Cortar_Fecha = QtWidgets.QAction(self)
        self.Popularidad = QtWidgets.QAction(self)

        self.Programas.addAction(self.BaseDeDatos)
        self.Programas.addAction(self.Muestra_Programa)
        self.Programas.addAction(self.Cortar_Fecha)
        self.Programas.addAction(self.Popularidad)

        # BOTON AYUDA
        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.Sobre_que = QtWidgets.QAction(self)
        self.Ayuda.addAction(self.Sobre_que)

        #self.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(self)
        #self.statusbar.setObjectName("statusbar")
        #self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.Programas.menuAction())
        self.menubar.addAction(self.Ayuda.menuAction())

        # FUNCIONES
        self.BARRAMENU(self)
        self.CUADROTEXTO(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def BARRAMENU(self, EXADATA):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("EXADATA", "MainWindow"))

        self.Programas.setTitle(_translate("EXADATA", "Programas"))
        self.BaseDeDatos.setText(_translate("EXADATA", "Base de dato"))
        self.Muestra_Programa.setText(_translate("EXADATA", "Muestra"))
        self.Cortar_Fecha.setText(_translate("EXADATA", "Cortar fecha"))
        self.Popularidad.setText(_translate("EXADATA", "Popularidad"))


        self.Ayuda.setTitle(_translate("EXADATA", "Ayuda"))
        self.Sobre_que.setText(_translate("EXADATA", "Sobre que"))

        # Funciones de menu
        self.BaseDeDatos.triggered.connect(self.BASE)
        self.Muestra_Programa.triggered.connect(self.MUESTRA)
        self.Cortar_Fecha.triggered.connect(self.CORTAR)
        self.Popularidad.triggered.connect(self.INFLUYENTES)
        self.Sobre_que.triggered.connect(self.AYUDA)


    def CUADROTEXTO(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("EXADATA", "EXADATA"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            # PARRAFO 1
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\""
                                            # TEXTO PARRAFO 1
                                            ">ExaData es una aplicacion creada con la finalidad de facilitar el manejo de informacion que se encuentra en la red social Twitter.<""/span></p>\n"

                                            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600; color:#ffaa00;\"><br /></p>\n"
                                            # PARRAFO 2
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\""
                                            # TEXTO PARRAFO 2
                                            ">$$$$$$$$</span></p></body></html>"))

    def BASE(self):
        self.ventana = Ui_MainWindow()
        self.ui = Ui_MainBD()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def MUESTRA(self):
        self.ventana = Ui_MainWindow()
        self.ui = Ui_MainMUESTRA()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def CORTAR(self):
        self.ventana = Ui_MainWindow()
        self.ui = Ui_MainCortar()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def INFLUYENTES(self):
        self.ventana = Ui_MainWindow()
        self.ui = Ui_MainInfluyentes()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def AYUDA(self):
        self.ventana = Ui_MainWindow()
        self.ui = Ui_MainAyuda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Salir",
                                     "Estas seguro que quieres salir?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # TEMA
    app.setStyle('Windows')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(60, 90, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    window = Ui_MainWindow()
    window.setupUI()
    window.show()
    sys.exit(app.exec_())
