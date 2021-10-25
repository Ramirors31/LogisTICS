# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuInicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from menuReportes import Ui_menuReportes
#from logisticayPedidos import Ui_MainWindow
#from inventario import Ui_inventario 


class MenuInicio(object):
    def setupUi(self, inicio):
        inicio.setObjectName("inicio")
        inicio.resize(1094, 679)
        self.centralwidget = QtWidgets.QWidget(inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 1091, 80))
        self.headerFrame.setAcceptDrops(False)
        self.headerFrame.setAutoFillBackground(False)
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label = QtWidgets.QLabel(self.headerFrame)
        self.label.setGeometry(QtCore.QRect(340, 10, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.contentFrame = QtWidgets.QFrame(self.centralwidget)
        self.contentFrame.setGeometry(QtCore.QRect(0, 80, 1091, 581))
        self.contentFrame.setStyleSheet("background-color: rgb(255, 251, 252);")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.label_2 = QtWidgets.QLabel(self.contentFrame)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 201, 201))
        self.label_2.setStyleSheet("border-image: url(:/Imagenes/graficos.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.contentFrame)
        self.label_3.setGeometry(QtCore.QRect(460, 100, 201, 201))
        self.label_3.setStyleSheet("border-image: url(:/Imagenes/inventario.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.contentFrame)
        self.label_4.setGeometry(QtCore.QRect(780, 110, 201, 201))
        self.label_4.setStyleSheet("border-image: url(:/Imagenes/pedidos.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.contentFrame)
        self.pushButton.setGeometry(QtCore.QRect(90, 360, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(118, 136, 135);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.contentFrame)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 360, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(118, 136, 135);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.contentFrame)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 360, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(118, 136, 135);")
        self.pushButton_3.setObjectName("pushButton_3")
        inicio.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(inicio)
        self.statusbar.setObjectName("statusbar")
        inicio.setStatusBar(self.statusbar)

        self.retranslateUi(inicio)
        QtCore.QMetaObject.connectSlotsByName(inicio)

 


    def retranslateUi(self, inicio):
        _translate = QtCore.QCoreApplication.translate
        inicio.setWindowTitle(_translate("inicio", "MainWindow"))
        self.label.setText(_translate("inicio", "Bienvenido a LogisTICS"))
        self.pushButton.setText(_translate("inicio", "Gráficos y Reportes"))
        self.pushButton_2.setText(_translate("inicio", "Inventario"))
        self.pushButton_3.setText(_translate("inicio", "Logistica y Pedidos"))


from iconos import Imagenes_rc 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inicio = QtWidgets.QMainWindow()
    ui = MenuInicio()
    ui.setupUi(inicio)
    inicio.show()
    sys.exit(app.exec_())