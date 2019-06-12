
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, \
                            QMessageBox, QHBoxLayout, QLabel,QGridLayout, QComboBox, QStyleFactory, QListWidget, QListWidgetItem,QFrame
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtSql import *
from PyQt5.QtCore import Qt,QThread, QBasicTimer
import os, re , sqlite3 , csv, sys
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
from nltk.tokenize import word_tokenize
import re


class Main_Nube(QMainWindow):
    pathFileName = ""
    nombre_BD = "Base.db"
    nombre_tabla = ""

    def __init__(self, parent=None):
        super(Main_Nube, self).__init__(parent)
        self.setWindowTitle("EXADATA")
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon("icono.jpg"))
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # FRAME
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(800)
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
        self.progressBar.setGeometry(QtCore.QRect(10, 560, 500, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)

        #inicio tabla 1
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        # formato tabla posx,posy,tamx,tamy
        self.tabla.setGeometry(QtCore.QRect(10, 110, 500, 200))
        self.tabla.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla.setColumnCount(4)
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
        self.tabla_popularidad.setGeometry(QtCore.QRect(10, 350, 500, 200))
        self.tabla_popularidad.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabla_popularidad.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabla_popularidad.setColumnCount(2)
        self.tabla_popularidad.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_popularidad.setHorizontalHeaderItem(1, item)
        self.tabla_popularidad.horizontalHeader().setDefaultSectionSize(225)
        self.tabla_popularidad.horizontalHeader().setStretchLastSection(True)
        self.tabla_popularidad.verticalHeader().setStretchLastSection(False)
        #self.tabla_popularidad.cellClicked.connect(self.ConsultarFecha)
        # fin tabla_popularidad

        # BOTONES
        # boton exportar resultado
        self.bt_exportar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_exportar.setGeometry(QtCore.QRect(670, 410, 110, 20))
        self.bt_exportar.clicked.connect(self.Exportar)

        # boton resultado
        self.resultado = QtWidgets.QPushButton(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(525, 410, 110, 20))
        self.resultado.clicked.connect(self.Resultado)

        # boton recarga_bd
        self.bt_recarga_bd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_recarga_bd.setGeometry(QtCore.QRect(10, 320, 500, 20))
        self.bt_recarga_bd.clicked.connect(self.CargarTabla)

        #=================================================================================

        #CALENDARIO
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(525, 110, 255, 155))
        self.calendario.setStyleSheet("")
        self.calendario.setStyleSheet("alternate-background-color: rgb(118, 148, 255);")
        self.calendario.setObjectName("calendario")

        #LABEL
        self.label_INFLUENCIADORES = QtWidgets.QLabel(self.centralwidget)
        self.label_INFLUENCIADORES.setGeometry(QtCore.QRect(525, 340, 121, 20))
        self.label_INFLUENCIADORES.setObjectName("label_INFLUENCIADORES")

        """"self.label_EXPORTAR = QtWidgets.QLabel(self.centralwidget)
        self.label_EXPORTAR.setGeometry(QtCore.QRect(525, 470, 200, 20))
        self.label_EXPORTAR.setObjectName("label_EXPORTAR")"""""

        self.label_PUBLICACIONES = QtWidgets.QLabel(self.centralwidget)
        self.label_PUBLICACIONES.setGeometry(QtCore.QRect(525, 470, 190, 20))
        self.label_PUBLICACIONES.setObjectName("label_PUBLICACIONES")

        #TEXTO
        self.fechaInicio = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaInicio.setGeometry(QtCore.QRect(525, 380, 110, 22))
        self.fechaInicio.setObjectName("fechaInicio")
        self.fechaInicio.setCalendarPopup(True)
        self.fechaTermino = QtWidgets.QDateEdit(self.centralwidget)
        self.fechaTermino.setGeometry(QtCore.QRect(670, 380, 110, 22))
        self.fechaTermino.setObjectName("fechaTermino")
        self.fechaTermino.setCalendarPopup(True)
        self.fechaInicio.setDate(QtCore.QDate.currentDate())
        self.fechaTermino.setDate(QtCore.QDate.currentDate())

        self.incioLetra = QtWidgets.QLabel(self.centralwidget)
        self.incioLetra.setGeometry(QtCore.QRect(525, 360, 111, 20))
        self.incioLetra.setObjectName("incioLetra")
        self.terminoLetra = QtWidgets.QLabel(self.centralwidget)
        self.terminoLetra.setGeometry(QtCore.QRect(670, 360, 111, 20))
        self.terminoLetra.setObjectName("terminoLetra")

        # BARRA MENU
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
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        #new table
        self.tabla_master()
        self.CargarTabla()
        self.progressBar.hide()
        #self.label_EXPORTAR.hide()
        self.bt_exportar.hide()

    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate
        MainBD.setWindowTitle(_translate("MainBD", "NUBE DE PALABRAS"))

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
        item.setText(_translate("MainBD", "CANTIDAD DE VECES OCUPADA"))
        # fin tabla_popularidad

        #LABEL
        self.incioLetra.setText(_translate("MainBD", "FECHA INICIO"))
        self.terminoLetra.setText(_translate("MainBD", "FECHA TERMINO"))
        self.label_INFLUENCIADORES.setText(_translate("MainBD", "NUBE DE PALABRAS"))
        #self.label_EXPORTAR.setText(_translate("MainBD", "EXPORTAR DATOS OBTENIDOS"))
        self.resultado.setText(_translate("MainBD", "RESULTADO"))
        self.bt_recarga_bd.setText(_translate("MainBD", "RECARGAR TABLA"))
        self.bt_exportar.setText(_translate("MainBD", "EXPORTAR"))

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

    def AYUDA(self):
        from Ayuda import Main_Ayuda
        self.ayuda = Main_Ayuda()
        self.ayuda.show()
        self.hide()

    def run_query(self, query, nombre_bd, parameters=()):
        with sqlite3.connect(self.nombre_BD) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def CargarTabla(self):
        nombre_bd = "Base.db"
        index = 0
        query = 'SELECT tabla,strftime("%d-%m-%Y",(fecha_inicio)),strftime("%d-%m-%Y",(fecha_termino)), cantidad FROM Master'
        #print(query)
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

    def Exportado(self):
        QMessageBox.warning(self.centralwidget, "EXPORTACION CORRECTA", "EXPORTACION DE BASE TERMINADA.")

    def closeEvent(self, event):
        close = QMessageBox.question(self, "Salir",
                                     "Estas seguro que quieres salir de la Ayuda?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            self.Home()
        else:
            print("")

    def tabla_master(self):
        nombre_bd = "Base.db"
        table = "Master"
        query = '''CREATE TABLE IF NOT EXISTS ''' + table + '''
                                (tabla text, 
                                fecha_inicio text ,
                                fecha_termino text, 
                                cantidad text)'''
        self.run_query(query, nombre_bd)
        query = "CREATE TABLE IF NOT EXISTS Word (palabras Text collate nocase,id Text)"
        #print("tabla creada")
        self.run_query(query,nombre_bd)

    def Mostrar_Publicaciones(self):
        nombre_bd = "Base.db"
        base = self.tabla.selectedItems()[0].text()
        index = 0
        query = 'select palabras, count(palabras) from Word where id="'+base+'" group by palabras order by count(palabras) desc'
        db_rows = self.run_query(query,nombre_bd)
        for row in db_rows:
            self.tabla_popularidad.setRowCount(index + 1)
            self.tabla_popularidad.setItem(index, 0, QTableWidgetItem(row[0]))
            self.tabla_popularidad.setItem(index, 1, QTableWidgetItem(str(row[1])))
            index += 1
        QMessageBox.warning(self.centralwidget, "TABLA NUBE DE PALABRAS TERMINADA", "TABLA NUBE DE PALABRAS TERMINADA.")

    def STOPBARRA(self):
        self.progressBar.setRange(0, 1)
        self.progressBar.hide()
        self.bt_exportar.show()
        self.bt_exportar.setEnabled(True)
        self.resultado.setEnabled(True)
        self.bt_recarga_bd.setEnabled(True)

    def BLOQUEO(self):
        self.bt_exportar.setEnabled(False)
        self.resultado.setEnabled(False)
        self.bt_recarga_bd.setEnabled(False)


    def Resultado(self):
        try:
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
        except:
            print("")

    def Exportar(self):
        base = self.tabla.selectedItems()[0].text()
        nombre_bd = "Base.db"
        fecha_inicio = self.fechaInicio.date().toString("yyyy-MM-dd")
        fecha_termino = self.fechaTermino.date().toString("yyyy-MM-dd")
        dir, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar archivo', base, 'csv(*.csv)')
        #print(dir)
        self.progressBar.show()
        self.progressBar.setRange(0, 0)
        self.BLOQUEO()
        self.thread = Hiloexportar(base, nombre_bd,fecha_inicio,fecha_termino, dir)
        self.thread.start()
        self.thread.taskFinished.connect(self.STOPBARRA)
        self.thread.taskFinished.connect(self.Mostrar_Publicaciones)


class Hilopalabras(QThread):
    taskFinished = QtCore.pyqtSignal()
    def __init__(self,nombre_tabla,nombre_base,desde,hasta):
        QThread.__init__(self)
        self.base = nombre_tabla
        self.nombre_bd = nombre_base
        self.fecha_inicio = desde
        self.fecha_termino = hasta

    def run(self):
        start_time = time()
        self.eliminarWord(self.base, self.nombre_bd)
        self.buscador(self.base,self.nombre_bd)
        #print("hilo terminado")
        elapsed_time = time() - start_time
        #print("======================= FIN ================================")
        #print(elapsed_time)
        self.taskFinished.emit()


    def run_query(self, query, nombre_bd, parameters=()):
        with sqlite3.connect(nombre_bd) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def buscador(self,tabla,base):
        query = 'select text from '+self.base+' where created_at between ("' + self.fecha_inicio + ' 00:00:00") and ("' + self.fecha_termino + ' 23:59:59")'
        #print(query)
        db = self.run_query(query,base)
        self.procesador_tweet(db, tabla,base)

    def procesador_tweet(self, tweets, tabla, base):
        test = []
        stop_words = set(stopwords.words('spanish'))
        texto = ""
        a = 0
        for i in tweets:
            word_tokens = word_tokenize(str(i))
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            for w in word_tokens:
                if w not in stop_words:
                    if w.isalnum():
                        if w != "https":
                            test.append(w.lower())
            a = a + 1
        self.wordcloud(test, tabla, base)

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

    def wordcloud(self, tweet, tabla, base):
        #print(base)
        conn = sqlite3.connect(base)
        for w in tweet:
            conn.execute("insert into Word (palabras,id) values (?,?);", (w, tabla))
        conn.commit()
        conn.close()

    def eliminarWord(self, tabla, base):
        query = 'delete from Word where id="'+tabla+'"'
        #print(query)
        db = self.run_query(query, base)
        #print("Tabla Limpia")
        #print("====================================================================================")


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
        try:
            #print("hilo iniciado")
            #self.eliminarWord(self.base, self.nombre_bd)
            sql = sqlite3.connect(self.nombre_bd)
            cur = sql.cursor()
            cur.execute('select palabras, count(palabras) as cantidad from Word where id="'+self.base+'" group by palabras order by cantidad desc')
            with open(self.dir, "w", newline='', errors='ignore') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([i[0] for i in cur.description])
                csv_writer.writerows(cur.fetchall())
            sql.close()
            self.taskFinished.emit()
            #print("hilo terminado")
        except:
            self.taskFinished.emit()
            print("")

if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    palette = QtGui.QPalette()
    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    app.setFont(fuente)
    window = Main_Nube()
    window.show()
    sys.exit(app.exec_())

