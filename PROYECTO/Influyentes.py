from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
                            QMessageBox, QHBoxLayout, QLabel,QGridLayout, QComboBox, QStyleFactory, QListWidget, QListWidgetItem,QFrame
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt,QThread, QBasicTimer
import os, re , sqlite3 , csv, sys


class Main_Influyentes(QMainWindow):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""

    def __init__(self, parent=None):
        super(Main_Influyentes, self).__init__(parent)
        self.setWindowTitle("EXADATA")
        self.setFixedSize(900, 700)
        self.setWindowIcon(QIcon("icono.jpg"))
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
        frame.setFixedWidth(1000)
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
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        # BARRA
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 660, 500, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        # BARRA 2
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar2.setGeometry(QtCore.QRect(10, 660, 500, 20))
        self.progressBar2.setProperty("value", 24)
        self.progressBar2.setTextVisible(False)
        self.progressBar2.setObjectName("progressBar")

        #inicio tabla bases ingresadas
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        # formato tabla posx,posy,tamx,tamy
        self.tabla.setGeometry(QtCore.QRect(10, 110, 500, 250))
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
        self.tabla_popularidad.setGeometry(QtCore.QRect(10, 400, 500, 250))
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
        self.bt_exportar_bd.setGeometry(QtCore.QRect(720, 410, 120, 20))
        self.bt_exportar_bd.setObjectName("bt_exportar_bd")
        self.bt_exportar_bd.clicked.connect(self.Exportar_Influencer)

        # boton resultado
        self.resultado = QtWidgets.QPushButton(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(550, 410, 120, 20))
        self.resultado.setObjectName("resultado")
        self.resultado.clicked.connect(self.Mostrar_Influencer)

        # boton exportar_bd2
        self.bt_exportar_bd2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar_bd2.setGeometry(QtCore.QRect(720, 540, 120, 20))
        self.bt_exportar_bd2.setObjectName("bt_exportar_bd2")
        self.bt_exportar_bd2.clicked.connect(self.Exportar_Publicaciones)

        # boton resultado2
        self.resultado2 = QtWidgets.QPushButton(self.centralwidget)
        self.resultado2.setGeometry(QtCore.QRect(550, 540, 120, 20))
        self.resultado2.setObjectName("resultado2")
        self.resultado2.clicked.connect(self.Mostrar_Publicaciones)

        # boton recarga_bd
        self.bt_recarga_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_recarga_bd.setGeometry(QtCore.QRect(10, 370, 500, 20))
        self.bt_recarga_bd.setObjectName("bt_recarga_bd")
        self.bt_recarga_bd.clicked.connect(self.CargarTabla)



        #=================================================================================
        self.setCentralWidget(self.centralwidget)


        #CALENDARIO
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(550, 110, 300, 200))
        self.calendario.setStyleSheet("")
        self.calendario.setStyleSheet("alternate-background-color: rgb(118, 148, 255);")
        self.calendario.setObjectName("calendario")

        #LABEL
        self.label_INFLUENCIADORES = QtWidgets.QLabel(self.centralwidget)
        self.label_INFLUENCIADORES.setGeometry(QtCore.QRect(550, 340, 120, 20))
        self.label_INFLUENCIADORES.setObjectName("label_INFLUENCIADORES")

        self.label_PUBLICACIONES = QtWidgets.QLabel(self.centralwidget)
        self.label_PUBLICACIONES.setGeometry(QtCore.QRect(550, 470, 190, 20))
        self.label_PUBLICACIONES.setObjectName("label_PUBLICACIONES")

        #TEXTO
        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(550, 380, 120, 22))
        self.fechaInicio.setObjectName("fechaInicio")
        self.fechaInicio.setCalendarPopup(True)
        self.fechaTermino = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino.setGeometry(QtCore.QRect(720, 380, 120, 22))
        self.fechaTermino.setObjectName("fechaTermino")
        self.fechaTermino.setCalendarPopup(True)
        self.fechaInicio.setDate(QtCore.QDate.currentDate())
        self.fechaTermino.setDate(QtCore.QDate.currentDate())

        self.incioLetra = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra.setGeometry(QtCore.QRect(550, 360, 120, 16))
        self.incioLetra.setObjectName("incioLetra")
        self.terminoLetra = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra.setGeometry(QtCore.QRect(720, 360, 120, 16))
        self.terminoLetra.setObjectName("terminoLetra")

        # TEXTO3
        self.fechaInicio2 = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio2.setGeometry(QtCore.QRect(550, 510, 120, 22))
        self.fechaInicio2.setObjectName("fechaInicio1")
        self.fechaInicio2.setCalendarPopup(True)
        self.fechaTermino2 = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino2.setGeometry(QtCore.QRect(720, 510, 120, 22))
        self.fechaTermino2.setObjectName("fechaTermino1")
        self.fechaTermino2.setCalendarPopup(True)
        self.fechaInicio2.setDate(QtCore.QDate.currentDate())
        self.fechaTermino2.setDate(QtCore.QDate.currentDate())

        self.incioLetra4 = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra4.setGeometry(QtCore.QRect(550, 490, 111, 16))
        self.incioLetra4.setObjectName("incioLetra2")
        self.terminoLetra4 = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra4.setGeometry(QtCore.QRect(720, 490, 111, 16))
        self.terminoLetra4.setObjectName("terminoLetra2")

        # BARRA MENU
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")

        self.Programas = QtWidgets.QMenu(self.menubar)
        self.BaseDeDatos = QtWidgets.QAction()
        self.menubar.addAction(self.Programas.menuAction())
        self.Programas.addAction(self.BaseDeDatos)
        self.BaseDeDatos.triggered.connect(self.close)

        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.SobreQue = QtWidgets.QAction()
        self.menubar.addAction(self.Ayuda.menuAction())
        self.Ayuda.addAction(self.SobreQue)
        self.SobreQue.triggered.connect(self.AYUDA)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        #new table
        self.tabla_master()
        self.CargarTabla()
        self.progressBar.hide()
        self.progressBar2.hide()

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

        self.bt_recarga_bd.setText(_translate("MainBD", "RECARGAR TABLA"))

        # BARRA MENU
        self.Programas.setTitle(_translate("MainBD", "Programas"))
        self.BaseDeDatos.setText(_translate("MainBD", "Salir"))


        self.Ayuda.setTitle(_translate("MainBD", "Ayuda"))
        self.SobreQue.setText(_translate("MainBD", "Sobre Que"))

    def Home(self):
        from Home import Main
        self.ventana = Main()
        self.ventana.show()
        self.ventana.setWindowState(Qt.WindowNoState)


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
        try:
            base = self.tabla.selectedItems()[0].text()
            fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
            fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")
            dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', base, 'csv(*.csv)')
            print(dir)
            self.progressBar.show()
            self.progressBar.setRange(0, 0)
            self.BLOQUEO()
            self.thread = HiloexportarInfluencer(base, fecha_inicio, fecha_termino, self.nombre_BD, dir)
            self.thread.start()
            self.thread.taskFinished.connect(self.Exportado)
            self.thread.taskFinishedBarra.connect(self.STOPBARRA)
        except :
            print()

    def Mostrar_Publicaciones(self):
        base = self.tabla.selectedItems()[0].text()
        fecha_inicio = self.fechaInicio2.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino2.date().toString("yyyy-MM-dd")

        index = 0
        query = 'select screen_name USUARIO,count(screen_name) CANTIDAD from ' +base+ ' where is_retweet="FALSE" and created_at between ("'+fecha_inicio+' 00:00:00") and ("'+fecha_termino+' 23:59:59") group by screen_name order by count(screen_name) desc'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tabla_popularidad.setRowCount(index + 1)
            self.tabla_popularidad.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla_popularidad.setItem(index, 1, QTableWidgetItem(str(row[1])))
            index += 1
        QMessageBox.warning(self.centralwidget, "TABLA MAYOR PUBLICACIONES TERMINADA", "TABLA MAYOR PUBLICACIONES TERMINADA.")

    def Exportar_Publicaciones(self):
        try:
            base = self.tabla.selectedItems()[0].text()
            fecha_inicio = self.fechaInicio2.date().toString("yyyy-MM-dd")
            fecha_termino = self.fechaTermino2.date().toString("yyyy-MM-dd")
            dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', base, 'csv(*.csv)')
            print(dir)
            self.progressBar2.show()
            self.progressBar2.setRange(0, 0)
            self.BLOQUEO()
            self.thread = HiloexportarPublicaciones(base, fecha_inicio, fecha_termino, self.nombre_BD, dir)
            self.thread.start()
            self.thread.taskFinished.connect(self.Exportado)
            self.thread.taskFinishedBarra.connect(self.STOPBARRA2)
        except:
            print()


    def Exportado(self):
        QMessageBox.warning(self.centralwidget, "EXPORTACION CORRECTA", "EXPORTACION DE BASE TERMINADA.")

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
        from Ayuda import Main_Ayuda
        self.ventana = Main_Ayuda()
        self.ventana.show()
        self.hide()

    def tabla_master(self):
        table = "Master"
        query = '''CREATE TABLE IF NOT EXISTS ''' + table + '''
                                (tabla text, 
                                fecha_inicio text ,
                                fecha_termino text, 
                                cantidad text)'''
        self.run_query(query)

    def STOPBARRA(self):
        self.progressBar.setRange(0, 1)
        self.progressBar.hide()

        self.bt_exportar_bd.setEnabled(True)
        self.resultado.setEnabled(True)
        self.bt_exportar_bd2.setEnabled(True)
        self.resultado2.setEnabled(True)
        self.bt_recarga_bd.setEnabled(True)

    def STOPBARRA2(self):
        self.progressBar2.setRange(0,1)
        self.progressBar2.hide()

        self.bt_exportar_bd.setEnabled(True)
        self.resultado.setEnabled(True)
        self.bt_exportar_bd2.setEnabled(True)
        self.resultado2.setEnabled(True)
        self.bt_recarga_bd.setEnabled(True)

    def BLOQUEO(self):
        self.bt_exportar_bd.setEnabled(False)
        self.resultado.setEnabled(False)
        self.bt_exportar_bd2.setEnabled(False)
        self.resultado2.setEnabled(False)
        self.bt_recarga_bd.setEnabled(False)


class HiloexportarInfluencer(QThread):
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
            cur.execute('select retweet_screen_name USUARIO,count(retweet_screen_name) CANTIDAD from ' + self.base + ' ' \
                         'where is_retweet  = "TRUE" and created_at between ("' + self.fecha_inicio + ' 00:00:00") and ("' + self.fecha_termino + ' 23:59:59") group by retweet_screen_name order by count(retweet_screen_name) desc')
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

class HiloexportarPublicaciones(QThread):
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
                'select screen_name USUARIO,count(screen_name) CANTIDAD from ' + self.base + ' where is_retweet="TRUE" and created_at between ("' + self.fecha_inicio + ' 00:00:00") and ("' + self.fecha_termino + ' 23:59:59") '
                                                                                                        'group by screen_name order by count(screen_name) desc')
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

    window = Main_Influyentes()
    window.show()
    sys.exit(app.exec_())


