# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BD.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
                            QMessageBox, QHBoxLayout, QLabel,QGridLayout, QComboBox, QStyleFactory, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt
import sys


class Ui_MainAyuda(QMainWindow):
    def setupUi(self, MainBD):
        MainBD.setObjectName("MainBD")
        MainBD.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainBD)
        self.centralwidget.setObjectName("centralwidget")
        MainBD.setCentralWidget(self.centralwidget)

        # LOGO
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
        MainBD.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainBD)
        self.CUADROTEXTO(self)
        QtCore.QMetaObject.connectSlotsByName(MainBD)


    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("MainBD", "AYUDA"))

    def CUADROTEXTO(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("EXADATA", "EXADATA"))
        MainBD.textBrowser.setHtml(_translate("MainBD",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            # PARRAFO 1
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\""
                                            # TEXTO PARRAFO 1
                                            ">AQUI VA LA EXPLICACION DE CADA PROGRAMAS MAS UN PEQUEÑO TUTORIAL<""/span></p>\n"

                                            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:600; color:#ffaa00;\"><br /></p>\n"
                                            # PARRAFO 2
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\""
                                            # TEXTO PARRAFO 2
                                            ">AQUI ALGO MAS</span></p></body></html>"))

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Salir",
                                     "Estas seguro que quieres salir de la Ayuda?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBD = QtWidgets.QMainWindow()
    ui = Ui_MainAyuda()
    ui.setupUi(MainBD)
    MainBD.show()
    sys.exit(app.exec_())


