# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analisasGrafico.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from database import prueba
from helpers import ventasHelpers

#CLASE PARA CONSTRUIR GRAFICA CON MATPLOTLIB
class Canvas_Graficos(FigureCanvas):
        def __init__(self, parent = None):
                self.fig, self.ax = plt.subplots(1,dpi = 100, figsize=(5,5),sharey=True, facecolor= 'white')
                super().__init__(self.fig)

                nombres = ['15','25','30','35','40']
                colores = ['red','red','red','red','red']
                tamaño = [10,15,20,25,30]
                
                self.ax.bar(nombres,tamaño,color=colores)
                self.fig.suptitle('Grafica de barras',  size = 9)


class MenuAnalisisGrafico(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1166, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 1171, 91))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label_3 = QtWidgets.QLabel(self.headerFrame)
        self.label_3.setGeometry(QtCore.QRect(410, 10, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.regresarBtn = QtWidgets.QPushButton(self.headerFrame)
        self.regresarBtn.setGeometry(QtCore.QRect(30, 10, 61, 61))
        self.regresarBtn.setStyleSheet("border-image: url(:/iconos/iconoRegresar.png);")
        self.regresarBtn.setText("")
        self.regresarBtn.setObjectName("regresarBtn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 90, 1161, 661))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 821, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.grafico = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.grafico.setGeometry(QtCore.QRect(20,60,831,561))
        self.grafico.setContentsMargins(0, 0, 0, 0)
        self.grafico.setObjectName("grafico")
        self.ventasGastosBtn = QtWidgets.QPushButton(self.frame)
        self.ventasGastosBtn.setGeometry(QtCore.QRect(860, 60, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.ventasGastosBtn.setFont(font)
        self.ventasGastosBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ventasGastosBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.ventasGastosBtn.setObjectName("ventasGastosBtn")
        self.ventasMensualBtn = QtWidgets.QPushButton(self.frame)
        self.ventasMensualBtn.setGeometry(QtCore.QRect(860, 150, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.ventasMensualBtn.setFont(font)
        self.ventasMensualBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ventasMensualBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.ventasMensualBtn.setObjectName("ventasMensualBtn")
        self.pedidosMensualBtn = QtWidgets.QPushButton(self.frame)
        self.pedidosMensualBtn.setGeometry(QtCore.QRect(860, 240, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.pedidosMensualBtn.setFont(font)
        self.pedidosMensualBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pedidosMensualBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.pedidosMensualBtn.setObjectName("pedidosMensualBtn")
        self.utilidadBtn = QtWidgets.QPushButton(self.frame)
        self.utilidadBtn.setGeometry(QtCore.QRect(860, 330, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.utilidadBtn.setFont(font)
        self.utilidadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.utilidadBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.utilidadBtn.setObjectName("utilidadBtn")
        self.condicionInventarioBtn = QtWidgets.QPushButton(self.frame)
        self.condicionInventarioBtn.setGeometry(QtCore.QRect(860, 420, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.condicionInventarioBtn.setFont(font)
        self.condicionInventarioBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.condicionInventarioBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.condicionInventarioBtn.setObjectName("condicionInventarioBtn")
        self.prediccionVentasBtn = QtWidgets.QPushButton(self.frame)
        self.prediccionVentasBtn.setGeometry(QtCore.QRect(860, 520, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.prediccionVentasBtn.setFont(font)
        self.prediccionVentasBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prediccionVentasBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.prediccionVentasBtn.setObjectName("prediccionVentasBtn")
        self.graficTitleLbl = QtWidgets.QLabel(self.frame)
        self.graficTitleLbl.setGeometry(QtCore.QRect(30, 15, 500, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.graficTitleLbl.setFont(font)
        self.graficTitleLbl.setObjectName("graficTitleLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #CODIGO PAR INICIAR LA GRAFICA
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [1000,1500,2000,5000,4000,1200,2300,4200,4300,2300,2200,1200,4200,5400,2400,3000,1500,2400,3300,4000,300,4500,2400,1100,1300,4200,3200,2300,1100,1000], label='Ventas')
        sc.axes.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [500,2000,1200,2300,6000,1500,2000,3200,4100,1000,1200,5400,1000,1200,3200,4000,2000,1200,800,600,400,3200,2200,1500,1400,2000,6400,1500,800,1200], label='Pedidos')
        self.grafico.addWidget(sc)

        #GRAFICO QUE MUESTRA LA RELACION COMPRAS VENTAS
        self.ventasGastosBtn.clicked.connect(self.comprasVentas_grafico)
    def comprasVentas_grafico(self):
        for i in reversed(range(self.grafico.count())): 
               self.grafico.itemAt(i).widget().setParent(None)
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [1000,1500,2000,5000,4000,1200,2300,4200,4300,2300,2200,1200,4200,5400,2400,3000,1500,2400,3300,4000,300,4500,2400,1100,1300,4200,3200,2300,1100,1000], label='Ventas')
        sc.axes.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [500,2000,1200,2300,6000,1500,2000,3200,4100,1000,1200,5400,1000,1200,3200,4000,2000,1200,800,600,400,3200,2200,1500,1400,2000,6400,1500,800,1200], label='Pedidos')
        self.grafico.addWidget(sc)
        self.graficTitleLbl.setText("Relacion Ventas-Gastos")
        
        #GRAFICO QUE MUESTRA LAS VENTAS MENSUALES.
        self.ventasMensualBtn.clicked.connect(self.ventas_grafico)

    def ventas_grafico(self):
        helper = ventasHelpers.VentasHelper("",0,"")
        datosVentas = helper.graficar_ventas()
        print(datosVentas)
        for i in reversed(range(self.grafico.count())): 
                self.grafico.itemAt(i).widget().setParent(None)
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.plot(datosVentas[0],datosVentas[1] , label='Ventas')
        #self.grafico.deleteLater()
        self.grafico.addWidget(sc)
        totalVentas = helper.ventas_mensuales()
        totalVentas = str(totalVentas)
        totalVentas = "Venta Mensual:$" + totalVentas
        self.graficTitleLbl.setText(totalVentas)

        

        #GRAFICO QUE MUESTA LOS PEDIDOS MENSUALES.
        self.pedidosMensualBtn.clicked.connect(self.pedidos_grafico)
    def pedidos_grafico(self):
        for i in reversed(range(self.grafico.count())): 
                self.grafico.itemAt(i).widget().setParent(None)    
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], [500,2000,1200,2300,6000,1500,2000,3200,4100,1000,1200,5400,1000,1200,3200,4000,2000,1200,800,600,400,3200,2200,1500,1400,2000,6400,1500,800,1200], label='Pedidos', color= "orange")
        
        self.grafico.addWidget(sc)
        self.graficTitleLbl.setText("Compras Mensuales: $26345")    
        #GRAFICO QUE MUESTRA LA PREDICCION DE LAS VENTAS PARA LA SEMANA
        self.prediccionVentasBtn.clicked.connect(self.prediccionVentas_grafico)

                #GRAFICO QUE MUESTRA LA UTILIDAD DE LOS PRODUCTOS
        self.utilidadBtn.clicked.connect(self.utilidad_grafico)
    def utilidad_grafico(self):
        for i in reversed(range(self.grafico.count())): 
             self.grafico.itemAt(i).widget().setParent(None)
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.bar(["Pulpo", "Camaron", "Almejas", "Filete", "Ostiones", "Pescado"],[30,70,40,65,70,80],color="orange")
        self.grafico.addWidget(sc)
        self.graficTitleLbl.setText("Porcentaje de Utilidad por producto en Inventario")

        #GRAFICO QUE MUESTRA LA CONDICION DEL INVENTARIO
        self.condicionInventarioBtn.clicked.connect(self.condicionInventario_grafico)
    def condicionInventario_grafico(self):
        for i in reversed(range(self.grafico.count())): 
             self.grafico.itemAt(i).widget().setParent(None)
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.bar(["Pulpo", "Camaron", "Almejas", "Filete", "Ostiones", "Pescado"],[10,20,30,22,10,8])
        self.grafico.addWidget(sc)
        self.graficTitleLbl.setText("Estado Actual del Inventario")

        #GRAFICO QUE MUESTRA LAS PREDICCIONES DE VENTA SEMANALES
        self.prediccionVentasBtn.clicked.connect(self.prediccionVentas_grafico)

    def prediccionVentas_grafico(self):
        for i in reversed(range(self.grafico.count())): 
             self.grafico.itemAt(i).widget().setParent(None)
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.pie(labels=["Pulpo", "Camaron", "Almejas", "Filete", "Ostiones", "Pescado"], x=[10,20,30,22,10,8],autopct="%0.1f%%")
        #self.grafico = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.grafico.addWidget(sc)
        self.graficTitleLbl.setText("Ventas semanales estimadas: $25212")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Análisis Gráfico"))
        self.ventasGastosBtn.setText(_translate("MainWindow", "Relacion Ventas-Gastos"))
        self.ventasMensualBtn.setText(_translate("MainWindow", "Ventas Mensual"))
        self.pedidosMensualBtn.setText(_translate("MainWindow", "Pedidos Mensual"))
        self.utilidadBtn.setText(_translate("MainWindow", "Utilidad Productos"))
        self.condicionInventarioBtn.setText(_translate("MainWindow", "Condicion Inventario"))
        self.prediccionVentasBtn.setText(_translate("MainWindow", "Prediccion Ventas"))
        self.graficTitleLbl.setText(_translate("MainWindow", "Relacion Ventas-Gastos"))
from iconos import iconosAnalisisGrafico_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuAnalisisGrafico()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
