# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioModificarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import productHelpers


class FormularioModificar(object):
    def setupUi(self, ModificarEliminarProducto):
        ModificarEliminarProducto.setObjectName("ModificarEliminarProducto")
        ModificarEliminarProducto.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(ModificarEliminarProducto)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.headerFrame.setAcceptDrops(False)
        self.headerFrame.setAutoFillBackground(False)
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label = QtWidgets.QLabel(self.headerFrame)
        self.label.setGeometry(QtCore.QRect(170, 10, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnRegresar = QtWidgets.QPushButton(self.headerFrame)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 10, 50, 50))
        self.btnRegresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegresar.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 811, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 15, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.productoTxt = QtWidgets.QTextEdit(self.frame)
        self.productoTxt.setGeometry(QtCore.QRect(170, 15, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productoTxt.setFont(font)
        self.productoTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.productoTxt.setObjectName("productoTxt")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 135, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nombreProductoTxt = QtWidgets.QTextEdit(self.frame)
        self.nombreProductoTxt.setGeometry(QtCore.QRect(170, 85, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nombreProductoTxt.setFont(font)
        self.nombreProductoTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nombreProductoTxt.setObjectName("nombreProductoTxt")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.distribuidorText = QtWidgets.QTextEdit(self.frame)
        self.distribuidorText.setGeometry(QtCore.QRect(170, 160, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distribuidorText.setFont(font)
        self.distribuidorText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.distribuidorText.setObjectName("distribuidorText")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 410, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.precioCompraTxt = QtWidgets.QTextEdit(self.frame)
        self.precioCompraTxt.setGeometry(QtCore.QRect(170, 245, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precioCompraTxt.setFont(font)
        self.precioCompraTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.precioCompraTxt.setObjectName("precioCompraTxt")
        self.precioVentaTxt = QtWidgets.QTextEdit(self.frame)
        self.precioVentaTxt.setGeometry(QtCore.QRect(170, 325, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precioVentaTxt.setFont(font)
        self.precioVentaTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.precioVentaTxt.setObjectName("precioVentaTxt")
        self.descripcionTxt = QtWidgets.QTextEdit(self.frame)
        self.descripcionTxt.setGeometry(QtCore.QRect(170,400,191,41))
        self.descripcionTxt.setFont(font)
        self.descripcionTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.stockTxt = QtWidgets.QTextEdit(self.frame)
        self.stockTxt.setGeometry(QtCore.QRect(170,475,191,41))
        self.stockTxt.setFont(font)
        self.stockTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.btnBuscar = QtWidgets.QPushButton(self.frame)
        self.btnBuscar.setGeometry(QtCore.QRect(380, 10, 41, 41))
        self.btnBuscar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscar.setStyleSheet("border-image: url(:/iconos/iconoBuscar.png);")
        self.btnBuscar.setText("")
        self.btnBuscar.setObjectName("btnBuscar")
        self.modificarBtn = QtWidgets.QPushButton(self.frame)
        self.modificarBtn.setGeometry(QtCore.QRect(440, 330, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modificarBtn.setFont(font)
        self.modificarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificarBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(34, 170, 32);")
        self.modificarBtn.setObjectName("modificarBtn")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(500, 40, 221, 221))
        self.label_7.setStyleSheet("border-image: url(:/iconos/inventarioIcono.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20,85,80,40))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font)
        self.stockLabel = QtWidgets.QLabel(self.frame)
        self.stockLabel.setGeometry(QtCore.QRect(20,480,80,40))
        self.stockLabel.setText("")
        self.stockLabel.setObjectName("stockLabel")
        self.stockLabel.setFont(font)
        self.eliminarBtn = QtWidgets.QPushButton(self.frame)
        self.eliminarBtn.setGeometry(QtCore.QRect(610, 330, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eliminarBtn.setFont(font)
        self.eliminarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 0, 3);")
        self.eliminarBtn.setObjectName("eliminarBtn")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(510, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        ModificarEliminarProducto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ModificarEliminarProducto)
        self.statusbar.setObjectName("statusbar")
        ModificarEliminarProducto.setStatusBar(self.statusbar)

        self.retranslateUi(ModificarEliminarProducto)
        QtCore.QMetaObject.connectSlotsByName(ModificarEliminarProducto)

        #MENSAJE DE ERROR
        self.msgError = QtWidgets.QMessageBox()
        self.msgError.setWindowTitle("Algo Salio Mal")

        #FUNCION PARA BUSCAR PRODUCTO EN LA BASE DE DATOS
        self.btnBuscar.clicked.connect(self.buscar_producto)
        
    def buscar_producto(self):
        try:
            self.idProducto = self.productoTxt.toPlainText()
            helper = productHelpers.ProductHelper(self.idProducto,"","",0,0,"",0)
            resultado = helper.buscar_registro()
            self.productoTxt.setText(resultado[0])
            self.nombreProductoTxt.setText(resultado[1])
            self.descripcionTxt.setText(resultado[2])
            self.precioVentaTxt.setText(str(resultado[3]))
            self.precioCompraTxt.setText(str(resultado[4]))
            self.distribuidorText.setText(resultado[5])
            self.stockTxt.setText(str(resultado[6]))
        except:
            self.msgError.setText("El producto que tratas de buscar no existe")
            self.msgError.exec_()

        #FUNCION PARA ELIMINAR PRODUCTO
        self.eliminarBtn.clicked.connect(self.eliminar_producto)

    def eliminar_producto(self):
        try:
             self.idProducto = self.productoTxt.toPlainText()
             helper = productHelpers.ProductHelper(self.idProducto,"","",0,0,"",0)
             eliminar = helper.eliminar_registro()
             self.descripcionTxt.clear()
             self.stockTxt.clear()
             self.productoTxt.clear()
             self.precioVentaTxt.clear()
             self.precioCompraTxt.clear()
             self.nombreProductoTxt.clear()
             self.distribuidorText.clear()

            
        except:
            self.msgError.setText("El producto que tratas de eliminar no existe")
            self.msgError.exec_()
            
    def refresh(self,component):
        component.setText("")

    def retranslateUi(self, ModificarEliminarProducto):
        _translate = QtCore.QCoreApplication.translate
        ModificarEliminarProducto.setWindowTitle(_translate("ModificarEliminarProducto", "MainWindow"))
        self.label.setText(_translate("ModificarEliminarProducto", "Modificar/ Eliminar Producto"))
        self.label_2.setText(_translate("ModificarEliminarProducto", "ID Producto:"))
        self.label_3.setText(_translate("ModificarEliminarProducto", "Precio Compra:"))
        self.label_4.setText(_translate("ModificarEliminarProducto", "Distribuidor:"))
        self.label_5.setText(_translate("ModificarEliminarProducto", "Precio Venta:"))
        self.label_6.setText(_translate("ModificarEliminarProducto", "Descripcion:"))
        self.modificarBtn.setText(_translate("ModificarEliminarProducto", "Modificar"))
        self.eliminarBtn.setText(_translate("ModificarEliminarProducto", "Eliminar"))
        self.label_8.setText(_translate("ModificarEliminarProducto", "¿Que desea hacer?"))
        self.label_9.setText(_translate("ModificarEliminarProducto", "Nombre:"))
        self.stockLabel.setText(_translate("ModificarEliminarProducto", "Stock:"))
from iconos import iconosModificarProducto_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModificarEliminarProducto = QtWidgets.QMainWindow()
    ui = FormularioModificar()
    ui.setupUi(ModificarEliminarProducto)
    ModificarEliminarProducto.show()
    sys.exit(app.exec_())
