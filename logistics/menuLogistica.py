# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logisticayPedidos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from helpers import pedidoHelpers


class MenuLogistica(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 1151, 91))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label_3 = QtWidgets.QLabel(self.headerFrame)
        self.label_3.setGeometry(QtCore.QRect(370, 10, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 90, 1141, 621))
        self.frame.setStyleSheet("background-color: rgb(255, 246, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pedidosTable = QtWidgets.QTableWidget(self.frame)
        self.pedidosTable.setGeometry(QtCore.QRect(10, 150, 881, 301))
        self.pedidosTable.setObjectName("pedidosTable")
        self.pedidosTable.setColumnCount(7)
        self.pedidosTable.setRowCount(0)
        #HEADER DEL MENU PEDIDOS
        self.header = self.pedidosTable.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.pedidosTable.setHorizontalHeaderItem(6, item)
        self.nuevoPedidoBtn = QtWidgets.QPushButton(self.frame)
        self.nuevoPedidoBtn.setGeometry(QtCore.QRect(920, 150, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nuevoPedidoBtn.setFont(font)
        self.nuevoPedidoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nuevoPedidoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.nuevoPedidoBtn.setObjectName("nuevoPedidoBtn")
        self.pedidoInteligenteBtn = QtWidgets.QPushButton(self.frame)
        self.pedidoInteligenteBtn.setGeometry(QtCore.QRect(920, 330, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pedidoInteligenteBtn.setFont(font)
        self.pedidoInteligenteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pedidoInteligenteBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.pedidoInteligenteBtn.setObjectName("pedidoInteligenteBtn")

        self.actualizarPedidoBtn = QtWidgets.QPushButton(self.frame)
        self.actualizarPedidoBtn.setGeometry(QtCore.QRect(920, 240, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actualizarPedidoBtn.setFont(font)
        self.actualizarPedidoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.actualizarPedidoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 136, 135);")
        self.actualizarPedidoBtn.setObjectName("actualizarPedidoBtn")
        self.btnRegresar = QtWidgets.QPushButton(self.headerFrame)
        self.btnRegresar.setGeometry(QtCore.QRect(40, 10, 91, 81))
        self.btnRegresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegresar.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #CARGAR DATOS EN LA TABLA
        tablaHelper = pedidoHelpers.PedidoHelper("",0,"","","","","")
        listaPedidos = tablaHelper.mostrar_tabla()
        self.pedidosTable.clearContents()
        row = 0
        for pedido in listaPedidos:
                self.pedidosTable.setRowCount(row + 1)
                self.pedidosTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(pedido[1])))
                self.pedidosTable.setItem(row, 1, QtWidgets.QTableWidgetItem(pedido[2]))
                self.pedidosTable.setItem(row, 2, QtWidgets.QTableWidgetItem(pedido[3]))
                self.pedidosTable.setItem(row, 3, QtWidgets.QTableWidgetItem(pedido[7]))
                self.pedidosTable.setItem(row, 4, QtWidgets.QTableWidgetItem(pedido[5]))
                self.pedidosTable.setItem(row, 5, QtWidgets.QTableWidgetItem((pedido[4])))
                self.pedidosTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(pedido[6])))

                row += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Log??stica y Pedidos"))
        self.label_4.setText(_translate("MainWindow", "Historial de Pedidos"))
        item = self.pedidosTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Pedido"))
        item = self.pedidosTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha Pedido"))
        item = self.pedidosTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.pedidosTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Forma de Pago"))
        item = self.pedidosTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Distribuidor"))
        item = self.pedidosTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha Llegada"))
        item = self.pedidosTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Total ($)"))
        self.nuevoPedidoBtn.setText(_translate("MainWindow", "Nuevo Pedido"))
        self.actualizarPedidoBtn.setText(_translate("MainWindow", "Actualizar Pedido"))
        self.pedidoInteligenteBtn.setText(_translate("MainWindow", "Pedido Inteligente"))
from iconos import iconosMenuLogistica_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuLogistica()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
