# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioActualizarDistribuidor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from helpers import distribuidorHelpers

class ActualizarDistribuidor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 911, 80))
        self.headerFrame.setAcceptDrops(False)
        self.headerFrame.setAutoFillBackground(False)
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label = QtWidgets.QLabel(self.headerFrame)
        self.label.setGeometry(QtCore.QRect(220, 10, 571, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.regresarBtn = QtWidgets.QPushButton(self.headerFrame)
        self.regresarBtn.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.regresarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regresarBtn.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.regresarBtn.setText("")
        self.regresarBtn.setObjectName("regresarBtn")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 911, 561))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.distribuidorTxt = QtWidgets.QTextEdit(self.frame_2)
        self.distribuidorTxt.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distribuidorTxt.setFont(font)
        self.distribuidorTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.distribuidorTxt.setObjectName("distribuidorTxt")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(20, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ubicacionTxt = QtWidgets.QTextEdit(self.frame_2)
        self.ubicacionTxt.setGeometry(QtCore.QRect(160, 90, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ubicacionTxt.setFont(font)
        self.ubicacionTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ubicacionTxt.setObjectName("ubicacionTxt")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(20, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.telefonoTxt = QtWidgets.QTextEdit(self.frame_2)
        self.telefonoTxt.setGeometry(QtCore.QRect(160, 170, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.telefonoTxt.setFont(font)
        self.telefonoTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.telefonoTxt.setObjectName("telefonoTxt")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(20, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.correoTxt = QtWidgets.QTextEdit(self.frame_2)
        self.correoTxt.setGeometry(QtCore.QRect(160, 250, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.correoTxt.setFont(font)
        self.correoTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.correoTxt.setObjectName("correoTxt")
        self.buscarBtn = QtWidgets.QPushButton(self.frame_2)
        self.buscarBtn.setGeometry(QtCore.QRect(480, 10, 41, 41))
        self.buscarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscarBtn.setStyleSheet("border-image: url(:/iconos/iconoBuscar.png);")
        self.buscarBtn.setText("")
        self.buscarBtn.setObjectName("buscarBtn")
        self.actualizarBtn = QtWidgets.QPushButton(self.frame_2)
        self.actualizarBtn.setGeometry(QtCore.QRect(530, 250, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actualizarBtn.setFont(font)
        self.actualizarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.actualizarBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(34, 170, 32);")
        self.actualizarBtn.setObjectName("actualizarBtn")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(600, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(600, 20, 181, 181))
        self.label_2.setStyleSheet("border-image: url(:/iconos/distribuidr.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.eliminarBtn = QtWidgets.QPushButton(self.frame_2)
        self.eliminarBtn.setGeometry(QtCore.QRect(710, 250, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eliminarBtn.setFont(font)
        self.eliminarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 0, 3);")
        self.eliminarBtn.setObjectName("eliminarBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.msgError = QtWidgets.QMessageBox()


        self.buscarBtn.clicked.connect(lambda: self.buscar_distribuidor())

        self.actualizarBtn.clicked.connect(lambda: self.actualizar_distribuidor())


    def buscar_distribuidor(self):
        nombre = self.distribuidorTxt.toPlainText()
        try:
            helper  = distribuidorHelpers.DistribuidorHelper(nombre,"","","")
            distribuidor = helper.buscar_registro()
            self.ubicacionTxt.setText(distribuidor[2])
            self.telefonoTxt.setText(distribuidor[3])
            self.correoTxt.setText(distribuidor[4])

        except:
            self.msgError.setText("Verifique que el producto que busca sea correcto???")
            self.msgError.setWindowTitle("Algo Salio Mal")
            self.msgError.exec_()



    def actualizar_distribuidor(self):
        nombre = self.distribuidorTxt.toPlainText()
        ubicacion = self.ubicacionTxt.toPlainText()
        telefono = self.telefonoTxt.toPlainText()
        correo = self.correoTxt.toPlainText()

        self.msgError.setText("??Seguro que desea Actualizar el producto "" {}""?".format(nombre))
        self.msgError.setIcon(QtWidgets.QMessageBox.Warning)
        self.msgError.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.msgError.setWindowTitle("Confirmacion de Actualizaci??n")
        self.msgError.exec_()
        botonConfirmar = self.msgError.button(QtWidgets.QMessageBox.Ok)
        if(self.msgError.clickedButton() == botonConfirmar):
            helper = distribuidorHelpers.DistribuidorHelper(nombre,ubicacion,telefono,correo)
            helper.actualizar_registro()

    def eliminar_distribuidor(self):
        nombre = self.distribuidorTxt.toPlainText()
        self.msgError.setText("??Seguro que desea Eliminar el producto "" {}""?".format(nombre))
        self.msgError.setIcon(QtWidgets.QMessageBox.Warning)
        self.msgError.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.msgError.setWindowTitle("Confirmacion de Eliminacion")
        self.msgError.exec_()
        botonConfirmar = self.msgError.button(QtWidgets.QMessageBox.Ok)
        if(self.msgError.clickedButton() == botonConfirmar):
            helper = distribuidorHelpers.DistribuidorHelper(nombre,"","","")
            helper.eliminar_registro()
    

        




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Buscar / Actualizar Distribuidor"))
        self.label_10.setText(_translate("MainWindow", "Distribuidor"))
        self.label_11.setText(_translate("MainWindow", "Ubicacion"))
        self.label_12.setText(_translate("MainWindow", "Tel??fono "))
        self.label_13.setText(_translate("MainWindow", "Correo"))
        self.actualizarBtn.setText(_translate("MainWindow", "Actualizar"))
        self.label_16.setText(_translate("MainWindow", "??Qu?? desea hacer?"))
        self.eliminarBtn.setText(_translate("MainWindow", "Eliminar"))
from iconos import iconosBuscarDistribuidor_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ActualizarDistribuidor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
