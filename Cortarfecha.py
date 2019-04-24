# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BD.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QComboBox, QStyleFactory, QListWidget, \
    QTableWidget, QTableWidgetItem, QListWidgetItem

import sqlite3
import csv
import sys
import datetime

class Ui_MainCortar(object):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""
    def setupUi(self, MainBD):
        MainBD.setObjectName("MainBD")
        MainBD.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainBD)
        self.centralwidget.setObjectName("centralwidget")

        #inicio tabla
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        # formato tabla posx,posy,tamx,tamy
        self.tabla.setGeometry(QtCore.QRect(10, 30, 510, 400))
        self.tabla.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla.setColumnCount(4)
        self.tabla.setObjectName("tabla")
        self.tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(3, item)
        self.tabla.horizontalHeader().setDefaultSectionSize(120)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setStretchLastSection(False)
        self.tabla.cellClicked.connect(self.ConsultarFecha)
        #fin tabla

        # BOTONES
        # boton exportar_bd
        self.bt_exportar_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd.setGeometry(QtCore.QRect(550, 300, 100, 20))
        self.bt_exportar_bd.setObjectName("bt_exportar_bd")
        self.bt_exportar_bd.clicked.connect(self.Exportar_Fecha)

        #=================================================================================
        MainBD.setCentralWidget(self.centralwidget)

        #CALENDARIO
        # formato tabla posx,posy,tamx,tamy
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(550, 40, 312, 183))
        self.calendario.setStyleSheet("")
        self.calendario.setStyleSheet("alternate-background-color: rgb(118, 148, 255);")
        self.calendario.setObjectName("calendario")

        #LABEL MUESTRA POR FECHA
        self.label_muestraFecha = QtWidgets.QLabel(self.centralwidget)
        self.label_muestraFecha.setGeometry(QtCore.QRect(550, 230, 121, 16))
        self.label_muestraFecha.setObjectName("label_muestraFecha")

        #LABEL MUESTRA DE TODA LA BASE
        self.label_muestraToda = QtWidgets.QLabel(self.centralwidget)
        self.label_muestraToda.setGeometry(QtCore.QRect(550, 360, 200, 16))
        self.label_muestraToda.setObjectName("label_muestraToda")

        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(550, 270, 120, 22))
        self.fechaInicio.setObjectName("fechaInicio")
        self.fechaInicio.setCalendarPopup(True)
        self.fechaTermino = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino.setGeometry(QtCore.QRect(720, 270, 120, 22))
        self.fechaTermino.setObjectName("fechaTermino")
        self.fechaTermino.setCalendarPopup(True)
        self.fechaInicio.setDate(QtCore.QDate.currentDate())
        self.fechaTermino.setDate(QtCore.QDate.currentDate())

        self.incioLetra = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra.setGeometry(QtCore.QRect(550, 250, 121, 16))
        self.incioLetra.setObjectName("incioLetra")
        self.terminoLetra = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra.setGeometry(QtCore.QRect(720, 250, 121, 16))
        self.terminoLetra.setObjectName("terminoLetra")

        # BARRA MENU
        self.menubar = QtWidgets.QMenuBar(MainBD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")

        self.Programas = QtWidgets.QMenu(self.menubar)
        self.BaseDeDatos = QtWidgets.QAction(MainBD)
        self.menubar.addAction(self.Programas.menuAction())
        self.Programas.addAction(self.BaseDeDatos)

        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.SobreQue = QtWidgets.QAction(MainBD)
        self.menubar.addAction(self.Ayuda.menuAction())
        self.Ayuda.addAction(self.SobreQue)


        self.retranslateUi(MainBD)
        QtCore.QMetaObject.connectSlotsByName(MainBD)

        #new table
        self.CargarTabla()


    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("MainBD", "Cortar Fecha"))

        # BARRA MENU
        self.Programas.setTitle(_translate("MainBD", "Programas"))
        self.BaseDeDatos.setText(_translate("MainBD", "Salir"))
        self.BaseDeDatos.triggered.connect(exit)

        self.Ayuda.setTitle(_translate("MainBD", "Ayuda"))
        self.SobreQue.setText(_translate("MainBD", "Sobre Que"))
        # self.SobreQue.triggered.connect(exit)

        #inicio tabla
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("MainBD", "NOMBRE"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("MainBD", "FECHA DESDE"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("MainBD", "FECHA HASTA"))
        item = self.tabla.horizontalHeaderItem(3)
        item.setText(_translate("MainBD", "TWEETS"))
        self.incioLetra.setText(_translate("MainBD", "FECHA INICIO"))
        self.terminoLetra.setText(_translate("MainBD", "FECHA TERMINO"))
        #fin tabla

        #LABEL
        self.label_muestraFecha.setText(_translate("MainBD", "CORTAR POR FECHA"))
        #self.label_muestraToda.setText(_translate("MainBD", "MUESTRA POR CANTIDAD DE TWEETS"))




        self.bt_exportar_bd.setText(_translate("MainBD", "EXPORTAR"))
        #self.bt_exportar_bd2.setText(_translate("MainBD", "EXPORTAR"))



    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result


    def CargarTabla(self):
        index = 0
        query = 'SELECT tbl_name FROM sqlite_master WHERE type = "table"'
        db_rows = self.run_query(query)
        for row in db_rows:
            #print(row)
            self.tabla.setRowCount(index + 1)
            #query = 'SELECT min(created_at),max(created_at) from ' + row[0]
            query = "SELECT strftime('%d-%m-%Y',min(created_at)),strftime('%d-%m-%Y',max(created_at)),count(*) from " + row[0]
            db_rows2 = self.run_query(query)
            for row2 in db_rows2:
                self.tabla.setItem(index, 0, QTableWidgetItem(row[0]))
                self.tabla.setItem(index, 1, QTableWidgetItem(row2[0]))
                self.tabla.setItem(index, 2, QTableWidgetItem(row2[1]))
                self.tabla.setItem(index, 3, QTableWidgetItem(str(row2[2])))
                index += 1

    def ConsultarFecha(self):
        #tabla = self.tabla.selectedItems()[0].text()
        #tabla = self.tabla.selectedItems()[3].text()
        a = self.tabla.currentRow()
        self.tabla.selectRow(a)
        #b = self.tabla.currentColumn()
        f_desde = self.tabla.item(a,1).text()

        f_hasta = self.tabla.item(a,2).text()
        year = f_desde[6:10]
        day = f_desde[0:2]
        month = f_desde[3:5]
        #print(month)
        self.fechaInicio.setDate(QtCore.QDate(int(year),int(month),int(day)))

        year = f_hasta[6:10]
        day = f_hasta[0:2]
        month = f_hasta[3:5]
        # print(month)
        self.fechaTermino.setDate(QtCore.QDate(int(year), int(month), int(day)))


    def Exportar_Fecha(self):
        base = self.tabla.selectedItems()[0].text()
        fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()

        cur.execute("select * from "+base+" where created_at BETWEEN ('"+fecha_inicio+" 00:00:00') and ('"+fecha_termino+" 23:59:59') order by created_at asc")
        with open(base+"_CORTAR" + ".csv", "w", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur.fetchall())
        QMessageBox.warning(self.centralwidget, "EXPORTACION CORTE LISTA", "EXPORTACION DE CORTE DE FECHA TERMINADA.")
        sql.close()

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBD = QtWidgets.QMainWindow()
    ui = Ui_MainBD()
    ui.setupUi(MainBD)
    MainBD.show()
    sys.exit(app.exec_())


