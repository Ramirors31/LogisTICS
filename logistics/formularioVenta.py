# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioVenta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime
import pymysql

from helpers import ventasHelpers, distribuidorHelpers,productHelpers,ventasDetalleHelpers



class FormularioVenta(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 741, 91))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label_3 = QtWidgets.QLabel(self.headerFrame)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 701, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 90, 731, 801))
        self.frame.setStyleSheet("background-color: rgb(255, 248, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(350, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ventaTable = QtWidgets.QTableWidget(self.frame)
        self.ventaTable.setGeometry(QtCore.QRect(80, 300, 540, 231))
        self.ventaTable.setObjectName("ventaTable")
        self.ventaTable.setColumnCount(4)
        self.ventaTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(3, item)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(420, 580, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(20, 570, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.completarVentaBtn = QtWidgets.QPushButton(self.frame)
        self.completarVentaBtn.setGeometry(QtCore.QRect(360, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.completarVentaBtn.setFont(font)
        self.completarVentaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.completarVentaBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.completarVentaBtn.setObjectName("completarVentaBtn")
        self.facturaBtn = QtWidgets.QPushButton(self.frame)
        self.facturaBtn.setGeometry(QtCore.QRect(160, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.facturaBtn.setFont(font)
        self.facturaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facturaBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.facturaBtn.setObjectName("facturaBtn")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 30, 141, 131))
        self.label.setStyleSheet("border-image: url(:/iconos/iconoVenta.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.regresarBtn = QtWidgets.QPushButton(self.headerFrame)
        self.regresarBtn.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.regresarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regresarBtn.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.regresarBtn.setText("")
        self.regresarBtn.setObjectName("regresarBtn")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(510, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.fechaTxt = QtWidgets.QLabel(self.frame)
        self.fechaTxt.setGeometry(QtCore.QRect(590, 43, 111, 16))
        self.fechaTxt.setFont(font)
        self.fechaTxt.setObjectName("fechaTxt")
        #OBTENIENDO FECHA DEL SISTEMA
        fecha = datetime.today().strftime('%d-%m-%Y')
        self.fechaTxt.setText(fecha)
        self.productoCombo = QtWidgets.QComboBox(self.frame)
        self.productoCombo.setGeometry(QtCore.QRect(130, 170, 160, 30))
        self.productoCombo.setObjectName("productoCombo")

        #OBTENIENDO INFORMACION DEL PARA COMBOBOX DESDE NUESTRA BASE DE DATOS
        helperProductos = productHelpers.ProductHelper("","","",0,0,"",0)
        valores = helperProductos.cargar_combobox()
        for i in range(len(valores)):
                producto = valores[i]
                self.productoCombo.addItem(producto)





        self.cantidadTextEdit = QtWidgets.QTextEdit(self.frame)
        self.cantidadTextEdit.setGeometry(QtCore.QRect(500, 170, 141, 31))
        self.cantidadTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cantidadTextEdit.setObjectName("cantidadTextEdit")
        self.addVentaBtn = QtWidgets.QPushButton(self.frame)
        self.addVentaBtn.setGeometry(QtCore.QRect(350, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addVentaBtn.setFont(font)
        self.addVentaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addVentaBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(34, 170, 32);")
        self.addVentaBtn.setObjectName("addVentaBtn")
        self.eliminarVentaBtn = QtWidgets.QPushButton(self.frame)
        self.eliminarVentaBtn.setGeometry(QtCore.QRect(500, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eliminarVentaBtn.setFont(font)
        self.eliminarVentaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarVentaBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 0, 3);")
        self.eliminarVentaBtn.setObjectName("eliminarVentaBtn")
        self.formaPagoCombo = QtWidgets.QComboBox(self.frame)
        self.formaPagoCombo.setGeometry(QtCore.QRect(160, 580, 151, 22))
        self.formaPagoCombo.setObjectName("formaPagoCombo")
        self.formaPagoCombo.addItem("")
        self.formaPagoCombo.addItem("")
        self.formaPagoCombo.addItem("")
        self.totalVentaTxt = QtWidgets.QLabel(self.frame)
        self.totalVentaTxt.setGeometry(QtCore.QRect(520, 580, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalVentaTxt.setFont(font)
        self.totalVentaTxt.setObjectName("totalVentaTxt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.completarVentaBtn.clicked.connect(lambda: self.registrar_venta("VENTA", self.totalVenta,self.fechaTxt.text()))

        #BOTON AÑADIR PRODUCTO A PEDIDO ACTUAL
        self.addVentaBtn.clicked.connect(lambda: self.addRow_venta(self.productoCombo.currentText(),30,int(self.cantidadTextEdit.toPlainText()),0))
        self.ventaTable.clearContents()
        self.listPedido = []

        #BOTON ELIMINAR PRODUCTO DE PEDIDO ACTUAL
        self.eliminarVentaBtn.clicked.connect(self.deleteRow_venta)
        #TOTAL DE VENTA
        self.totalVenta = 0

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
        #AÑADIENDO PRODUCTOS A LA TABLA DE VENTA LOCAL
    def addRow_venta(self,producto,precioUnitario,cantidad,subtotal):
                subtotal = cantidad * precioUnitario
                self.totalVenta = self.totalVenta + subtotal
                fila = [producto, precioUnitario, cantidad, subtotal]
                self.listPedido.append(fila)
                row = 0
                for producto in self.listPedido:
                        self.ventaTable.setRowCount(row + 1)
                        self.ventaTable.setItem(row, 0, QtWidgets.QTableWidgetItem(producto[0])) 
                        self.ventaTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(producto[1]))) 
                        self.ventaTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2]))) 
                        self.ventaTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3]))) 

                        row += 1
                totalVenta = "$"+ str(self.totalVenta)
                self.totalVentaTxt.setText(totalVenta)

        #FUNCION PARA ELIMINAR UNA FILA DEL VENTA ACTUAL
    def deleteRow_venta(self):
            self.listPedido.pop()
            row = 0
            for producto in self.listPedido:
                        self.ventaTable.setRowCount(row + 1)
                        self.ventaTable.setItem(row, 0, QtWidgets.QTableWidgetItem(producto[0])) 
                        self.ventaTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(producto[1]))) 
                        self.ventaTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2]))) 
                        self.ventaTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3]))) 

                        row += 1
            totalVenta = "$"+ str(self.totalVenta)
            self.totalVentaTxt.setText(totalVenta)
            



        #BOTON PARA REGISTRAR VENTA EN BASE DE DATOS
           
        #FUNCION PARA REGISTRAR REPORTE DE VENTA EN LA TABLA REPORTES.
    def registrar_venta(self, motivo, cantidad, fecha):
        try:   
                helper =  ventasHelpers.VentasHelper(motivo,float(cantidad),fecha)
                helper.insertar()
                self.msg = QtWidgets.QMessageBox()
                self.msg.setWindowTitle("Confirmacion Registro")
                self.msg.setText("Venta Registrada con éxito")
                self.cantidadTextEdit.clear()
                self.totalVentaTxt.clear() 
                self.ventaTable.clearContents()

                #AÑADIMOS DETALLES DE VENTA A LA TABLA DETALLES DE VENTA
                helper.registrar_detalles(self.listPedido)
                
                self.listPedido = []
                self.msg.exec_()
        except pymysql.Error as err:
                print("Algo salio mal:", format(err))
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Reporte Venta"))
        self.label_8.setText(_translate("MainWindow", "Producto:"))
        self.label_9.setText(_translate("MainWindow", "Cantidad:"))
        item = self.ventaTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.ventaTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.ventaTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.ventaTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Subtotal"))
        self.label_10.setText(_translate("MainWindow", "Total:"))
        self.label_11.setText(_translate("MainWindow", "Forma Pago"))
        self.completarVentaBtn.setText(_translate("MainWindow", "Completar Venta"))
        self.facturaBtn.setText(_translate("MainWindow", "Solicitar Factura"))
        self.label_6.setText(_translate("MainWindow", "Fecha:"))
        """self.productoCombo.setItemText(0, _translate("MainWindow", "Camaron"))
        self.productoCombo.setItemText(1, _translate("MainWindow", "Pulpo KG"))
        self.productoCombo.setItemText(2, _translate("MainWindow", "Almeja PZ"))
        self.productoCombo.setItemText(3, _translate("MainWindow", "Atun Medallon PZ"))"""
        self.addVentaBtn.setText(_translate("MainWindow", "Añadir "))
        self.eliminarVentaBtn.setText(_translate("MainWindow", "Eliminar"))
        self.formaPagoCombo.setItemText(0, _translate("MainWindow", "Efectivo"))
        self.formaPagoCombo.setItemText(1, _translate("MainWindow", "Tarjeta Credito/ Débito"))
        self.formaPagoCombo.setItemText(2, _translate("MainWindow", "Transferencia Bancaria"))
        self.totalVentaTxt.setText(_translate("MainWindow", "$0"))
from iconos import iconosReporteVenta_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FormularioVenta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
