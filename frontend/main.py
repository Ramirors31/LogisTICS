import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from menuInventario import MenuInventario
from login import Ui_login
from menuInicio import Ui_inicio
from menuReportes import MenuReportes
from formularioVenta import FormularioVenta
from menuLogistica import MenuLogistica
from formularioProducto import FormularioProducto

class MyApp(QtWidgets.QMainWindow):
    #FUNCION PARA CARGAR LA VENTANA INICIAL DE LOGIN
    def __init__(self):
        super(MyApp, self).__init__()
        self.login = QtWidgets.QMainWindow()
        self.ui = Ui_login()
        self.ui.setupUi(self.login)
        self.login.show()
        self.btnIniciarSesion = self.ui.pushButton
        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    #FUNCION LOGIN Y MOSTRAR MENU DE INICIO.
    def iniciar_sesion(self):
        self.menuInicio= QtWidgets.QMainWindow()
        self.ui=Ui_inicio()
        self.ui.setupUi(self.menuInicio)
        self.menuInicio.show()
        self.btnMenuReportes = self.ui.pushButton
        self.btnMenuInventario = self.ui.pushButton_2
        self.btnMenuLogistica = self.ui.pushButton_3
        self.btnMenuReportes.clicked.connect(self.menu_reportes)
        self.btnMenuInventario.clicked.connect(self.menu_inventario)
        self.btnMenuLogistica.clicked.connect(self.menu_logistica)
        self.login.hide()

    #FUNCION PARA MOSTRAR EL MENU REPORTES
    def menu_reportes(self):
        self.menuReportes= QtWidgets.QMainWindow()
        self.ui=MenuReportes()
        self.ui.setupUi(self.menuReportes)
        self.menuReportes.show()
        self.menuInicio.hide()
        self.btnRegresar = self.ui.btnRegresar
        self.btnRegresar.clicked.connect(self.regresar_reportes)
        self.btnReporteVenta = self.ui.reporteVentaBtn
        self.btnReporteVenta.clicked.connect(self.abrir_reporteVenta)

    #FUNCION PARA ABRIR UN REPORTE DE VENTA DENTRO DEL MENU VENTAS
    def abrir_reporteVenta(self):
        self.reporteVenta= QtWidgets.QMainWindow()
        self.ui=FormularioVenta()
        self.ui.setupUi(self.reporteVenta)
        self.reporteVenta.show()
        self.menuReportes.hide()
        self.btnRegresar = self.ui.regresarBtn
        self.btnRegresar.clicked.connect(self.regresar_reporteVenta)

    #FUNCIONA PARA REGRESAR AL MENU REPORTES DESDE UN REPORTE DE VENTA    
    def regresar_reporteVenta(self):
        self.reporteVenta.hide()
        self.menuReportes.show()
    
    #BOTON REGRESAR EN EL MENU REPORTES
    def regresar_reportes(self):
        self.menuReportes.hide()
        self.menuInicio.show()

       
    #FUNCION PARA MOSTRAR EL MENU INVENTARIO
    def menu_inventario(self):
        self.menuInventario = QtWidgets.QMainWindow()
        self.ui= MenuInventario()
        self.ui.setupUi(self.menuInventario)
        self.menuInventario.show()
        self.menuInicio.hide()
        self.btnRegresar = self.ui.btnRegresar
        self.btnRegresar.clicked.connect(self.regresar_inventario)
        self.btnAñadirProducto= self.ui.addProductoBtn
        self.btnAñadirProducto.clicked.connect(self.formulario_producto)


    #BOTOTN REGRESAR EN EL MENU INVENTARIO
    def regresar_inventario(self):
        self.menuInventario.hide()
        self.menuInicio.show()

    #BOTON MOSTRAR EL FORMULARIO PARA AÑADIR UN PRODUCTO
    def formulario_producto(self):
        self.formularioProducto = QtWidgets.QMainWindow()
        self.ui = FormularioProducto()
        self.ui.setupUi(self.formularioProducto)
        self.formularioProducto.show()
        self.menuInventario.hide()
        self.btnRegresar = self.ui.regresarBtn
        self.btnRegresar.clicked.connect(self.regresar_formularioProducto)

    #FUNCION PARA REGRESAR AL MENU INVENTARIO DESDE FORMULARIO DE PRODUCTO
    def regresar_formularioProducto(self):
        self.formularioProducto.hide()
        self.menuInventario.show()
    #FUNCIONA PARA MOSTRAR EL MENU LOGISTICA
    def menu_logistica(self):
        self.menuLogistica = QtWidgets.QMainWindow()
        self.ui= MenuLogistica()
        self.ui.setupUi(self.menuLogistica)
        self.menuLogistica.show()
        self.menuInicio.hide()
        self.btnRegresar = self.ui.btnRegresar
        self.btnRegresar.clicked.connect(self.regresar_logistica)

    #BOTON REGRESAR EN EL MENU LOGISTICA
    def regresar_logistica(self):
        self.menuLogistica.hide()
        self.menuInicio.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    input()

