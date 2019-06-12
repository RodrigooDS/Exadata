
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction, qApp,QFrame,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont ,QImage, QBrush

from pprint import pprint

#from BD import Ui_MainBD
#from Muestra import Ui_MainMUESTRA
#from Cortarfecha import Ui_MainCortar
#from Influyentes import Ui_MainInfluyentes
#from NubePalabras import Ui_MainNube
#from Bigramma import Ui_MainBigrama

#import logo_rc
import sys

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        # VENTANA
        self.setWindowTitle("EXADATA")
        self.setFixedSize(800,600)
        self.setWindowIcon(QIcon("icono.jpg"))

        # FRAME
        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(51, 0, 102))

        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(paleta)
        frame.setFixedWidth(900)
        frame.setFixedHeight(100)
        frame.move(0,0)

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

        labelVersion = QLabel(frame)
        labelVersion.setText(" EXADATA VERSIÓN BETA: 1.0  ")
        self.statusBar = self.statusBar()
        self.statusBar.addPermanentWidget(labelVersion, 0)

        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(800, 600))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)


        #LOGO


        # BARRA MENU
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")

        # BOTON PROGRAMAS
        self.Programas = QtWidgets.QMenu(self.menubar)
        self.Apariencia = QtWidgets.QMenu(self.Programas)
        self.BaseDeDatos = QtWidgets.QAction(self)
        self.Muestra_Programa = QtWidgets.QAction(self)
        self.Cortar_Fecha = QtWidgets.QAction(self)
        self.Popularidad = QtWidgets.QAction(self)
        self.Nube_Palabras = QtWidgets.QAction(self)
        self.Bigramma = QtWidgets.QAction(self)
        self.Oscuro = QtWidgets.QAction(self)
        self.Claro = QtWidgets.QAction(self)

        # BOTON CONFIGURACIONES
        self.Configuracion = QtWidgets.QMenu(self.menubar)

        self.Programas.addAction(self.BaseDeDatos)
        self.Programas.addAction(self.Muestra_Programa)
        self.Programas.addAction(self.Cortar_Fecha)
        self.Programas.addAction(self.Popularidad)
        self.Programas.addAction(self.Nube_Palabras)
        self.Programas.addAction(self.Bigramma)
        self.Apariencia.addAction(self.Oscuro)
        self.Apariencia.addAction(self.Claro)
        self.Configuracion.addAction(self.Apariencia.menuAction())
        self.menubar.addAction(self.Configuracion.menuAction())

        # BOTON AYUDA
        self.Ayuda = QtWidgets.QMenu(self.menubar)
        self.Sobre_que = QtWidgets.QAction(self)
        self.Ayuda.addAction(self.Sobre_que)

        self.menubar.addAction(self.Programas.menuAction())
        self.menubar.addAction(self.Ayuda.menuAction())
        self.menubar.addAction(self.Configuracion.menuAction())

        # FUNCIONES
        self.BARRAMENU(self)
        #self.CUADROTEXTO(self)

    def BARRAMENU(self, EXADATA):

        _translate = QtCore.QCoreApplication.translate
        self.Programas.setTitle(_translate("EXADATA", "Programas"))
        self.BaseDeDatos.setText(_translate("EXADATA", "Base de dato"))
        self.Muestra_Programa.setText(_translate("EXADATA", "Muestra"))
        self.Cortar_Fecha.setText(_translate("EXADATA", "Cortar fecha"))
        self.Popularidad.setText(_translate("EXADATA", "Popularidad"))
        self.Nube_Palabras.setText(_translate("EXADATA", "Nube De Palabras"))
        self.Bigramma.setText(_translate("EXADATA", "Bigrama"))
        self.Apariencia.setTitle(_translate("EXADATA", "Apariencia"))
        self.Oscuro.setText(_translate("EXADATA", "Oscuro"))
        self.Claro.setText(_translate("EXADATA", "Claro"))
        self.Ayuda.setTitle(_translate("EXADATA", "Ayuda"))
        self.Sobre_que.setText(_translate("EXADATA", "Sobre que"))
        self.Configuracion.setTitle(_translate("EXADATA", "Configuracion"))

        # Funciones de menu
        self.BaseDeDatos.triggered.connect(self.BASE)
        self.Muestra_Programa.triggered.connect(self.MUESTRA)
        self.Cortar_Fecha.triggered.connect(self.CORTAR)
        self.Popularidad.triggered.connect(self.INFLUYENTES)
        self.Nube_Palabras.triggered.connect(self.NUBEPALABRAS)
        self.Bigramma.triggered.connect(self.NUBEBIGRAMA)
        self.Sobre_que.triggered.connect(self.AYUDA)
        self.Oscuro.triggered.connect(self.darktheme)
        self.Claro.triggered.connect(self.lighttheme)

    def BASE(self):
        from BD import Main_DB
        self.BD = Main_DB()
        self.BD.show()
        self.hide()

    def MUESTRA(self):
        from Muestra import Main_MUESTRA
        self.ayuda = Main_MUESTRA()
        self.ayuda.show()
        self.hide()

    def CORTAR(self):
        from Cortarfecha import Main_Cortar
        self.ventana = Main_Cortar()
        self.ventana.show()
        self.hide()

    def INFLUYENTES(self):
        from Influyentes import Main_Influyentes
        self.ventana = Main_Influyentes()
        self.ventana.show()
        self.hide()

    def NUBEPALABRAS(self):
        self.ventana = Ui_MainNube()
        self.ventana.setupUi(self.ventana)
        self.ventana.show()

    def NUBEBIGRAMA(self):
        self.ventana = Ui_MainBigrama()
        self.ventana.setupUi(self.ventana)
        self.ventana.show()

    def AYUDA(self):
        from Ayuda import Main_Ayuda
        self.ayuda = Main_Ayuda()
        self.ayuda.show()
        self.hide()

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Salir",
                                     "Estas seguro que quieres salir?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def darktheme(self):
        app.setStyle('fusion')
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(60, 90, 197).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)

    def lighttheme(self):
        app.setStyle('fusion')
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(240, 240, 240))
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(255, 0, 0))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(60, 90, 197).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    palette = QtGui.QPalette()
    fuente = QFont()

    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    app.setFont(fuente)

    window = Main()
    window.show()
    sys.exit(app.exec_())
