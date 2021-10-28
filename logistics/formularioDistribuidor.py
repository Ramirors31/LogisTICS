# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioDistribuidor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import distribuidorHelpers

class FormularioDistribuidor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 711, 91))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label_3 = QtWidgets.QLabel(self.headerFrame)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 701, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.FormularioDistribuidor = QtWidgets.QFrame(self.centralwidget)
        self.FormularioDistribuidor.setGeometry(QtCore.QRect(0, 90, 701, 721))
        self.FormularioDistribuidor.setStyleSheet("background-color: rgb(255, 248, 249);")
        self.FormularioDistribuidor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FormularioDistribuidor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FormularioDistribuidor.setObjectName("FormularioDistribuidor")
        self.label_12 = QtWidgets.QLabel(self.FormularioDistribuidor)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.FormularioDistribuidor)
        self.label_13.setGeometry(QtCore.QRect(20, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_19 = QtWidgets.QLabel(self.FormularioDistribuidor)
        self.label_19.setGeometry(QtCore.QRect(20, 460, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.contactoTxt = QtWidgets.QTextEdit(self.FormularioDistribuidor)
        self.contactoTxt.setGeometry(QtCore.QRect(250, 450, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contactoTxt.setFont(font)
        self.contactoTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.contactoTxt.setObjectName("contactoTxt")
        self.addBtn = QtWidgets.QPushButton(self.FormularioDistribuidor)
        self.addBtn.setGeometry(QtCore.QRect(250, 610, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBtn.setFont(font)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.addBtn.setObjectName("addBtn")
        self.nombreTxt = QtWidgets.QTextEdit(self.FormularioDistribuidor)
        self.nombreTxt.setGeometry(QtCore.QRect(250, 230, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nombreTxt.setFont(font)
        self.nombreTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nombreTxt.setObjectName("nombreTxt")
        self.ubicacionTxt = QtWidgets.QTextEdit(self.FormularioDistribuidor)
        self.ubicacionTxt.setGeometry(QtCore.QRect(250, 300, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ubicacionTxt.setFont(font)
        self.ubicacionTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ubicacionTxt.setObjectName("ubicacionTxt")
        self.regresarBtn = QtWidgets.QPushButton(self.FormularioDistribuidor)
        self.regresarBtn.setGeometry(QtCore.QRect(30, 30, 81, 71))
        self.regresarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regresarBtn.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.regresarBtn.setText("")
        self.regresarBtn.setObjectName("regresarBtn")
        self.label_20 = QtWidgets.QLabel(self.FormularioDistribuidor)
        self.label_20.setGeometry(QtCore.QRect(20, 370, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.telefonoTxt = QtWidgets.QTextEdit(self.FormularioDistribuidor)
        self.telefonoTxt.setGeometry(QtCore.QRect(250, 370, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.telefonoTxt.setFont(font)
        self.telefonoTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.telefonoTxt.setObjectName("telefonoTxt")
        self.label = QtWidgets.QLabel(self.FormularioDistribuidor)
        self.label.setGeometry(QtCore.QRect(290, 20, 161, 151))
        self.label.setStyleSheet("border-image: url(:/iconos/distribuidr.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #LLAMANDO A LA FUNCION AÑADIR AL PULSAR BOTON
        self.addBtn.clicked.connect(lambda: self.añadir_distribuidor(self.nombreTxt.toPlainText(),
        self.ubicacionTxt.toPlainText(),self.telefonoTxt.toPlainText(),self.contactoTxt.toPlainText()))

    def añadir_distribuidor(self,nombre,ubicacion,telefono,contacto):
        helper = distribuidorHelpers.DistribuidorHelper(nombre,ubicacion,telefono,contacto)
        print(nombre)
        helper.insertar() 
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Confirmacion Registro")
        self.msg.setText("Distribuidor Registrado con éxito")
        self.refresh = ""
        self.telefonoTxt.setText(self.refresh) 
        self.nombreTxt.setText(self.refresh) 
        self.contactoTxt.setText(self.refresh) 
        self.ubicacionTxt.setText(self.refresh)
        self.msg.exec_()
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Añadir Distribuidor"))
        self.label_12.setText(_translate("MainWindow", "Nombre:"))
        self.label_13.setText(_translate("MainWindow", "Ubicacion:"))
        self.label_19.setText(_translate("MainWindow", "Contacto:"))
        self.addBtn.setText(_translate("MainWindow", "Añadir DIstribuidor"))
        self.label_20.setText(_translate("MainWindow", "Telefono:"))
from iconos import iconosAñadirDistribuidor_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FormularioDistribuidor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
