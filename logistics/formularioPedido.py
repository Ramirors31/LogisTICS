# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioPedido.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from helpers import pedidoHelpers,distribuidorHelpers, productHelpers


class FormularioPedido(object):
    def setupUi(self, FormularioPedido):
        FormularioPedido.setObjectName("FormularioPedido")
        FormularioPedido.resize(780, 867)
        self.centralwidget = QtWidgets.QWidget(FormularioPedido)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 781, 91))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label_3 = QtWidgets.QLabel(self.headerFrame)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 701, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 90, 781, 781))
        self.frame.setStyleSheet("background-color: rgb(255, 248, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(560, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(650, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        #OBTENIENDO FECHA DEL SISTEMA   
        fecha = datetime.today().strftime('%d-%m-%Y')
        self.label_7.setText(fecha)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(460, 230, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        

        #OBTENIENDO PRODUCTOS DE LA BASE DE DATOS PARA COMBOBOX     
        self.productoComboBox = QtWidgets.QComboBox(self.frame)
        self.productoComboBox.setGeometry(QtCore.QRect(590, 230, 131, 22))

        helperProductos = productHelpers.ProductHelper("","","",0,0,"",0)
        valores = helperProductos.cargar_combobox()
        productos = []
        for i in range(len(valores)):
                producto = valores[i]
                self.productoComboBox.addItem(producto)

        
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 300, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cantidadTextEdit = QtWidgets.QTextEdit(self.frame)
        self.cantidadTextEdit.setGeometry(QtCore.QRect(160, 300, 151, 31))
        self.cantidadTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cantidadTextEdit.setObjectName("cantidadTextEdit")
        self.pedidoTable = QtWidgets.QTableWidget(self.frame)
        self.pedidoTable.setGeometry(QtCore.QRect(150, 360, 501, 221))
        self.pedidoTable.setObjectName("pedidoTable")
        self.pedidoTable.setColumnCount(4)
        self.pedidoTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pedidoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidoTable.setHorizontalHeaderItem(3, item)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(500, 620, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.addPedidoBtn = QtWidgets.QPushButton(self.frame)
        self.addPedidoBtn.setGeometry(QtCore.QRect(460, 290, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPedidoBtn.setFont(font)
        self.addPedidoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addPedidoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(34, 170, 32);")
        self.addPedidoBtn.setObjectName("addPedidoBtn")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(40, 610, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formaPagoCombo = QtWidgets.QComboBox(self.frame)
        self.formaPagoCombo.setGeometry(QtCore.QRect(190, 620, 131, 22))
        self.formaPagoCombo.setObjectName("formaPagoCombo")
        self.formaPagoCombo.addItem("")
        self.formaPagoCombo.addItem("")
        self.formaPagoCombo.addItem("")
        self.registrarPedidoBtn = QtWidgets.QPushButton(self.frame)
        self.registrarPedidoBtn.setGeometry(QtCore.QRect(310, 680, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.registrarPedidoBtn.setFont(font)
        self.registrarPedidoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registrarPedidoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.registrarPedidoBtn.setObjectName("registrarPedidoBtn")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.distribudorCombo = QtWidgets.QComboBox(self.frame)
        self.distribudorCombo.setGeometry(QtCore.QRect(160, 230, 180, 30))
        self.distribudorCombo.setObjectName("distribuidorCombo")

        #AÑADIR ELEMENTOS AL COMBO BOX  
        helperDistribuidor = distribuidorHelpers.DistribuidorHelper("","","","")
        valores = helperDistribuidor.cargar_distribuidores()
        for i in range(len(valores)):
                distribuidor = valores[i]
                self.distribudorCombo.addItem(distribuidor)

        
        #CARGANDO LISTA DE PRODUCTOS DE LA BASE DE DATOS
        

        self.btnRegresar = QtWidgets.QPushButton(self.frame)
        self.btnRegresar.setGeometry(QtCore.QRect(50, 30, 71, 71))
        self.btnRegresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegresar.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(330, 30, 131, 131))
        self.label.setStyleSheet("border-image: url(:/iconos/iconoPedido.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.totalTxt = QtWidgets.QLabel(self.frame)
        self.totalTxt.setGeometry(QtCore.QRect(600, 620, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalTxt.setFont(font)
        self.totalTxt.setObjectName("totalTxt")
        self.eliminarPedidoBtn = QtWidgets.QPushButton(self.frame)
        self.eliminarPedidoBtn.setGeometry(QtCore.QRect(600, 290, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eliminarPedidoBtn.setFont(font)
        self.eliminarPedidoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarPedidoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 0, 3);")
        self.eliminarPedidoBtn.setObjectName("eliminarPedidoBtn")
        FormularioPedido.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FormularioPedido)
        self.statusbar.setObjectName("statusbar")
        FormularioPedido.setStatusBar(self.statusbar)

        self.retranslateUi(FormularioPedido)
        QtCore.QMetaObject.connectSlotsByName(FormularioPedido)

        #BOTON AÑADIR PRODUCTO A PEDIDO ACTUAL
        self.addPedidoBtn.clicked.connect(lambda: self.addRow_pedido(self.productoComboBox.currentText(),30,int(self.cantidadTextEdit.toPlainText()),0))
        self.pedidoTable.clearContents()
        self.listPedido = []

        #BOTON ELIMINAR PRODUCTO DE PEDIDO ACTUAL
        self.eliminarPedidoBtn.clicked.connect(self.deleteRow_pedido)
        #TOTAL DE VENTA
        self.totalVenta = 0

        #REGISTRAR EL PEDIDO EN LA BASE DE DATOS
        self.registrarPedidoBtn.clicked.connect(lambda:self.registrar_pedido("PEDIDO",self.totalVenta,self.label_7.text()))
    
    def registrar_pedido(self,motivo,total,fecha):
            helper = pedidoHelpers.PedidoHelper(motivo,float(total),fecha)
            helper.insertar()    
            self.msgConfirmacion = QtWidgets.QMessageBox()
            self.msgConfirmacion.setWindowTitle("Pedido Confirmado")
            self.msgConfirmacion.setIcon(QtWidgets.QMessageBox.Information)
            self.msgConfirmacion.setText("El pedido se a registrado con exito")
            self.msgConfirmacion.exec_()
            self.totalTxt.clear()
            self.cantidadTextEdit.clear()
            self.pedidoTable.clearContents()
            distribuidor = self.distribudorCombo.currentText()
            helper.registrar_detalles(self.listPedido, distribuidor)

            self.listPedido = []

    def retranslateUi(self, FormularioPedido):
        _translate = QtCore.QCoreApplication.translate
        FormularioPedido.setWindowTitle(_translate("FormularioPedido", "MainWindow"))
        self.label_3.setText(_translate("FormularioPedido", "Reporte Pedido"))
        self.label_6.setText(_translate("FormularioPedido", "Fecha:"))
        self.label_8.setText(_translate("FormularioPedido", "Producto:"))
        self.label_9.setText(_translate("FormularioPedido", "Cantidad:"))
        item = self.pedidoTable.horizontalHeaderItem(0)
        item.setText(_translate("FormularioPedido", "Producto"))
        item = self.pedidoTable.horizontalHeaderItem(1)
        item.setText(_translate("FormularioPedido", "Precio Unitario"))
        item = self.pedidoTable.horizontalHeaderItem(2)
        item.setText(_translate("FormularioPedido", "Cantidad"))
        item = self.pedidoTable.horizontalHeaderItem(3)
        item.setText(_translate("FormularioPedido", "Subtotal"))
        self.label_10.setText(_translate("FormularioPedido", "Total:"))
        self.addPedidoBtn.setText(_translate("FormularioPedido", "Añadir "))
        self.label_11.setText(_translate("FormularioPedido", "Forma Pago"))
        self.formaPagoCombo.setItemText(0, _translate("FormularioPedido", "Efectivo"))
        self.formaPagoCombo.setItemText(1, _translate("FormularioPedido", "Tarjeta de Crédito/Debito"))
        self.formaPagoCombo.setItemText(2, _translate("FormularioPedido", "Transferencia Bancaria"))
        self.registrarPedidoBtn.setText(_translate("FormularioPedido", "Registrar Pedido"))
        self.label_12.setText(_translate("FormularioPedido", "Distribuidor:"))
        self.totalTxt.setText(_translate("FormularioPedido", "$200"))
        self.eliminarPedidoBtn.setText(_translate("FormularioPedido", "Eliminar"))
        
        

        #AÑADIENDO PRODUCTOS A LA TABLA DE PEDIDO LOCAL
    def addRow_pedido(self,producto,precioUnitario,cantidad,subtotal):
                subtotal = cantidad * precioUnitario
                self.totalVenta = self.totalVenta + subtotal
                fila = [producto, precioUnitario, cantidad, subtotal]
                self.listPedido.append(fila)
                row = 0
                for producto in self.listPedido:
                        self.pedidoTable.setRowCount(row + 1)
                        self.pedidoTable.setItem(row, 0, QtWidgets.QTableWidgetItem(producto[0])) 
                        self.pedidoTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(producto[1]))) 
                        self.pedidoTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2]))) 
                        self.pedidoTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3]))) 

                        row += 1
                totalVenta = "$"+ str(self.totalVenta)
                self.totalTxt.setText(totalVenta)

        #FUNCION PARA ELIMINAR UNA FILA DEL PEDIDO ACTUAL
    def deleteRow_pedido(self):
            self.listPedido.pop()
            row = 0
            for producto in self.listPedido:
                        self.pedidoTable.setRowCount(row + 1)
                        self.pedidoTable.setItem(row, 0, QtWidgets.QTableWidgetItem(producto[0])) 
                        self.pedidoTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(producto[1]))) 
                        self.pedidoTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2]))) 
                        self.pedidoTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3]))) 

                        row += 1
            totalVenta = "$"+ str(self.totalVenta)
            self.totalTxt.setText(totalVenta)



from iconos import iconosReportePedido_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formularioPedido = QtWidgets.QMainWindow()
    ui = FormularioPedido()
    ui.setupUi(formularioPedido)
    formularioPedido.show()
    sys.exit(app.exec_())
