# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formularioProducto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class FormularioProducto(object):
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
        self.label_3.setGeometry(QtCore.QRect(180, 10, 701, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.FormularioProducto = QtWidgets.QFrame(self.centralwidget)
        self.FormularioProducto.setGeometry(QtCore.QRect(0, 90, 701, 721))
        self.FormularioProducto.setStyleSheet("background-color: rgb(255, 248, 249);")
        self.FormularioProducto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FormularioProducto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FormularioProducto.setObjectName("FormularioProducto")
        self.label_12 = QtWidgets.QLabel(self.FormularioProducto)
        self.label_12.setGeometry(QtCore.QRect(20, 200, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.FormularioProducto)
        self.label_13.setGeometry(QtCore.QRect(20, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_18 = QtWidgets.QLabel(self.FormularioProducto)
        self.label_18.setGeometry(QtCore.QRect(20, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.distribuidorCombo = QtWidgets.QComboBox(self.FormularioProducto)
        self.distribuidorCombo.setGeometry(QtCore.QRect(250, 490, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distribuidorCombo.setFont(font)
        self.distribuidorCombo.setObjectName("distribuidorCombo")
        self.distribuidorCombo.addItem("")
        self.distribuidorCombo.addItem("")
        self.distribuidorCombo.addItem("")
        self.label_19 = QtWidgets.QLabel(self.FormularioProducto)
        self.label_19.setGeometry(QtCore.QRect(20, 430, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.precioVentaTxt = QtWidgets.QTextEdit(self.FormularioProducto)
        self.precioVentaTxt.setGeometry(QtCore.QRect(250, 420, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precioVentaTxt.setFont(font)
        self.precioVentaTxt.setObjectName("precioVentaTxt")
        self.addBtn = QtWidgets.QPushButton(self.FormularioProducto)
        self.addBtn.setGeometry(QtCore.QRect(240, 610, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.addBtn.setObjectName("addBtn")
        self.productoTxt = QtWidgets.QTextEdit(self.FormularioProducto)
        self.productoTxt.setGeometry(QtCore.QRect(250, 190, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productoTxt.setFont(font)
        self.productoTxt.setObjectName("productoTxt")
        self.descripcionTxt = QtWidgets.QTextEdit(self.FormularioProducto)
        self.descripcionTxt.setGeometry(QtCore.QRect(250, 270, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descripcionTxt.setFont(font)
        self.descripcionTxt.setObjectName("descripcionTxt")
        self.regresarBtn = QtWidgets.QPushButton(self.FormularioProducto)
        self.regresarBtn.setGeometry(QtCore.QRect(30, 30, 81, 71))
        self.regresarBtn.setStyleSheet("border-image: url(:/iconoProducto_rc/iconoRegresar.png);")
        self.regresarBtn.setText("")
        self.regresarBtn.setObjectName("regresarBtn")
        self.label_20 = QtWidgets.QLabel(self.FormularioProducto)
        self.label_20.setGeometry(QtCore.QRect(20, 360, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.precioCompraTxt = QtWidgets.QTextEdit(self.FormularioProducto)
        self.precioCompraTxt.setGeometry(QtCore.QRect(250, 350, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.precioCompraTxt.setFont(font)
        self.precioCompraTxt.setObjectName("precioCompraTxt")
        self.label = QtWidgets.QLabel(self.FormularioProducto)
        self.label.setGeometry(QtCore.QRect(300, 30, 131, 121))
        self.label.setStyleSheet("border-image: url(:/iconoProducto_rc/iconoProducto.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Añadir Producto"))
        self.label_12.setText(_translate("MainWindow", "Nombre Producto:"))
        self.label_13.setText(_translate("MainWindow", "Descripcion: "))
        self.label_18.setText(_translate("MainWindow", "Distribuidor"))
        self.distribuidorCombo.setItemText(0, _translate("MainWindow", "Congeladora Mazatlan"))
        self.distribuidorCombo.setItemText(1, _translate("MainWindow", "Mariscos Monterrey"))
        self.distribuidorCombo.setItemText(2, _translate("MainWindow", "Distribuidora Un Nuevo Mundo"))
        self.label_19.setText(_translate("MainWindow", "Precio Venta:"))
        self.addBtn.setText(_translate("MainWindow", "Añadir Producto"))
        self.label_20.setText(_translate("MainWindow", "Precio Compra"))
import Iconos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FormularioProducto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
