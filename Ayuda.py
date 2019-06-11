# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BD.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction, qApp,QFrame,QLabel,QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from Home import Main
import sys


class Main_Ayuda(QMainWindow):
    def __init__(self, parent=None):
        super(Main_Ayuda, self).__init__(parent)
        self.setWindowTitle("EXADATA (AYUDA)")
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


        # LOGO
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # CUADRO TEXTO
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 780, 480))

    def Home(self):
        from Home import Main
        self.ventana = Main()
        self.ventana.show()
        self.ventana.setWindowState(Qt.WindowNoState)


    def closeEvent(self,event):
        close = QMessageBox.question(self,"Salir",
                                     "Estas seguro que quieres salir de la Ayuda?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            print("cerro")
            self.Home()
        else:
            print("")

    def retranslateUi(self, MainBD):
        _translate = QtCore.QCoreApplication.translate


    def CUADROTEXTO(self):
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setHtml(("MainBD",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Ayuda de EXADATA</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p align=\"justify\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">¿Cómo cambiar el tema de EXADATA?</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">El tema oscuro permite disminuir el brillo de la pantalla, para utilizar EXADATA con un fondo oscuro.  Pero además posee la opción de utilizar un fondo claro, y se realiza de la siguiente forma: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Seleccionar la pestaña configuración. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Posicionar el mouse sobre la pestaña apariencia. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Escoger entre el tema oscuro y claro del programa. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">      </span></p>\n"
"<p align=\"justify\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">¿Cómo limpiar una base?</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Cuando hablamos de limpiar una base, nos referimos a quitar de un CSV todos aquellos tweets (líneas de la base) que se repitan. Para esto no es necesario utilizar ninguna de las aplicaciones, puesto que EXADATA posee la capacidad de limpiar la base cuando la subimos/importamos al programa. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p align=\"justify\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Subir/Importar bases de datos (CSV) a la aplicación</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Para poder subir una base de datos a EXADATA debemos tener en consideración, que el programa solo acepta archivos en formato CSV.  Para poder hacerlo debemos seguir los siguientes pasos: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Seleccionamos la pestaña programas. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Una vez se despliegue el menú de programas, elegimos Base de datos donde se despliega una nueva ventana. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Para subir un archivo CSV y visualizarlo en la tabla de EXADATA, nos ubicamos en la parte superior derecha en donde debemos escribir el nombre con el que queremos guardar la base. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Una vez escrito el nombre, podemos seleccionar el botón importar desde donde podremos seleccionar el archivo CSV desde nuestro computador. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    5.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">El programa nos pregunta si queremos guardar la base con dicho nombre, para que aparezca en el programa, debemos seleccionar 'Yes'. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    6.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Si el archivo se ha subido correctamente nos muestra una alerta a la que debemos poner ok. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">¿Cómo eliminar una base de la tabla de EXADATA?</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Eliminar base nos sirve para despejar la tabla del programa cuando no necesitemos utilizar las bases que ya se encuentran almacenadas, para hacerlo debemos seguir estos pasos: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Seleccionar el nombre de la tabla que deseamos eliminar, pinchando sobre su nombre. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Presionamos el botón Eliminar base que se encuentra en la esquina inferior derecha. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Nos aparece una alerta que nos avisa si estamos seguros o no de borrar la base en cuestión. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Si la respuesta es YES, la base es quitada de la tabla de EXADATA. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">¿Cómo unir dos o más bases?   </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> EXADATA posee la capacidad de juntar distintas bases en una sola, para poder realizar un análisis de bases afines, es por eso que posee una función extra de unión de bases. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Esto se realiza de la siguiente forma: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Subimos la base la cual queremos sea la base raíz a la cual se unirán las otras bases, si es que no tenemos la base en EXADATA. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">La seleccionamos, y la opción Agregar base </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Se despliega una ventana para seleccionar la base que queremos pegar. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Seleccionamos el archivo y se debe seleccionar Abrir. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    5.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Ahora la base raíz puede trabajarse como cualquier otra dentro de la aplicación, además tenemos la opción de exportarla. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))




if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle('fusion')
    palette = QtGui.QPalette()
    fuente = QFont()

    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")
    app.setFont(fuente)

    window = Main_Ayuda()
    window.show()
    sys.exit(app.exec_())


