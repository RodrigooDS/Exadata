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

class Ui_MainInfluyentes(object):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""
    def setupUi(self, MainBD):
        MainBD.setObjectName("MainBD")
        MainBD.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainBD)
        self.centralwidget.setObjectName("centralwidget")

        #inicio tabla 1
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        # formato tabla posx,posy,tamx,tamy
        self.tabla.setGeometry(QtCore.QRect(10, 40, 510, 250))
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

        # inicio tabla_popularidad
        self.tabla_popularidad = QtWidgets.QTableWidget(self.centralwidget)
        # formato tabla_popularidad posx,posy,tamx,tamy
        self.tabla_popularidad.setGeometry(QtCore.QRect(10, 310, 510, 250))
        self.tabla_popularidad.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla_popularidad.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla_popularidad.setColumnCount(2)
        self.tabla_popularidad.setObjectName("tabla_popularidad")
        self.tabla_popularidad.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(1, item)
        self.tabla_popularidad.horizontalHeader().setDefaultSectionSize(250)
        self.tabla_popularidad.horizontalHeader().setStretchLastSection(True)
        self.tabla_popularidad.verticalHeader().setStretchLastSection(False)
        self.tabla_popularidad.cellClicked.connect(self.ConsultarFecha)
        # fin tabla_popularidad

        # BOTONES
        # boton exportar_bd
        self.bt_exportar_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd.setGeometry(QtCore.QRect(720, 380, 100, 20))
        self.bt_exportar_bd.setObjectName("bt_exportar_bd")
        self.bt_exportar_bd.clicked.connect(self.Exportar_Influencer)

        # boton resultado
        self.resultado = QtWidgets.QPushButton(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(550, 380, 100, 20))
        self.resultado.setObjectName("resultado")
        self.resultado.clicked.connect(self.Mostrar_Influencer)

        # boton exportar_bd2
        self.bt_exportar_bd2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd2.setGeometry(QtCore.QRect(720, 510, 100, 20))
        self.bt_exportar_bd2.setObjectName("bt_exportar_bd2")
        self.bt_exportar_bd2.clicked.connect(self.Exportar_Publicaciones)

        # boton resultado2
        self.resultado2 = QtWidgets.QPushButton(self.centralwidget)
        self.resultado2.setGeometry(QtCore.QRect(550, 510, 100, 20))
        self.resultado2.setObjectName("resultado2")
        self.resultado2.clicked.connect(self.Mostrar_Publicaciones)



        #=================================================================================
        MainBD.setCentralWidget(self.centralwidget)


        #CALENDARIO
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(550, 50, 312, 183))
        self.calendario.setStyleSheet("")
        self.calendario.setStyleSheet("alternate-background-color: rgb(118, 148, 255);")
        self.calendario.setObjectName("calendario")

        #LABEL
        self.label_INFLUENCIADORES = QtWidgets.QLabel(self.centralwidget)
        self.label_INFLUENCIADORES.setGeometry(QtCore.QRect(550, 310, 121, 20))
        self.label_INFLUENCIADORES.setObjectName("label_INFLUENCIADORES")

        self.label_PUBLICACIONES = QtWidgets.QLabel(self.centralwidget)
        self.label_PUBLICACIONES.setGeometry(QtCore.QRect(550, 440, 190, 20))
        self.label_PUBLICACIONES.setObjectName("label_PUBLICACIONES")


        #TEXTO
        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(550, 350, 110, 22))
        self.fechaInicio.setObjectName("fechaInicio")
        self.fechaInicio.setCalendarPopup(True)
        self.fechaTermino = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino.setGeometry(QtCore.QRect(720, 350, 110, 22))
        self.fechaTermino.setObjectName("fechaTermino")
        self.fechaTermino.setCalendarPopup(True)
        self.fechaInicio.setDate(QtCore.QDate.currentDate())
        self.fechaTermino.setDate(QtCore.QDate.currentDate())

        self.incioLetra = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra.setGeometry(QtCore.QRect(550, 330, 111, 16))
        self.incioLetra.setObjectName("incioLetra")
        self.terminoLetra = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra.setGeometry(QtCore.QRect(720, 330, 111, 16))
        self.terminoLetra.setObjectName("terminoLetra")

        # TEXTO3
        self.fechaInicio2 = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio2.setGeometry(QtCore.QRect(550, 480, 110, 22))
        self.fechaInicio2.setObjectName("fechaInicio1")
        self.fechaInicio2.setCalendarPopup(True)
        self.fechaTermino2 = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino2.setGeometry(QtCore.QRect(720, 480, 110, 22))
        self.fechaTermino2.setObjectName("fechaTermino1")
        self.fechaTermino2.setCalendarPopup(True)
        self.fechaInicio2.setDate(QtCore.QDate.currentDate())
        self.fechaTermino2.setDate(QtCore.QDate.currentDate())

        self.incioLetra4 = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra4.setGeometry(QtCore.QRect(550, 460, 111, 16))
        self.incioLetra4.setObjectName("incioLetra2")
        self.terminoLetra4 = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra4.setGeometry(QtCore.QRect(720, 460, 111, 16))
        self.terminoLetra4.setObjectName("terminoLetra2")

        # BARRA MENU
        self.menubar = QtWidgets.QMenuBar(MainBD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        MainBD.setWindowTitle(_translate("MainBD", "POPULARIDAD"))

        #inicio tabla
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("MainBD", "NOMBRE"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("MainBD", "FECHA DESDE"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("MainBD", "FECHA HASTA"))
        item = self.tabla.horizontalHeaderItem(3)
        item.setText(_translate("MainBD", "TWEETS"))

        #fin tabla

        # inicio tabla_popularidad
        item = self.tabla_popularidad.horizontalHeaderItem(0)
        item.setText(_translate("MainBD", "NOMBRE USUARIO"))
        item = self.tabla_popularidad.horizontalHeaderItem(1)
        item.setText(_translate("MainBD", "CANTIDAD RETWEETS / PUBLICACIONES"))
        # fin tabla_popularidad

        #LABEL
        self.incioLetra.setText(_translate("MainBD", "FECHA INICIO"))
        self.terminoLetra.setText(_translate("MainBD", "FECHA TERMINO"))

        self.incioLetra4.setText(_translate("MainBD", "FECHA INICIO"))
        self.terminoLetra4.setText(_translate("MainBD", "FECHA TERMINO"))

        self.label_INFLUENCIADORES.setText(_translate("MainBD", "INFLUENCIADORES"))
        self.label_PUBLICACIONES.setText(_translate("MainBD", "USUARIO CON MAS PUBLICACIONES"))


        self.bt_exportar_bd.setText(_translate("MainBD", "EXPORTAR"))
        self.resultado.setText(_translate("MainBD", "RESULTADO"))

        self.bt_exportar_bd2.setText(_translate("MainBD", "EXPORTAR"))
        self.resultado2.setText(_translate("MainBD", "RESULTADO"))

        # BARRA MENU
        self.Programas.setTitle(_translate("MainBD", "Programas"))
        self.BaseDeDatos.setText(_translate("MainBD", "Salir"))
        self.BaseDeDatos.triggered.connect(exit)

        self.Ayuda.setTitle(_translate("MainBD", "Ayuda"))
        self.SobreQue.setText(_translate("MainBD", "Sobre Que"))
        # self.SobreQue.triggered.connect(exit)





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
            self.tabla.setRowCount(index + 1)
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
        self.fechaInicio2.setDate(QtCore.QDate(int(year), int(month), int(day)))

        year = f_hasta[6:10]
        day = f_hasta[0:2]
        month = f_hasta[3:5]
        # print(month)
        self.fechaTermino.setDate(QtCore.QDate(int(year), int(month), int(day)))
        self.fechaTermino2.setDate(QtCore.QDate(int(year), int(month), int(day)))

    def Mostrar_Influencer(self):
        base = self.tabla.selectedItems()[0].text()
        fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")

        index = 0
        query = 'select retweet_screen_name USUARIO,count(retweet_screen_name) CANTIDAD from ' +base+ ' ' \
                'where is_retweet  = "TRUE" and created_at between ("'+fecha_inicio+' 00:00:00") and ("'+fecha_termino+' 23:59:59") group by retweet_screen_name order by count(retweet_screen_name) desc'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tabla_popularidad.setRowCount(index + 1)
            self.tabla_popularidad.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla_popularidad.setItem(index, 1, QTableWidgetItem(str(row[1])))
            index += 1
        QMessageBox.warning(self.centralwidget, "TABLA INFLUENCER TERMINADA", "TABLA INFLUENCER TERMINADA.")

    def Exportar_Influencer(self):
        base = self.tabla.selectedItems()[0].text()
        fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()

        cur.execute('select retweet_screen_name USUARIO,count(retweet_screen_name) CANTIDAD from ' +base+ ' ' \
                'where is_retweet  = "TRUE" and created_at between ("'+fecha_inicio+' 00:00:00") and ("'+fecha_termino+' 23:59:59") group by retweet_screen_name order by count(retweet_screen_name) desc')
        with open(base+"_INFLUENCER" + ".csv", "w", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur.fetchall())
        sql.close()
        self.Mostrar_Influencer()
        QMessageBox.warning(self.centralwidget, "EXPORTACION INFLUENCER TERMINADA", "EXPORTACION TABLA INFLUENCER TERMINADA.")

    def Mostrar_Publicaciones(self):
        base = self.tabla.selectedItems()[0].text()
        fecha_inicio = self.fechaInicio2.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino2.date().toString("yyyy-MM-dd")

        index = 0
        #CAMBIAR CONSULTA POR MAS CANTIDAD DE PUBLICACIONES!!!!!!!!!!!!!!!!!
        query = 'select screen_name USUARIO,count(screen_name) CANTIDAD from ' +base+ ' where is_retweet="TRUE" and created_at between ("'+fecha_inicio+' 00:00:00") and ("'+fecha_termino+' 23:59:59") group by screen_name order by count(screen_name) desc'
        ###################################
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tabla_popularidad.setRowCount(index + 1)
            self.tabla_popularidad.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla_popularidad.setItem(index, 1, QTableWidgetItem(str(row[1])))
            index += 1
        QMessageBox.warning(self.centralwidget, "TABLA MAYOR PUBLICACIONES TERMINADA", "TABLA MAYOR PUBLICACIONES TERMINADA.")

    def Exportar_Publicaciones(self):
        base = self.tabla.selectedItems()[0].text()
        fecha_inicio = self.fechaInicio2.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino2.date().toString("yyyy-MM-dd")
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()
        #CAMBIAR CONSULTA POR MAS CANTIDAD DE PUBLICACIONES!!!!!!!!!!!!!!!!!
        cur.execute('select screen_name USUARIO,count(screen_name) CANTIDAD from ' +base+ ' where is_retweet="TRUE" and created_at between ("'+fecha_inicio+' 00:00:00") and ("'+fecha_termino+' 23:59:59") group by screen_name order by count(screen_name) desc')
        ###################################
        with open(base+"_MASPUBLICACIONES" + ".csv", "w", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur.fetchall())
        sql.close()
        self.Mostrar_Publicaciones()
        QMessageBox.warning(self.centralwidget, "EXPORTACION MAYOR PUBLICACIONES TERMINADA", "EXPORTACION MAYOR PUBLICACIONES TERMINADA.")

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


