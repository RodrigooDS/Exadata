# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EXADATA.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from pprint import pprint
from BD import Ui_MainBD
from Muestra import Ui_MainBD
import logo_rc
import sys

class INDEX(object):
    def setupUi(self, EXADATA):
        #TITULO DE VENTANA
        EXADATA.setObjectName("EXADATA")
        #TAMAÑO DE VENTANA
        EXADATA.resize(800, 600)


        #LOGO
        self.centralwidget = QtWidgets.QWidget(EXADATA)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 0, 435, 351))
        self.label.setStyleSheet("border-image: url(:/cct/logo.png);")
        EXADATA.setCentralWidget(self.centralwidget)

        #CUADRO TEXTO
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(270, 285, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        EXADATA.setCentralWidget(self.centralwidget)

        #BARRA MENU
        self.menubar = QtWidgets.QMenuBar(EXADATA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

            #BOTON PROGRAMAS
        self.Programas = QtWidgets.QMenu(self.menubar)
        self.BaseDeDatos = QtWidgets.QAction(EXADATA)
        self.Muestra = QtWidgets.QAction(EXADATA)
        self.Programas.addAction(self.BaseDeDatos)
        self.Programas.addAction(self.Muestra)

            #BOTON AYUDA
        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.Sobre_que = QtWidgets.QAction(EXADATA)
        self.Ayuda.addAction(self.Sobre_que)


        EXADATA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EXADATA)
        self.statusbar.setObjectName("statusbar")
        EXADATA.setStatusBar(self.statusbar)
        self.menubar.addAction(self.Programas.menuAction())
        self.menubar.addAction(self.Ayuda.menuAction())

        #FUNCIONES
        self.BARRAMENU(EXADATA)
        self.CUADROTEXTO(EXADATA)
        QtCore.QMetaObject.connectSlotsByName(EXADATA)

    def BARRAMENU(self, EXADATA):
        _translate = QtCore.QCoreApplication.translate
        EXADATA.setWindowTitle(_translate("EXADATA", "MainWindow"))

        self.Programas.setTitle(_translate("EXADATA", "Programas"))
        self.BaseDeDatos.setText(_translate("EXADATA", "BASE DE DATOS"))
        self.Muestra.setText(_translate("EXADATA", "MUESTRA"))

        self.Ayuda.setTitle(_translate("EXADATA", "Ayuda"))
        self.Sobre_que.setText(_translate("EXADATA", "Sobre que"))

        #Funciones de menu
        self.BaseDeDatos.triggered.connect(self.Abrir_BD)
        self.Muestra.triggered.connect(self.Abrir_Muestra)

    def CUADROTEXTO(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("EXADATA", "EXADATA"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            #PARRAFO 1
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\""
                                                #TEXTO PARRAFO 1
                                            ">ExaData es una aplicacion creada con la finalidad de facilitar el manejo de informacion que se encuentra en la red social Twitter.<""/span></p>\n"
                                            
                                            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600; color:#ffaa00;\"><br /></p>\n"
                                            #PARRAFO 2
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\""
                                                #TEXTO PARRAFO 2
                                            ">$$$$$$$$</span></p></body></html>"))

    def Abrir_BD(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_MainBD()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def Abrir_Muestra(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_MainBD()
        self.ui.setupUi(self.ventana)
        self.ventana.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #TEMA
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

    EXADATA = QtWidgets.QMainWindow()
    ui = INDEX()
    ui.setupUi(EXADATA)
    EXADATA.show()
    sys.exit(app.exec_())

