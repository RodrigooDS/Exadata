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

class Ui_MainBD(object):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""
    def setupUi(self, MainBD):
        MainBD.setObjectName("MainBD")
        MainBD.resize(800, 600)
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

        #=================================================================================
        MainBD.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainBD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuProgramas = QtWidgets.QMenu(self.menubar)
        self.menuProgramas.setObjectName("menuProgramas")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainBD.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainBD)
        self.statusbar.setObjectName("statusbar")
        MainBD.setStatusBar(self.statusbar)
        self.actionIndex = QtWidgets.QAction(MainBD)
        self.actionIndex.setObjectName("actionIndex")
        self.actionSalir = QtWidgets.QAction(MainBD)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSobre = QtWidgets.QAction(MainBD)
        self.actionSobre.setObjectName("actionSobre")
        self.actionManual_De_Uso = QtWidgets.QAction(MainBD)
        self.actionManual_De_Uso.setObjectName("actionManual_De_Uso")
        self.menuProgramas.addAction(self.actionIndex)
        self.menuProgramas.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionSobre)
        self.menuAyuda.addAction(self.actionManual_De_Uso)
        self.menubar.addAction(self.menuProgramas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())


        self.retranslateUi(MainBD)
        QtCore.QMetaObject.connectSlotsByName(MainBD)

        #new table
        self.get_products()


    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("MainBD", "Base De Datos"))
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
        self.menuProgramas.setTitle(_translate("MainBD", "Programas"))
        self.menuAyuda.setTitle(_translate("MainBD", "Ayuda"))
        self.actionIndex.setText(_translate("MainBD", "Index"))
        self.actionSalir.setText(_translate("MainBD", "Salir"))
        self.actionSobre.setText(_translate("MainBD", "Sobre"))
        self.actionManual_De_Uso.setText(_translate("MainBD", "Manual De Uso"))

    def AbrirArchivo(self):
        global pathFileName
        pathFileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Wybierz plik', '', 'csv(*.csv)')
        print("pathFileName-`{}`, \n_-`{}`".format(pathFileName, _))
        if pathFileName:
            f = open(pathFileName, 'rb')

            print(pathFileName)
            #self.dzielenieStron(f)

    def CargarCSV(self):
        self.AbrirArchivo()
        self.GuardarCSV()

    def GuardarCSV(self):
        # Using try in case user types in unknown file or closes without choosing a file.
        #nombre_tabla = self.name.get()
        nombre_tabla =   self.input_nombre_bd.text()
        #print(nombre_tabla)
        # poner un try/catch
        #f = open(pathFileName, 'r', encoding='utf-8')
        f=open(pathFileName,'r')
        # f=open(name,'r')
        # Omitimos la linea de encabezado
        next(f, None)
        reader = csv.reader(f, delimiter=',')
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS ''' + nombre_tabla + '''
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
                profile_image_url text)''')

        for row in reader:
            cur.execute(
                "INSERT INTO " + nombre_tabla + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                 row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                 row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                 row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39],
                 row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49],
                 row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59],
                 row[60], row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69],
                 row[70], row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78], row[79],
                 row[80], row[81], row[82], row[83], row[84], row[85], row[86], row[87]))

        # cur.execute("delete from " + nombre_tabla +" where rowid not in (select  min(rowid) from "+ nombre_tabla + " group by status_id)")

        # self.limpiarBase()
        f.close()
        sql.commit()
        sql.close()
        self.limpiarBase(nombre_tabla)
        self.get_products()
        self.ContadorFilas()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def limpiarBase(self,tabla):
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()
        #print(tabla)
        cur.execute(
            "delete from " + tabla + " where rowid not in (select  min(rowid) from " + tabla + " group by status_id)")
        sql.commit()
        sql.close()

    def get_products(self):
        index = 0
        query = 'SELECT tbl_name FROM sqlite_master WHERE type = "table"'
        db_rows = self.run_query(query)
        for row in db_rows:
            #print(row)
            self.tabla.setRowCount(index + 1)
            query = 'SELECT min(created_at) from ' + row[0]
            db_rows2 = self.run_query(query)
            for row2 in db_rows2:
                query = 'SELECT max(created_at) from ' + row[0]
                db_rows3 = self.run_query(query)
                for row3 in db_rows3:
                    self.tabla.setItem(index, 0, QTableWidgetItem(row[0]))
                    self.tabla.setItem(index, 1, QTableWidgetItem(row2[0]))
                    self.tabla.setItem(index, 2, QTableWidgetItem(row3[0]))
                    index += 1

    def BorrarTabla(self):
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()
        selected = self.tabla.currentIndex()
        nombre = self.tabla.selectedItems()[0].text()
        print(nombre)
        cur.execute("DROP TABLE " + nombre)
        cur.execute("vacuum")
        self.tabla.removeRow(selected.row())
        sql.commit()
        sql.close()

    def ContadorFilas(self):
        count = self.tabla.rowCount()
        print(count)
    def ExportarBase(self):
        base = self.tabla.selectedItems()[0].text()
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()
        cur.execute("select * from " + base)
        with open(base + ".csv", "w", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur.fetchall())
        sql.close()

    def Anadir(self):
        base = self.tabla.selectedItems()[0].text()
        name = askopenfilename(initialdir="C:/",
                               filetypes=(("Text File", ".csv"), ("All Files", ".*")),
                               title="Choose a file."
                               )
        directorio = name
        f = open(directorio, 'r')
        reader = csv.reader(f, delimiter=',')
        sql = sqlite3.connect(self.nombre_BD)
        cur = sql.cursor()
        for row in reader:
            cur.execute(
                "INSERT INTO " + base + " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                 row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                 row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                 row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39],
                 row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49],
                 row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59],
                 row[60], row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69],
                 row[70], row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78], row[79],
                 row[80], row[81], row[82], row[83], row[84], row[85], row[86], row[87]))

        f.close()
        sql.commit()
        self.get_products()
        sql.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBD = QtWidgets.QMainWindow()
    ui = Ui_MainBD()
    ui.setupUi(MainBD)
    MainBD.show()
    sys.exit(app.exec_())


