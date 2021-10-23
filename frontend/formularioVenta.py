# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioVenta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class FormularioVenta(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 855)
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
        self.frame.setGeometry(QtCore.QRect(0, 90, 731, 771))
        self.frame.setStyleSheet("background-color: rgb(255, 248, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.productoComboBox = QtWidgets.QComboBox(self.frame)
        self.productoComboBox.setGeometry(QtCore.QRect(120, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productoComboBox.setFont(font)
        self.productoComboBox.setObjectName("productoComboBox")
        self.productoComboBox.addItem("")
        self.productoComboBox.addItem("")
        self.productoComboBox.addItem("")
        self.productoComboBox.addItem("")
        self.productoComboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(330, 250, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cantidadTxt = QtWidgets.QTextEdit(self.frame)
        self.cantidadTxt.setGeometry(QtCore.QRect(430, 240, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cantidadTxt.setFont(font)
        self.cantidadTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cantidadTxt.setObjectName("cantidadTxt")
        self.ventaTable = QtWidgets.QTableWidget(self.frame)
        self.ventaTable.setGeometry(QtCore.QRect(50, 320, 631, 221))
        self.ventaTable.setObjectName("ventaTable")
        self.ventaTable.setColumnCount(5)
        self.ventaTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(4, item)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(430, 580, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.totalTxt = QtWidgets.QTextEdit(self.frame)
        self.totalTxt.setGeometry(QtCore.QRect(510, 570, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalTxt.setFont(font)
        self.totalTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.totalTxt.setObjectName("totalTxt")
        self.addBtn = QtWidgets.QPushButton(self.frame)
        self.addBtn.setGeometry(QtCore.QRect(530, 240, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.addBtn.setObjectName("addBtn")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(50, 570, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formaPagoCombo = QtWidgets.QComboBox(self.frame)
        self.formaPagoCombo.setGeometry(QtCore.QRect(170, 570, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.formaPagoCombo.setFont(font)
        self.formaPagoCombo.setObjectName("formaPagoCombo")
        self.formaPagoCombo.addItem("")
        self.formaPagoCombo.addItem("")
        self.formaPagoCombo.addItem("")
        self.completarVentaBtn = QtWidgets.QPushButton(self.frame)
        self.completarVentaBtn.setGeometry(QtCore.QRect(150, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.completarVentaBtn.setFont(font)
        self.completarVentaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.completarVentaBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.completarVentaBtn.setObjectName("completarVentaBtn")
        self.facturaBtn = QtWidgets.QPushButton(self.frame)
        self.facturaBtn.setGeometry(QtCore.QRect(410, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.facturaBtn.setFont(font)
        self.facturaBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facturaBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.facturaBtn.setObjectName("facturaBtn")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 20, 231, 171))
        self.label.setStyleSheet("border-image: url(:/iconoVenta/venta.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.regresarBtn = QtWidgets.QPushButton(self.frame)
        self.regresarBtn.setGeometry(QtCore.QRect(30, 20, 81, 81))
        self.regresarBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regresarBtn.setStyleSheet("border-image: url(:/iconoVenta/iconoRegresar.png);")
        self.regresarBtn.setText("")
        self.regresarBtn.setObjectName("regresarBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Reporte Venta"))
        self.label_8.setText(_translate("MainWindow", "Producto:"))
        self.productoComboBox.setItemText(0, _translate("MainWindow", "Camarón(KG)"))
        self.productoComboBox.setItemText(1, _translate("MainWindow", "Pulpo(KG)"))
        self.productoComboBox.setItemText(2, _translate("MainWindow", "Almejas(PZ)"))
        self.productoComboBox.setItemText(3, _translate("MainWindow", "Pescado(KG)"))
        self.productoComboBox.setItemText(4, _translate("MainWindow", "Filete Pescado(KG)"))
        self.label_9.setText(_translate("MainWindow", "Cantidad:"))
        item = self.ventaTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Num. Venta"))
        item = self.ventaTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.ventaTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.ventaTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.ventaTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Subtotal"))
        self.label_10.setText(_translate("MainWindow", "Total:"))
        self.addBtn.setText(_translate("MainWindow", "Añadir "))
        self.label_11.setText(_translate("MainWindow", "Forma Pago"))
        self.formaPagoCombo.setItemText(0, _translate("MainWindow", "Efectivo"))
        self.formaPagoCombo.setItemText(1, _translate("MainWindow", "Tarjeta de Crédito/Debito"))
        self.formaPagoCombo.setItemText(2, _translate("MainWindow", "Transferencia Bancaria"))
        self.completarVentaBtn.setText(_translate("MainWindow", "Completar Venta"))
        self.facturaBtn.setText(_translate("MainWindow", "Solicitar Factura"))
from iconos import iconosVenta_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FormularioVenta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
