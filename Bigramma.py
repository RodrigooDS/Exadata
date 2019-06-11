# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BD.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# nltk librería de análisis de lenguaje
from time import time
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
stop_words_sp = set(stopwords.words('spanish'))
stop_words_en = set(stopwords.words('english'))
# Concatenar las stopwords aplicándose a una cuenta que genera contenido en inglés y español
stop_words = stop_words_sp | stop_words_en
from nltk import tokenize
from nltk import bigrams
from nltk.tokenize import word_tokenize
import re



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
                            QMessageBox, QHBoxLayout, QLabel,QGridLayout, QComboBox, QStyleFactory, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt,QThread, QBasicTimer
from Ayuda import Main_Ayuda
import sqlite3
import csv
import sys
import datetime

class Ui_MainBigrama(QMainWindow):
    pathFileName = ""
    nombre_bd = "Base.db"
    nombre_tabla = ""
    def setupUi(self, MainBD):
        MainBD.setObjectName("MainBD")
        MainBD.setFixedSize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainBD)
        self.centralwidget.setObjectName("centralwidget")

        # BARRA
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(550, 440, 280, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

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
        self.tabla_popularidad.setGeometry(QtCore.QRect(10, 340, 510, 250))
        self.tabla_popularidad.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla_popularidad.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla_popularidad.setColumnCount(3)
        self.tabla_popularidad.setObjectName("tabla_popularidad")
        self.tabla_popularidad.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(2, item)
        self.tabla_popularidad.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_popularidad.horizontalHeader().setStretchLastSection(True)
        self.tabla_popularidad.verticalHeader().setStretchLastSection(False)
        #self.tabla_popularidad.cellClicked.connect(self.ConsultarFecha)
        # fin tabla_popularidad

        # BOTONES
        # boton exportar_bd
        self.bt_exportar_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd.setGeometry(QtCore.QRect(550, 490, 110, 20))
        self.bt_exportar_bd.setObjectName("bt_exportar_bd")
        self.bt_exportar_bd.clicked.connect(self.Exportar)

        # boton resultado
        self.resultado = QtWidgets.QPushButton(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(550, 410, 100, 20))
        self.resultado.setObjectName("resultado")
        self.resultado.clicked.connect(self.test)

        # boton recarga_bd
        self.bt_recarga_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_recarga_bd.setGeometry(QtCore.QRect(10, 300, 510, 20))
        self.bt_recarga_bd.setObjectName("bt_recarga_bd")
        self.bt_recarga_bd.clicked.connect(self.CargarTabla)



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
        self.label_INFLUENCIADORES.setGeometry(QtCore.QRect(550, 340, 121, 20))
        self.label_INFLUENCIADORES.setObjectName("label_INFLUENCIADORES")

        self.label_EXPORTAR = QtWidgets.QLabel(self.centralwidget)
        self.label_EXPORTAR.setGeometry(QtCore.QRect(550, 470, 200, 20))
        self.label_EXPORTAR.setObjectName("label_EXPORTAR")

        self.label_PUBLICACIONES = QtWidgets.QLabel(self.centralwidget)
        self.label_PUBLICACIONES.setGeometry(QtCore.QRect(550, 470, 190, 20))
        self.label_PUBLICACIONES.setObjectName("label_PUBLICACIONES")

        #TEXTO
        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(550, 380, 110, 22))
        self.fechaInicio.setObjectName("fechaInicio")
        self.fechaInicio.setCalendarPopup(True)
        self.fechaTermino = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino.setGeometry(QtCore.QRect(720, 380, 110, 22))
        self.fechaTermino.setObjectName("fechaTermino")
        self.fechaTermino.setCalendarPopup(True)
        self.fechaInicio.setDate(QtCore.QDate.currentDate())
        self.fechaTermino.setDate(QtCore.QDate.currentDate())

        self.incioLetra = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra.setGeometry(QtCore.QRect(550, 360, 111, 16))
        self.incioLetra.setObjectName("incioLetra")
        self.terminoLetra = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra.setGeometry(QtCore.QRect(720, 360, 111, 16))
        self.terminoLetra.setObjectName("terminoLetra")

        # BARRA MENU
        self.menubar = QtWidgets.QMenuBar(MainBD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")

        self.Programas = QtWidgets.QMenu(self.menubar)
        self.BaseDeDatos = QtWidgets.QAction(MainBD)
        self.menubar.addAction(self.Programas.menuAction())
        self.Programas.addAction(self.BaseDeDatos)
        self.Programas.triggered.connect(self.close)

        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.SobreQue = QtWidgets.QAction(MainBD)
        self.menubar.addAction(self.Ayuda.menuAction())
        self.Ayuda.addAction(self.SobreQue)
        self.SobreQue.triggered.connect(self.AYUDA)

        self.retranslateUi(MainBD)
        QtCore.QMetaObject.connectSlotsByName(MainBD)

        #new table
        self.tabla_master()
        self.CargarTabla()
        self.progressBar.hide()
        self.bt_exportar_bd.hide()
        self.label_EXPORTAR.hide()

    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("MainBD", "Bigrama"))

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
        item.setText(_translate("MainBD", "PALABRA"))
        item = self.tabla_popularidad.horizontalHeaderItem(1)
        item.setText(_translate("MainBD", "PALABRA"))
        item = self.tabla_popularidad.horizontalHeaderItem(2)
        item.setText(_translate("MainBD", "CANTIDAD DE VECES OCUPADA"))
        # fin tabla_popularidad

        #LABEL
        self.incioLetra.setText(_translate("MainBD", "FECHA INICIO"))
        self.terminoLetra.setText(_translate("MainBD", "FECHA TERMINO"))
        self.label_INFLUENCIADORES.setText(_translate("MainBD", "NUBE DE PALABRAS"))
        self.label_EXPORTAR.setText(_translate("MainBD", "EXPORTAR DATOS OBTENIDOS"))

        self.bt_exportar_bd.setText(_translate("MainBD", "EXPORTAR"))
        self.resultado.setText(_translate("MainBD", "RESULTADO"))

        self.bt_recarga_bd.setText(_translate("MainBD", "RECARGAR TABLA"))

        # BARRA MENU
        self.Programas.setTitle(_translate("MainBD", "Programas"))
        self.BaseDeDatos.setText(_translate("MainBD", "Salir"))


        self.Ayuda.setTitle(_translate("MainBD", "Ayuda"))
        self.SobreQue.setText(_translate("MainBD", "Sobre Que"))

    def run_query(self, query, nombre_bd, parameters=()):
        with sqlite3.connect(self.nombre_bd) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def CargarTabla(self):
        nombre_bd = "Base.db"
        index = 0
        query = 'SELECT tabla,strftime("%d-%m-%Y",(fecha_inicio)),strftime("%d-%m-%Y",(fecha_termino)), cantidad FROM Master'
        print(query)
        db_rows = self.run_query(query,nombre_bd)
        for row in db_rows:
            self.tabla.setRowCount(index + 1)
            self.tabla.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla.setItem(index, 1, QTableWidgetItem(row[1]))
            self.tabla.setItem(index, 2, QTableWidgetItem(row[2]))
            self.tabla.setItem(index, 3, QTableWidgetItem(str(row[3])))
            index += 1

    def ConsultarFecha(self):
        a = self.tabla.currentRow()
        self.tabla.selectRow(a)
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

    def Mostrar_Publicaciones(self):
        nombre_bd = "Base.db"
        base = self.tabla.selectedItems()[0].text()
        index = 0
        query = 'SELECT palabras1,palabras2,count(palabras1) FROM BIGRAMA where id="'+base+'" GROUP BY palabras1,palabras2 order by count(palabras1) desc'
        db_rows = self.run_query(query,nombre_bd)
        for row in db_rows:
            self.tabla_popularidad.setRowCount(index + 1)
            self.tabla_popularidad.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla_popularidad.setItem(index, 1, QTableWidgetItem(row[1]))
            self.tabla_popularidad.setItem(index, 2, QTableWidgetItem(str(row[2])))
            index += 1
        QMessageBox.warning(self.centralwidget, "TABLA NUBE DE PALABRAS TERMINADA", "TABLA NUBE DE PALABRAS TERMINADA.")

    def Exportado(self):
        QMessageBox.warning(self.centralwidget, "EXPORTACION CORRECTA", "EXPORTACION DE BASE TERMINADA.")

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Salir",
                                     "Estas seguro que quieres salir?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def AYUDA(self):
        self.ventana = Ui_MainNube()
        self.ui = Ui_MainAyuda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def tabla_master(self):
        nombre_bd = "Base.db"
        table = "Master"
        query = '''CREATE TABLE IF NOT EXISTS ''' + table + '''
                                (tabla text, 
                                fecha_inicio text ,
                                fecha_termino text, 
                                cantidad text)'''
        self.run_query(query, nombre_bd)

        query = "CREATE TABLE IF NOT EXISTS BIGRAMA (palabras1 Text collate nocase,palabras2 Text collate nocase, id Text)"
        print("tabla creada")
        self.run_query(query,nombre_bd)

    def STOPBARRA(self):
        self.progressBar.setRange(0, 1)
        self.progressBar.hide()
        self.label_EXPORTAR.show()
        self.bt_exportar_bd.show()

        self.bt_exportar_bd.setEnabled(True)
        self.resultado.setEnabled(True)
        self.bt_recarga_bd.setEnabled(True)

    def BLOQUEO(self):
        self.bt_exportar_bd.setEnabled(False)
        self.resultado.setEnabled(False)
        self.bt_recarga_bd.setEnabled(False)

    def test(self):
        base = self.tabla.selectedItems()[0].text()
        nombre_bd = "Base.db"
        fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")
        self.progressBar.show()
        self.progressBar.setRange(0, 0)
        self.BLOQUEO()
        self.thread = Hilopalabras(base, nombre_bd,fecha_inicio,fecha_termino)
        self.thread.start()
        self.thread.taskFinished.connect(self.STOPBARRA)
        self.thread.taskFinished.connect(self.Mostrar_Publicaciones)


    def Exportar(self):
        base = self.tabla.selectedItems()[0].text()
        nombre_bd = "Base.db"
        fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")


        dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', base, 'csv(*.csv)')
        print(dir)
        self.progressBar.show()
        self.progressBar.setRange(0, 0)
        self.BLOQUEO()
        self.thread = Hiloexportar(base, nombre_bd,fecha_inicio,fecha_termino, dir)
        self.thread.start()
        self.thread.taskFinished.connect(self.STOPBARRA)
        self.thread.taskFinished.connect(self.Mostrar_Publicaciones)

class Hilopalabras(QThread):
    taskFinished = QtCore.pyqtSignal()
    def __init__(self, nombre_tabla, nombre_base, desde, hasta):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.nombre_bd = nombre_base
        self.fecha_inicio = desde
        self.fecha_termino = hasta


    def run(self):
        start_time = time()
        self.eliminarWord(self.base, self.nombre_bd)
        self.buscador(self.base,self.nombre_bd)
        print("hilo terminado")
        elapsed_time = time() - start_time
        print("======================= FIN ================================")
        print(elapsed_time)
        self.taskFinished.emit()

    def run_query(self, query, nombre_bd, parameters=()):
        with sqlite3.connect(nombre_bd) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def buscador(self,tabla,base):

        query = 'select text from '+self.base+' where created_at between ("' + self.fecha_inicio + ' 00:00:00") and ("' + self.fecha_termino + ' 23:59:59")'
        db = self.run_query(query,base)

        self.procesador_tweet(db, tabla,base)

    def procesador_tweet(self, tweets, tabla, base):

        stop_words = set(stopwords.words('spanish'))
        x = []
        y = []
        a = 0
        for text in tweets:

            res = [(x, i.split()[j + 1]) for i in text
                   for j, x in enumerate(i.split()) if j < len(i.split()) - 1]
            #print(str(a) + "   =(despues)= " + str(res))
            for i in range(len(res)):
                if res[i][0].isalnum() and res[i][1].isalnum():
                    if res[i][0]!=stop_words and res[i][1]!=stop_words:
                        #print(str(res[i][0]) + " ==== " + str(res[i][1]))
                        x.append((res[i][0]))
                        y.append(res[i][1])
            a = a +1
        self.wordcloud(x,y,tabla, base)

    def removedor_emoji(self, string):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', string)

    def wordcloud(self, x,y, tabla, base):
        conn = sqlite3.connect(base)
        for w in range(len(x)):
            conn.execute("insert into BIGRAMA (palabras1,palabras2,id) values (?,?,?);", (x[w],y[w], tabla))
        conn.commit()
        conn.close()

    def eliminarWord(self, tabla, base):
        query = 'delete from BIGRAMA where id="'+tabla+'"'
        print(query)
        db = self.run_query(query, base)
        print("Tabla Limpia")
        print("====================================================================================")

class Hiloexportar(QThread):
    taskFinished = QtCore.pyqtSignal()
    def __init__(self,nombre_tabla,nombre_base,desde,hasta,dir):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.nombre_bd = nombre_base
        self.fecha_inicio = desde
        self.fecha_termino = hasta
        self.dir = dir

    def run(self):
        print("hilo iniciado")
        #self.eliminarWord(self.base, self.nombre_bd)
        sql = sqlite3.connect(self.nombre_bd)
        cur = sql.cursor()
        cur.execute('SELECT palabras1,palabras2,count(palabras1) FROM BIGRAMA WHERE ID="'+self.base+'" GROUP BY palabras1,palabras2 order by count(palabras1) desc')
        with open(self.dir, "w", newline='', errors='ignore') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([i[0] for i in cur.description])
            csv_writer.writerows(cur.fetchall())
        sql.close()
        self.taskFinished.emit()
        print("hilo terminado")

    '''def eliminarWord(self, tabla, base):
        query = 'delete from Word where id="'+tabla+'"'
        print(query)
        db = self.run_query(query, base)
        print("Tabla Limpia")
        print("====================================================================================")

    def run_query(self, query, nombre_bd, parameters=()):
        with sqlite3.connect(nombre_bd) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBD = QtWidgets.QMainWindow()
    ui = Ui_MainBigrama()
    ui.setupUi(MainBD)
    MainBD.show()
    sys.exit(app.exec_())


