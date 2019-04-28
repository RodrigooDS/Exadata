from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
                            QMessageBox, QHBoxLayout, QLabel,QGridLayout, QComboBox, QStyleFactory, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt,QThread, QBasicTimer
import os, re , sqlite3 , csv, sys
from Ayuda import Ui_MainAyuda

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
        self.tabla_master()
        self.CargarTabla()

    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("MainBD", "Base De Datos"))
        # BARRA MENU
        self.Programas.setTitle(_translate("MainBD", "Programas"))
        self.BaseDeDatos.setText(_translate("MainBD", "Salir"))
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
        if self.Comprobar_texto(nombre_tabla) == 0:
            self.alerta_tabla()
        else:
            try:
                dir = self.AbrirArchivo()
                buttonReply = QMessageBox.question(self, 'GUARDAR BASE', "Quieres guardar la base de "+nombre_tabla+"?",
                                                   QMessageBox.Yes | QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('Si clicked.')
                    self.hilocarga = Hilocargar(nombre_tabla, self.nombre_BD, dir)
                    self.hilocarga.start()
                    self.hilocarga.taskFinished.connect(self.CargarTabla)
                if buttonReply == QMessageBox.No:
                    print('No clicked.')
            except:
                print("")

    def tabla_master(self):
        table = "Master"
        query = '''CREATE TABLE IF NOT EXISTS ''' + table + '''
                                (tabla text, 
                                fecha_inicio text ,
                                fecha_termino text, 
                                cantidad text)'''
        self.run_query(query)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def CargarTabla(self):
        index = 0
        query = 'SELECT tabla,fecha_inicio,fecha_termino FROM Master'
        print(query)
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tabla.setRowCount(index + 1)
            self.tabla.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla.setItem(index, 1, QTableWidgetItem(row[1]))
            self.tabla.setItem(index, 2, QTableWidgetItem(row[2]))
            index += 1

    def BorrarTabla(self):
        selected = self.tabla.currentIndex()
        nombre = self.tabla.selectedItems()[0].text()
        print(nombre)
        buttonReply = QMessageBox.question(self, 'ELIMINAR BASE', "QUIERES BORRAR LA BASE " + nombre + "?",
                                           QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Si clicked.')
            self.hiloeliminar = Hiloeliminar(nombre, self.nombre_BD)
            self.hiloeliminar.start()
            self.tabla.removeRow(selected.row())
        if buttonReply == QMessageBox.No:
            print('No clicked.')

    def ExportarBase(self):
        base = self.tabla.selectedItems()[0].text()
        dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', '', 'csv(*.csv)')
        print(dir)
        self.thread = Hiloexportar(base,self.nombre_BD,dir)
        self.thread.start()

    def Anadir(self):
        try:
            dir = self.AbrirArchivo()
            base = self.tabla.selectedItems()[0].text()
            print(base)
            #dir = self.AbrirArchivo()
            self.hiloagrega = Hiloagregar(base, self.nombre_BD, dir)
            self.hiloagrega.start()
            #self.Insertar(reader, base)
        except:
            print("")

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



class Hiloeliminar(QThread):

    def __init__(self,nombre_tabla,nombre_base):
        QThread.__init__(self)
        #self.selected = selected
        self.nombre = nombre_tabla
        self.nombre_bd = nombre_base

    def run(self):
        try :
            query = "DROP TABLE " + self.nombre
            self.run_query(query,self.nombre_bd)
            print("listo 1")
            query = 'DELETE FROM Master WHERE tabla = "' + self.nombre +'"'
            self.run_query(query, self.nombre_bd)
            print("listo 2")
            query = "vacuum"
            self.run_query(query,self.nombre_bd)
        except:
            print("")

    def run_query(self, query,nombre_BD, parameters=()):
        with sqlite3.connect(nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
  
class Hiloexportar(QThread):

    def __init__(self,nombre_tabla,nombre_base,dir):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.nombre_BD = nombre_base
        self.dir = dir
        self.centralwidget = QtWidgets.QWidget()

    def run(self):
        print("hilo iniciado")
        try:
            sql = sqlite3.connect(self.nombre_BD)
            cur = sql.cursor()
            cur.execute("select * from " + self.base)
            with open(self.dir, "w", newline='', errors='ignore') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur.fetchall())
            sql.close()
            QMessageBox.warning(self.centralwidget, "EXPORTACION CORRECTA", "EXPORTACION DE BASE TERMINADA.")
        except:
            print("")


class Hilocargar(QThread):
    taskFinished = QtCore.pyqtSignal()
    def __init__(self, nombre_tabla, nombre_base, dir):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.nombre_BD = nombre_base
        self.dir = dir
        self.centralwidget = QtWidgets.QWidget()

    def run(self):
        print("================================================")
        print(self.base)
        print(self.nombre_BD)
        print(self.dir)
        print("================================================")
        f = open(self.dir, 'r',errors='ignore')
        next(f, None)
        reader = csv.reader(f, delimiter=',')
        self.CrearTabla(self.base,self.nombre_BD)
        self.Insertar(reader,self.base,self.nombre_BD)
        self.Insertar_Master(self.base,self.nombre_BD)
        QMessageBox.warning(self.centralwidget, "IMPORTACION CORRECTA", "IMPORTACION DE BASE TERMINADA.")
        self.taskFinished.emit()


    def CrearTabla(self,nombre_tabla,nombre_base):
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
        self.run_query(query,nombre_base)
        table = "Master"
        query = '''CREATE TABLE IF NOT EXISTS ''' + table + '''
                        (tabla text, 
                        fecha_inicio text , 
                        fecha_termino text, 
                        cantidad text)'''
        self.run_query(query, nombre_base)

    def Insertar_Master(self,nombre_tabla,nombre_bd):
        table = "Master"
        query = 'SELECT min(created_at), max(created_at),count(*) from ' + nombre_tabla
        db_rows = self.run_query(query,nombre_bd)
        for row in db_rows:
            query = "INSERT INTO Master VALUES (?,?,?,?)"
            parametros = (nombre_tabla,row[0],row[1], row[2])
            self.run_query(query, nombre_bd,parametros)

    def Insertar(self,csv,tabla,nombre_base):
        sql = sqlite3.connect(nombre_base)
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
        self.limpiarBase(tabla, nombre_base)

    def limpiarBase(self,tabla,nombre_base):
        query = "delete from " + tabla + " where rowid not in (select  min(rowid) from " + tabla + " group by status_id)"
        print(nombre_base)
        db = self.run_query(query,nombre_base)

    def run_query(self, query,nombre_BD, parameters=()):
        with sqlite3.connect(nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

class Hiloagregar(QThread):

    def __init__(self, nombre_tabla, nombre_base, dir):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.nombre_BD = nombre_base
        self.dir = dir

    def run(self):
        print("================================================")
        print(self.base)
        print(self.nombre_BD)
        print(self.dir)
        print("================================================")
        try:
            f = open(self.dir, 'r', errors='ignore')
            # Omitimos la linea de encabezado
            next(f, None)
            reader = csv.reader(f, delimiter=',')
            #print(base)
            #print(dir)
            self.Insertar(reader,self.base,self.nombre_BD)
        except:
            print("")

    def Insertar(self,csv,tabla,nombre_base):
        sql = sqlite3.connect(nombre_base)
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
        self.limpiarBase(tabla,nombre_base)

    def limpiarBase(self,tabla,nombre_base):
        query = "delete from " + tabla + " where rowid not in (select  min(rowid) from " + tabla + " group by status_id)"
        print(nombre_base)
        db = self.run_query(query,nombre_base)
        #sql = sqlite3.connect(nombre_base)
        #cur = sql.cursor()
        #print(tabla)

    def run_query(self, query,nombre_BD, parameters=()):
        #print("run_query 1")
        with sqlite3.connect(nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBD = Ui_MainBD()
    MainBD.setupUI()
    MainBD.show()
    sys.exit(app.exec_())
