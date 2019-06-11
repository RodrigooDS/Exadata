# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BD.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
                            QMessageBox, QHBoxLayout, QLabel,QGridLayout, QComboBox, QStyleFactory, QListWidget, QListWidgetItem,QFrame
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt,QThread, QBasicTimer
from Ayuda import Main_Ayuda
import sqlite3
import csv
import sys
import datetime

class Main_MUESTRA(QMainWindow):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""

    def __init__(self, parent=None):
        super(Main_MUESTRA, self).__init__(parent)
        self.setWindowTitle("EXADATA")
        self.setFixedSize(900, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # FRAME
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(950)
        frame.setFixedHeight(100)
        frame.move(0, 0)

        labelIcono = QLabel(frame)
        labelIcono.setFixedWidth(65)
        labelIcono.setFixedHeight(65)
        labelIcono.setPixmap(QPixmap("icono.jpg").scaled(65, 65, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        labelIcono.move(10, 28)

        fuenteTitulo = QFont()
        fuenteTitulo.setPointSize(25)
        fuenteTitulo.setBold(True)

        labelTitulo = QLabel("<font color='white'>EXADATA</font>", frame)
        labelTitulo.setFont(fuenteTitulo)
        labelTitulo.move(85, 30)

        fuenteSubtitulo = QFont()
        fuenteSubtitulo.setPointSize(13)

        labelSubtitulo = QLabel("<font color='white'>Análisis de Tweets "
                                , frame)
        labelSubtitulo.setFont(fuenteSubtitulo)
        labelSubtitulo.move(85, 68)

        # BARRA
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 480, 510, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        #inicio tabla
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        # formato tabla posx,posy,tamx,tamy
        self.tabla.setGeometry(QtCore.QRect(10, 120, 510, 400))
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
        self.bt_exportar_bd.setGeometry(QtCore.QRect(550, 400, 100, 20))
        self.bt_exportar_bd.setObjectName("bt_exportar_bd")
        self.bt_exportar_bd.clicked.connect(self.Exportar_Fecha)

        # boton exportar_bd2
        self.bt_exportar_bd2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd2.setGeometry(QtCore.QRect(635, 460, 100, 20))
        self.bt_exportar_bd2.setObjectName("bt_exportar_bd2")
        self.bt_exportar_bd2.clicked.connect(self.Exportar_Cantidad)

        # CUADRO TEXTO
        self.muestra_cantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.muestra_cantidad.setGeometry(QtCore.QRect(550, 460, 50, 20))
        self.muestra_cantidad.setObjectName("muestra_cantidad")

        #=================================================================================
        self.setCentralWidget(self.centralwidget)

        #CALENDARIO
        # formato tabla posx,posy,tamx,tamy
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(550, 120, 312, 183))
        self.calendario.setStyleSheet("")
        self.calendario.setStyleSheet("alternate-background-color: rgb(118, 148, 255);")
        self.calendario.setObjectName("calendario")

        #LABEL MUESTRA POR FECHA
        self.label_muestraFecha = QtWidgets.QLabel(self.centralwidget)
        self.label_muestraFecha.setGeometry(QtCore.QRect(550, 330, 121, 16))
        self.label_muestraFecha.setObjectName("label_muestraFecha")

        #LABEL MUESTRA DE TODA LA BASE
        self.label_muestraToda = QtWidgets.QLabel(self.centralwidget)
        self.label_muestraToda.setGeometry(QtCore.QRect(550, 440, 200, 16))
        self.label_muestraToda.setObjectName("label_muestraToda")

        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(550, 370, 110, 22))
        self.fechaInicio.setObjectName("fechaInicio")
        self.fechaInicio.setCalendarPopup(True)
        self.fechaTermino = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino.setGeometry(QtCore.QRect(720, 370, 110, 22))
        self.fechaTermino.setObjectName("fechaTermino")
        self.fechaTermino.setCalendarPopup(True)
        self.fechaInicio.setDate(QtCore.QDate.currentDate())
        self.fechaTermino.setDate(QtCore.QDate.currentDate())

        self.incioLetra = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra.setGeometry(QtCore.QRect(550, 350, 111, 16))
        self.incioLetra.setObjectName("incioLetra")
        self.terminoLetra = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra.setGeometry(QtCore.QRect(720, 350, 111, 16))
        self.terminoLetra.setObjectName("terminoLetra")

        #BARRA MENU
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")

        self.Programas = QtWidgets.QMenu(self.menubar)
        self.BaseDeDatos = QtWidgets.QAction(self)
        self.menubar.addAction(self.Programas.menuAction())
        self.Programas.addAction(self.BaseDeDatos)
        self.BaseDeDatos.triggered.connect(self.close)

        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.SobreQue = QtWidgets.QAction(self)
        self.menubar.addAction(self.Ayuda.menuAction())
        self.Ayuda.addAction(self.SobreQue)
        self.SobreQue.triggered.connect(self.AYUDA)

        # boton recarga_bd
        self.bt_recarga_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_recarga_bd.setGeometry(QtCore.QRect(10, 530, 510, 20))
        self.bt_recarga_bd.setObjectName("bt_recarga_bd")
        self.bt_recarga_bd.clicked.connect(self.CargarTabla)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        #new table
        self.tabla_master()
        self.CargarTabla()
        self.progressBar.hide()

    def retranslateUi(self, Main_MUESTRA):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Main_MUESTRA", "Muestra"))
        #inicio tabla
        item = self.tabla.horizontalHeaderItem(0)
        item.setText(_translate("Main_MUESTRA", "NOMBRE"))
        item = self.tabla.horizontalHeaderItem(1)
        item.setText(_translate("Main_MUESTRA", "FECHA DESDE"))
        item = self.tabla.horizontalHeaderItem(2)
        item.setText(_translate("Main_MUESTRA", "FECHA HASTA"))
        item = self.tabla.horizontalHeaderItem(3)
        item.setText(_translate("Main_MUESTRA", "TWEETS"))
        self.incioLetra.setText(_translate("Main_MUESTRA", "FECHA INICIO"))
        self.terminoLetra.setText(_translate("Main_MUESTRA", "FECHA TERMINO"))
        #fin tabla

        #LABEL
        self.label_muestraFecha.setText(_translate("Main_MUESTRA", "MUESTRA POR FECHA"))
        self.label_muestraToda.setText(_translate("Main_MUESTRA", "MUESTRA POR CANTIDAD DE TWEETS"))
        self.bt_exportar_bd.setText(_translate("Main_MUESTRA", "EXPORTAR"))
        self.bt_exportar_bd2.setText(_translate("Main_MUESTRA", "EXPORTAR"))
        self.bt_recarga_bd.setText(_translate("Main_MUESTRA", "RECARGAR TABLA"))

        #BARRA MENU
        self.Programas.setTitle(_translate("Main_MUESTRA", "Programas"))
        self.BaseDeDatos.setText(_translate("Main_MUESTRA", "Salir"))


        self.Ayuda.setTitle(_translate("Main_MUESTRA", "Ayuda"))
        self.SobreQue.setText(_translate("Main_MUESTRA", "Sobre Que"))

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def CargarTabla(self):
        index = 0
        query = 'SELECT tabla,strftime("%d-%m-%Y",(fecha_inicio)),strftime("%d-%m-%Y",(fecha_termino)), cantidad FROM Master'
        print(query)
        db_rows = self.run_query(query)
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
        dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', base, 'csv(*.csv)')
        print(dir)
        self.progressBar.show()
        self.progressBar.setRange(0, 0)
        self.BLOQUEO()
        self.thread = HiloexportarFecha(base,fecha_inicio,fecha_termino, self.nombre_BD, dir)
        self.thread.start()
        self.thread.taskFinished.connect(self.Exportado)
        self.thread.taskFinishedBarra.connect(self.STOPBARRA)

    def Exportar_Cantidad(self):
        base = self.tabla.selectedItems()[0].text()
        cantidad_tweets = self.muestra_cantidad.text()
        dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', base, 'csv(*.csv)')
        print(dir)
        self.progressBar.show()
        self.progressBar.setRange(0, 0)
        self.BLOQUEO()
        self.thread = HiloexportarCantidad(base, cantidad_tweets, self.nombre_BD, dir)
        self.thread.start()
        self.thread.taskFinished.connect(self.Exportado)
        self.thread.taskFinishedBarra.connect(self.STOPBARRA)

    def Exportado(self):
        QMessageBox.warning(self.centralwidget, "EXPORTACION CORRECTA", "EXPORTACION DE BASE TERMINADA.")

    def Home(self):
        from Home import Main
        self.ventana = Main()
        self.ventana.show()
        self.ventana.setWindowState(Qt.WindowNoState)

    def closeEvent(self, event):
        close = QMessageBox.question(self, "Salir",
                                     "Estas seguro que quieres salir de la Ayuda?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            print("cerro")
            self.Home()
        else:
            print("")

    def AYUDA(self):
        self.ventana = Main_MUESTRA()
        self.ui = Ui_MainAyuda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def tabla_master(self):
        table = "Master"
        query = '''CREATE TABLE IF NOT EXISTS ''' + table + '''
                                (tabla text, 
                                fecha_inicio text ,
                                fecha_termino text, 
                                cantidad text)'''
        self.run_query(query)

    def STOPBARRA(self):
        self.progressBar.setRange(0,1)
        self.progressBar.hide()

        self.bt_exportar_bd.setEnabled(True)
        self.bt_exportar_bd2.setEnabled(True)
        self.bt_recarga_bd.setEnabled(True)


    def BLOQUEO(self):
        self.bt_exportar_bd.setEnabled(False)
        self.bt_exportar_bd2.setEnabled(False)
        self.bt_recarga_bd.setEnabled(False)



class HiloexportarFecha(QThread):
    taskFinished = QtCore.pyqtSignal()
    taskFinishedBarra = QtCore.pyqtSignal()
    def __init__(self,nombre_tabla,desde, hasta,nombre_base,dir):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.fecha_inicio = desde
        self.fecha_termino = hasta
        self.nombre_BD = nombre_base
        self.dir = dir
        self.centralwidget = QtWidgets.QWidget()

    def run(self):
        print("hilo iniciado")
        try:
            sql = sqlite3.connect(self.nombre_BD)
            cur = sql.cursor()
            cur.execute(
                "select * from " + self.base + " where created_at BETWEEN ('" + self.fecha_inicio + " 00:00:00') and ('" + self.fecha_termino + " 23:59:59') order by created_at asc, RANDOM() LIMIT 1000")

            with open(self.dir, "w", newline='', errors='ignore') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur.fetchall())
            sql.close()
            self.taskFinishedBarra.emit()
            self.taskFinished.emit()

        except:
            print("")
        print("hilo terminado")

class HiloexportarCantidad(QThread):
    taskFinished = QtCore.pyqtSignal()
    taskFinishedBarra = QtCore.pyqtSignal()
    def __init__(self,nombre_tabla,cantidad,nombre_base,dir):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.cantidad_tweets = cantidad
        self.nombre_BD = nombre_base
        self.dir = dir
        self.centralwidget = QtWidgets.QWidget()

    def run(self):
        print("hilo iniciado")
        try:
            sql = sqlite3.connect(self.nombre_BD)
            cur = sql.cursor()
            cur.execute("SELECT * FROM " + self.base + " RANDOM LIMIT(" + self.cantidad_tweets + ")")

            with open(self.dir, "w", newline='', errors='ignore') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur.fetchall())
            sql.close()
            self.taskFinishedBarra.emit()
            self.taskFinished.emit()

        except:
            print("")
        print("hilo terminado")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle('fusion')
    palette = QtGui.QPalette()
    fuente = QFont()

    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    app.setFont(fuente)

    window = Ui_MainMUESTRA()
    window.show()
    sys.exit(app.exec_())



