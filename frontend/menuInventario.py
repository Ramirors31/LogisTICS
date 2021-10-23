# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventario.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MenuInventario(object):
    def setupUi(self, inventario):
        inventario.setObjectName("inventario")
        inventario.resize(1120, 660)
        self.centralwidget = QtWidgets.QWidget(inventario)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 1121, 81))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label = QtWidgets.QLabel(self.headerFrame)
        self.label.setGeometry(QtCore.QRect(440, 10, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 1121, 581))
        self.frame.setStyleSheet("background-color: rgb(255, 244, 246);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.inventarioTable = QtWidgets.QTableWidget(self.frame)
        self.inventarioTable.setGeometry(QtCore.QRect(50, 240, 891, 192))
        self.inventarioTable.setObjectName("inventarioTable")
        self.inventarioTable.setColumnCount(7)
        self.inventarioTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.inventarioTable.setHorizontalHeaderItem(6, item)
        self.addProductoBtn = QtWidgets.QPushButton(self.frame)
        self.addProductoBtn.setGeometry(QtCore.QRect(50, 120, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addProductoBtn.setFont(font)
        self.addProductoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.addProductoBtn.setObjectName("addProductoBtn")
        self.buscarProductoText = QtWidgets.QPlainTextEdit(self.frame)
        self.buscarProductoText.setGeometry(QtCore.QRect(570, 120, 301, 51))
        self.buscarProductoText.setObjectName("buscarProductoText")
        self.buscarProductoBtn = QtWidgets.QPushButton(self.frame)
        self.buscarProductoBtn.setGeometry(QtCore.QRect(900, 120, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buscarProductoBtn.setFont(font)
        self.buscarProductoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.buscarProductoBtn.setObjectName("buscarProductoBtn")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.modificarBtn = QtWidgets.QPushButton(self.frame)
        self.modificarBtn.setGeometry(QtCore.QRect(320, 120, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modificarBtn.setFont(font)
        self.modificarBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.modificarBtn.setObjectName("modificarBtn")
        self.btnRegresar = QtWidgets.QPushButton(self.frame)
        self.btnRegresar.setGeometry(QtCore.QRect(60, 10, 101, 91))
        self.btnRegresar.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        inventario.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(inventario)
        self.statusbar.setObjectName("statusbar")
        inventario.setStatusBar(self.statusbar)

        self.retranslateUi(inventario)
        QtCore.QMetaObject.connectSlotsByName(inventario)

    def retranslateUi(self, inventario):
        _translate = QtCore.QCoreApplication.translate
        inventario.setWindowTitle(_translate("inventario", "MainWindow"))
        self.label.setText(_translate("inventario", "Inventario"))
        item = self.inventarioTable.horizontalHeaderItem(0)
        item.setText(_translate("inventario", "ID Producto"))
        item = self.inventarioTable.horizontalHeaderItem(1)
        item.setText(_translate("inventario", "Nombre Producto"))
        item = self.inventarioTable.horizontalHeaderItem(2)
        item.setText(_translate("inventario", "Precio Compra"))
        item = self.inventarioTable.horizontalHeaderItem(3)
        item.setText(_translate("inventario", "Precio Venta"))
        item = self.inventarioTable.horizontalHeaderItem(4)
        item.setText(_translate("inventario", "En Stock"))
        item = self.inventarioTable.horizontalHeaderItem(5)
        item.setText(_translate("inventario", "Distribuidor"))
        item = self.inventarioTable.horizontalHeaderItem(6)
        item.setText(_translate("inventario", "Ubicacion"))
        self.addProductoBtn.setText(_translate("inventario", "Añadir Producto"))
        self.buscarProductoBtn.setText(_translate("inventario", "Buscar Producto"))
        self.label_2.setText(_translate("inventario", "Mis Productos"))
        self.modificarBtn.setText(_translate("inventario", "Modificar/Eliminar"))
import iconosMenuInventario_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventario = QtWidgets.QMainWindow()
    ui = MenuInventario()
    ui.setupUi(inventario)
    inventario.show()
    sys.exit(app.exec_())
