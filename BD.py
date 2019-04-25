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
import os
import re
from Ayuda import Ui_MainAyuda


import sqlite3
import csv
import sys

class Ui_MainBD(QMainWindow):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""
    def setupUi(self, MainBD):
        MainBD.setObjectName("MainBD")
        MainBD.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainBD)
        self.centralwidget.setObjectName("centralwidget")

        #inicio tabla
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(10, 110, 375, 250))
        self.tabla.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla.setColumnCount(3)
        self.tabla.setObjectName("tabla")
        self.tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, item)
        self.tabla.horizontalHeader().setDefaultSectionSize(120)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setStretchLastSection(False)
        
        #fin tabla

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 70, 151, 16))
        self.label.setObjectName("label")

        #qlineedit nombre base
        self.input_nombre_bd = QtWidgets.QLineEdit(self.centralwidget)
        self.input_nombre_bd.setGeometry(QtCore.QRect(550, 110, 170, 20))
        self.input_nombre_bd.setObjectName("input_nombre_bd")

        # label
        #label nombre_bd
        self.label_nombre_base = QtWidgets.QLabel(self.centralwidget)
        self.label_nombre_base.setGeometry(QtCore.QRect(395, 110, 141, 16))
        self.label_nombre_base.setObjectName("label_nombre_base")
        # label editar_bd
        self.label_editar_bd = QtWidgets.QLabel(self.centralwidget)
        self.label_editar_bd.setGeometry(QtCore.QRect(550, 230, 121, 16))
        self.label_editar_bd.setObjectName("label_editar_bd")

        # BOTONES
        #boton importar
        self.bt_importar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_importar.setGeometry(QtCore.QRect(550, 150, 170, 20))
        self.bt_importar.setObjectName("bt_importar")
        # boton agregar_bd
        self.bt_agregar_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_agregar_bd.setGeometry(QtCore.QRect(550, 260, 170, 20))
        self.bt_agregar_bd.setObjectName("bt_agregar_bd")
        self.bt_agregar_bd.clicked.connect(self.Anadir)
        # boton eliminar_bd
        self.bt_eliminar_bt = QtWidgets.QPushButton(self.centralwidget)
        self.bt_eliminar_bt.setGeometry(QtCore.QRect(550, 290, 170, 20))
        self.bt_eliminar_bt.setObjectName("bt_eliminar_bt")
        self.bt_eliminar_bt.clicked.connect(self.BorrarTabla)
        # boton exportar_bd
        self.bt_exportar_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd.setGeometry(QtCore.QRect(550, 320, 170, 20))
        self.bt_exportar_bd.setObjectName("bt_exportar_bd")
        self.bt_exportar_bd.clicked.connect(self.ExportarBase)
        # boton recarga_bd
        self.bt_recarga_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_recarga_bd.setGeometry(QtCore.QRect(10, 370, 375, 20))
        self.bt_recarga_bd.setObjectName("bt_recarga_bd")
        self.bt_recarga_bd.clicked.connect(self.CargarTabla)

        #=================================================================================
        MainBD.setCentralWidget(self.centralwidget)

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
        MainBD.setWindowTitle(_translate("MainBD", "Base De Datos"))

        # BARRA MENU
        self.Programas.setTitle(_translate("MainBD", "Programas"))
        self.BaseDeDatos.setText(_translate("MainBD", "Salir"))
        #self.BaseDeDatos.triggered.connect()

        self.Ayuda.setTitle(_translate("MainBD", "Ayuda"))
        self.SobreQue.setText(_translate("MainBD", "Sobre Que"))
        self.SobreQue.triggered.connect(self.AYUDA)




        #inicio tabla
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("MainBD", "NOMBRE"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("MainBD", "FECHA DESDE"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("MainBD", "FECHA HASTA"))
        #fin tabla
        self.label.setText(_translate("MainBD", "CREACIÓN DE BASE DE DATOS"))
        self.label_nombre_base.setText(_translate("MainBD", "NOMBRE DE LA NUEVA BASE:"))
        self.bt_importar.setText(_translate("MainBD", "IMPORTAR"))
        self.bt_importar.clicked.connect(self.CargarCSV)

        self.label_editar_bd.setText(_translate("MainBD", "EDITAR BASE DE DATOS"))
        self.bt_agregar_bd.setText(_translate("MainBD", "AGREGAR BASE"))
        self.bt_eliminar_bt.setText(_translate("MainBD", "ELIMINAR BASE"))
        self.bt_exportar_bd.setText(_translate("MainBD", "EXPORTAR"))
        self.bt_recarga_bd.setText(_translate("MainBD", "RECARGAR TABLA"))

    def AbrirArchivo(self):
        #global pathFileName
        dir = ""
        dir, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Seleccionar archivo', '', 'csv(*.csv)')
        #print("pathFileName-`{}`, \n_-`{}`".format(pathFileName, _))
        if dir:
            f = open(dir, 'rb')
            #print(pathFileName)
            return dir
            #self.dzielenieStron(f)

    def Comprobar_texto(self,texto):
        #return 0 incorrecto
        #return 1 correcto
        if texto == "":
            print("vacio")
            return 0
            #self.alerta_tabla()
        elif texto != "":
            campo = re.compile(r"[A-Za-z]{1,20}")
            if campo.search(texto):  # Comprobemos que esta es una URL valida
                return 1
            else:
                return 0

    def CargarCSV(self):
        nombre_tabla = self.input_nombre_bd.text()
        print(nombre_tabla)
        #self.Comprobar_texto(nombre_tabla)
        if self.Comprobar_texto(nombre_tabla) == 0:
            print("vacio")
            self.alerta_tabla()
        else:
            try:
                dir = self.AbrirArchivo()
                self.GuardarCSV(dir)
            except:
                print("")

    def CrearTabla(self,nombre_tabla):
        query = '''CREATE TABLE IF NOT EXISTS ''' + nombre_tabla + '''
                (user_id Text, 
                status_id Text , 
                created_at Datetime, 
                screen_name Text,
                text Text,
                source Text,
                display_text_width int, 
                reply_to_status_id Text,
                reply_to_user_id Text,
                reply_to_screen_name Text, 
                is_quote TEXT,
                is_retweet Text,
                favorite_count int, 
                retweet_count int,
                hashtags text,
                symbols text, 
                urls_url text,
                urls_tco text,
                urls_expanded_url text,
                media_url text,
                media_tco text,
                media_expanded_url text,
                media_type text,
                ext_media_url text,
                ext_media_tco text,
                ext_media_expanded_url text,
                ext_media_type text,
                mentions_user_id text, 
                mentions_screen_name text, 
                lang text, 
                quoted_status_id text,
                quoted_text text, 
                quoted_created_at text, 
                quoted_source text,
                quoted_favorite_count int,
                quoted_retweet_count int, 
                quoted_user_id text,
                quoted_screen_name text,
                quoted_name text,
                quoted_followers_count int,
                quoted_friends_count int, 
                quoted_statuses_count int,
                quoted_location text, 
                quoted_description text,
                quoted_verified text,
                retweet_status_id text,
                retweet_text text, 
                retweet_created_at datetime, 
                retweet_source text, 
                retweet_favorite_count int,
                retweet_retweet_count int,
                retweet_user_id text, 
                retweet_screen_name text, 
                retweet_name text, 
                retweet_followers_count int,
                retweet_friends_count int ,
                retweet_statuses_count int,
                retweet_location text,
                retweet_description text,
                retweet_verified text,
                place_url text,
                place_name text,
                place_full_name text, 
                place_type text,
                country text,
                country_code text,
                geo_coords text,
                coords_coords text,
                bbox_coords text,
                status_url text,
                name text, 
                location text, 
                description text, 
                link text, 
                protected text, 
                followers_count int,
                friends_count int,
                listed_count int, 
                statuses_count int, 
                favourites_count int,
                account_created_at datetime,
                verified text,
                profile_url text,
                profile_expanded_url text,
                account_lang text, 
                profile_banner_url text,
                profile_background_url text,
                profile_image_url text)'''
        db = self.run_query(query)

    def Insertar(self,csv,tabla):
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()
        for row in csv:
            cur.execute(
                "INSERT INTO " + tabla +" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                 row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                 row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                 row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39],
                 row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49],
                 row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59],
                 row[60], row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69],
                 row[70], row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78], row[79],
                 row[80], row[81], row[82], row[83], row[84], row[85], row[86], row[87]))
        sql.commit()
        sql.close()
        self.limpiarBase(tabla)

    def GuardarCSV(self,dir):

        nombre_tabla =   self.input_nombre_bd.text()
        #print(nombre_tabla)
        # poner un try/catch

        f = open(dir, 'r',errors='ignore')

        #f = open(dir, 'r', encoding='utf-8')

        # Omitimos la linea de encabezado
        next(f, None)
        reader = csv.reader(f, delimiter=',')
        self.CrearTabla(nombre_tabla)
        self.Insertar(reader,nombre_tabla)

        # self.limpiarBase()
        f.close()
        #sql.commit()
        #sql.close()
        #self.limpiarBase(nombre_tabla)
        self.CargarTabla()
        #self.ContadorFilas()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def limpiarBase(self,tabla):
        query = "delete from " + tabla + " where rowid not in (select  min(rowid) from " + tabla + " group by status_id)"
        db = self.run_query(query)
        sql = sqlite3.connect(self.nombre_BD)
        #cur = sql.cursor()
        #print(tabla)
        """cur.execute(
            "delete from " + tabla + " where rowid not in (select  min(rowid) from " + tabla + " group by status_id)")
        sql.commit()
        sql.close()"""

    def CargarTabla(self):
        index = 0
        query = 'SELECT tbl_name FROM sqlite_master WHERE type = "table"'
        db_rows = self.run_query(query)
        for row in db_rows:
            #print(row)
            self.tabla.setRowCount(index + 1)
            query = 'SELECT min(created_at),max(created_at) from ' + row[0]
            db_rows2 = self.run_query(query)
            for row2 in db_rows2:
                self.tabla.setItem(index, 0, QTableWidgetItem(row[0]))
                self.tabla.setItem(index, 1, QTableWidgetItem(row2[0]))
                self.tabla.setItem(index, 2, QTableWidgetItem(row2[1]))
                index += 1

    def BorrarTabla(self):
        #sql = sqlite3.connect(self.nombre_BD)
        #cur = sql.cursor()
        selected = self.tabla.currentIndex()
        nombre = self.tabla.selectedItems()[0].text()
        query = "DROP TABLE " + nombre
        db = self.run_query(query)
        query = "vacuum"
        db = self.run_query(query)
        self.tabla.removeRow(selected.row())

    def ExportarBase(self):
        try:
            base = self.tabla.selectedItems()[0].text()
            sql = sqlite3.connect(self.nombre_BD)
            cur = sql.cursor()
            cur.execute("select * from " + base)
            dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', '', 'csv(*.csv)')
            with open(dir, "w", newline='',errors='ignore') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur.fetchall())
            QMessageBox.warning(self.centralwidget, "EXPORTACION CORRECTA", "EXPORTACION DE BASE TERMINADA.")
            sql.close()
        except:
            print("")

    def Anadir(self):
        dir = self.AbrirArchivo()
        base = self.tabla.selectedItems()[0].text()

        f = open(dir, 'r', errors='ignore')

        # Omitimos la linea de encabezado
        next(f, None)
        reader = csv.reader(f, delimiter=',')
        print(base)
        print(dir)
        self.Insertar(reader, base)

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Salir",
                                     "Estas seguro que quieres salir?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def alerta_tabla(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Campo de texto no valido")
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def AYUDA(self):
        self.ventana = Ui_MainBD()
        self.ui = Ui_MainAyuda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def SALIR(self):
        exit()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBD = Ui_MainBD()
    MainBD.setupUI()
    MainBD.show()
    sys.exit(app.exec_())
