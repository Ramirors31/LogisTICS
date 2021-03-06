from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from helpers import productHelpers, prediccionVentas,prediccionProductos,pedidoHelpers
from analisisGrafico import MenuAnalisisGrafico
from database import prueba
from helpers import prediccionProductos,productHelpers
import analisisDetallado
from datetime import datetime

  

#CLASE PARA CONSTRUIR GRAFICA CON MATPLOTLIB


class MenuPedidoInteligente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1550, 1300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headerFrame = QtWidgets.QFrame(self.centralwidget)
        self.headerFrame.setGeometry(QtCore.QRect(0, 0, 1550, 91))
        self.headerFrame.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.label_3 = QtWidgets.QLabel(self.headerFrame)
        self.label_3.setGeometry(QtCore.QRect(650, 10, 461, 71))
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
        self.frame.setGeometry(QtCore.QRect(0, 90, 1550, 1300))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 5, 700, 340))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.grafico = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.grafico.setContentsMargins(0, 0, 0, 0)
        self.grafico.setObjectName("grafico")

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)

        self.prediccionVentasBtn = QtWidgets.QPushButton(self.frame)
        self.prediccionVentasBtn.setGeometry(QtCore.QRect(970, 560, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.prediccionVentasBtn.setFont(font)
        self.prediccionVentasBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prediccionVentasBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(34, 170, 32);\n"
"border-radius:20px")
        self.prediccionVentasBtn.setObjectName("prediccionVentasBtn")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(600, 5, 900, 340))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.grafico_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.grafico_2.setContentsMargins(0, 0, 0, 0)
        self.grafico_2.setObjectName("grafico_2")
        self.ventaTable = QtWidgets.QTableWidget(self.frame)
        self.ventaTable.setGeometry(QtCore.QRect(50, 370, 631, 231))
        self.ventaTable.setObjectName("ventaTable")
        self.ventaTable.setColumnCount(4)
        self.ventaTable.setRowCount(0)

        self.tableHeader = self.ventaTable.horizontalHeader()
        self.tableHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ventaTable.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 330, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.analisisDetalladoBtn = QtWidgets.QPushButton(self.frame)
        self.analisisDetalladoBtn.setGeometry(QtCore.QRect(970, 460, 251, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.analisisDetalladoBtn.setFont(font)
        self.analisisDetalladoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analisisDetalladoBtn.setStyleSheet("background-color: rgb(52, 136, 140);\n"
"color: rgb(255, 244, 246);\n"
"border-radius:20px")
        self.analisisDetalladoBtn.setObjectName("analisisDetalladoBtn")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(510, 620, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #CLICK LISTENERS

        #GRAFICAMOS EL INVENTARIO
        inventarioHelper = productHelpers.ProductHelper("","","",0,0,"",0)
        datosInventario = inventarioHelper.graficar_productos()
        #print(datosInventario)
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.barh(datosInventario[0],datosInventario[1])
        self.grafico.addWidget(sc)

        #GRAFICAMOS LA PREDICCION DE LAS VENTAS
        helperPrediccion = prediccionVentas.RegresionVentas()
        datos = helperPrediccion.prediccion_semanal(22,29)
        prediccionSemanal = "Ventas Estimadas:$" + str(datos[0])
        sc = prueba.MplCanvas(self, width=5, height=4, dpi=150)
        sc.axes.plot(datos[2],datos[1], marker = "o")
        sc.axes.set_ylabel("$")
        sc.axes.set_xlabel("Dia del Mes")
        sc.axes.text(11,4650,prediccionSemanal)
        self.grafico_2.addWidget(sc)

        #PEDIDO INTELIGENTE
        self.analisis = prediccionProductos.RegresionProductos()
        dias = [self.analisis.diaCallo,self.analisis.diaCamaronC,self.analisis.diaCamaronG,self.analisis.diaFilete,self.analisis.diaAtun,self.analisis.diaOstion,self.analisis.diaPescado,self.analisis.diaPulpo]
        ventas =[self.analisis.ventaCallo,self.analisis.ventaCamaronC,self.analisis.ventaCamaronG,self.analisis.ventaFilete,self.analisis.ventaAtun,self.analisis.ventaOstion,self.analisis.ventaPescado,self.analisis.ventaPulpo]
        helper = productHelpers.ProductHelper("","","",0,0,"",0)

        predicciones = []
        sugerencias =[]
        for item in range(len(dias)):
                item = self.analisis.aplicar_regresion(dias[item],ventas[item])
                predicciones.append(item[0])
        total = 0
        inventario = helper.graficar_productos()
        productos = inventario[0]
        stock = inventario[1]
        self.pedido = []
        print(predicciones)
        for i in range(len(stock)):
                sugerenciaSemanal = predicciones[i] - stock[i]
                if (sugerenciaSemanal < 0):
                        sugerenciaSemanal = 0
                        sugerencias.append(sugerenciaSemanal)
                        
                sugerencias.append(int(sugerenciaSemanal))

        for i in range(len(productos)):
                itemPedido = []
                itemPedido.append(productos[i])
                itemPedido.append(sugerencias[i])
                helperPrecio = productHelpers.ProductHelper("",productos[i],"",0,0,"",0)
                precio = helperPrecio.buscar_precioProducto()
                itemPedido.append(precio[0])
                subtotal = precio[0] * sugerencias[i]
                itemPedido.append(subtotal)
                total = total + subtotal
                self.pedido.append(itemPedido)

        
                self.ventaTable.clearContents()
        row = 0
        for producto in self.pedido:
                self.ventaTable.setRowCount(row + 1)
                self.ventaTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(producto[0])))
                self.ventaTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(producto[1])))
                self.ventaTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(producto[2])))
                self.ventaTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(producto[3])))


                row += 1

        totalVenta =  str(total)
        self.label_5.setText(totalVenta)
        
        fecha = datetime.today().strftime('%d-%m-%Y')
        self.prediccionVentasBtn.clicked.connect(lambda:self.registrar_pedido("PEDIDO",self.label_5.text(),fecha))
       
        #REGISTRAR EL PEDIDO INTELIGENTE EN LA BASE DE DATOS
    def registrar_pedido(self,motivo,total,fecha):
            helper = pedidoHelpers.PedidoHelper(motivo,float(total),fecha)
            helper.insertar()    
            self.msgConfirmacion = QtWidgets.QMessageBox()
            self.msgConfirmacion.setWindowTitle("Pedido Confirmado")
            self.msgConfirmacion.setIcon(QtWidgets.QMessageBox.Information)
            self.msgConfirmacion.setText("El pedido se a registrado con exito")
            self.msgConfirmacion.exec_()
            self.label_5.clear()
            self.ventaTable.clearContents()
            
            helper.registrar_detalles(self.pedido, "Congeladora Mazatlan")

            self.pedido = []
                


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Pedido Inteligente"))
    
        self.prediccionVentasBtn.setText(_translate("MainWindow", "Generar Pedido"))
        item = self.ventaTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.ventaTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.ventaTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.ventaTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Subtotal"))
     
        self.label.setText(_translate("MainWindow", "Pedido Recomendado"))
        self.label_2.setText(_translate("MainWindow", "Estado Inventario"))
 
        self.analisisDetalladoBtn.setText(_translate("MainWindow", "An??lisis Detallado"))
        self.label_5.setText(_translate("MainWindow", "Total: $ 0.00"))
from iconos import iconosPedidoInteligente_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuPedidoInteligente()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())