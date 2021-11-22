
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from menuInventario import MenuInventario
from login import Login
from menuInicio import MenuInicio
from menuReportes import MenuReportes
from formularioVenta import FormularioVenta
from menuLogistica import MenuLogistica
from formularioProducto import FormularioProducto
from menuDistribuidores import MenuDistribuidores
from formularioDistribuidor import FormularioDistribuidor
from formularioPedido import FormularioPedido
from formularioModificarProducto import FormularioModificar
from analisisGrafico import MenuAnalisisGrafico
from pedidoInteligente import MenuPedidoInteligente
from analisisDetallado import AnalisisDetallado
from menuPrincipal import MenuPrincipal
from formularioActualizarDistribuidor import ActualizarDistribuidor

class MyApp(QtWidgets.QMainWindow):
    #FUNCION PARA CARGAR LA VENTANA INICIAL DE LOGIN
    def __init__(self):
        super(MyApp, self).__init__()
        self.login = QtWidgets.QMainWindow()
        self.ui = Login()
        self.ui.setupUi(self.login)
        self.login.show()
        self.btnIniciarSesion = self.ui.pushButton
        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    #FUNCION LOGIN Y MOSTRAR MENU DE INICIO.

    def iniciar_sesion(self):
        
        user = self.ui.userTextEdit.text()
        password= self.ui.passwordTextEdit.text()
        
        if(user == "1" and password == "123"):
            self.menuInicio= QtWidgets.QMainWindow()
            self.ui=MenuPrincipal()
            self.ui.setupUi(self.menuInicio)
            self.menuInicio.show()
            self.login.hide()
            self.ui.menuReportesBtn.clicked.connect(self.menu_reportes)
            self.ui.menuInventarioBtn.clicked.connect(self.menu_inventario)
            self.ui.menuDistribuidoresBtn.clicked.connect(self.menu_distribuidores)
            self.ui.menuAnalisisGraficoBtn.clicked.connect(self.menu_analisisGrafico)
            self.ui.menuPedidosBtn.clicked.connect(self.menu_logistica)


        else:
                self.ui.label_6.setText("Usuario o contraseña invalidos. Vuelva a intentar")

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
        self.btnAnalisisGrafico = self.ui.analisisGraficoBtn
        self.btnAnalisisGrafico.clicked.connect(self.menu_analisisGrafico)

    #FUNCION PARA ABRIR UN REPORTE DE VENTA DENTRO DEL MENU VENTAS
    def abrir_reporteVenta(self):
        self.reporteVenta= QtWidgets.QMainWindow(self.menuReportes)
        self.ui=FormularioVenta()
        self.ui.setupUi(self.reporteVenta)
        self.reporteVenta.show()
        self.menuReportes.hide()
        self.btnRegresar = self.ui.regresarBtn
        self.btnRegresar.clicked.connect(self.regresar_reporteVenta)
        

    #FUNCIONA PARA REGRESAR AL MENU REPORTES DESDE UN REPORTE DE VENTA    
    def regresar_reporteVenta(self):
        self.reporteVenta.close()
        self.menu_reportes()
    
    #BOTON REGRESAR EN EL MENU REPORTES
    def regresar_reportes(self):
        self.menuReportes.hide()
        self.menuInicio.show()

    #BOTON PARA ABRIR EL MENU ANALISIS GRAFICO
    def menu_analisisGrafico(self):
        self.menuAnalisisGrafico = QtWidgets.QMainWindow()
        self.ui = MenuAnalisisGrafico()
        self.ui.setupUi(self.menuAnalisisGrafico)
        self.menuAnalisisGrafico.show()
        self.menuInicio.hide()
        self.btnRegresar = self.ui.regresarBtn
        self.btnRegresar.clicked.connect(self.regresar_menuPrincipalGraficos)

    #FUNCION PARA REGRESAR AL MENU REPORTES DESDE EL MENU ANALISIS GRAFICO
    def regresar_menuPrincipalGraficos(self):
        self.menuAnalisisGrafico.hide()
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
        self.ui.modificarBtn.clicked.connect(self.formulario_modificarProducto)

    
    #BOTON PARA FORMULARIO MODIFICAR PRODUCTO
    def formulario_modificarProducto(self):
        self.formularioModificar = QtWidgets.QMainWindow()
        self.ui = FormularioModificar()
        self.ui.setupUi(self.formularioModificar)
        self.menuInventario.hide()
        self.formularioModificar.show()
        self.ui.btnRegresar.clicked.connect(self.regresar_formularioModProducto)

    #BOTON PARA REGRESAR A MENU INVENTARIO DESDE MODIFICAR PRODUCTO
    def regresar_formularioModProducto(self):
        self.formularioModificar.close()
        self.menu_inventario()

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
        self.formularioProducto.close()
        self.menu_inventario()
    #FUNCIONA PARA MOSTRAR EL MENU LOGISTICA Y PEDIDOS
    def menu_logistica(self):
        self.menuLogistica = QtWidgets.QMainWindow()
        self.ui= MenuLogistica()
        self.ui.setupUi(self.menuLogistica)
        self.menuLogistica.show()
        self.menuInicio.hide()
        self.btnRegresar = self.ui.btnRegresar
        self.btnRegresar.clicked.connect(self.regresar_logistica)
        self.ui.nuevoPedidoBtn.clicked.connect(self.nuevo_pedido)
        self.ui.pedidoInteligenteBtn.clicked.connect(self.pedido_inteligente)

    #FUNCION PARA ABRIR MENU PEDIDO INTELIGENTE DESDE MENU LOGISTICA
    def pedido_inteligente(self):
        self.pedidoInteligente = QtWidgets.QMainWindow()
        self.ui = MenuPedidoInteligente()
        self.ui.setupUi(self.pedidoInteligente)
        self.menuLogistica.hide()
        self.pedidoInteligente.show()
        self.ui.regresarBtn.clicked.connect(self.regresar_logistica_inteligente)
        self.ui.analisisDetalladoBtn.clicked.connect(self.detalle_pedidoInteligente)

    #FUNCION PARA REGRESAR AL MENU LOGISTICA DESDE EL MENU PEDIDO INTELIGENTE
    def regresar_logistica_inteligente(self):
        self.pedidoInteligente.hide()
        self.menuLogistica.show()

    #FUNCION PARA ABRIR EL ANALISIS DETALLADO DEL PEDIDO INTELIGENTE.
    def detalle_pedidoInteligente(self):
        self.detallePedidoInteligente = QtWidgets.QMainWindow()
        self.ui = AnalisisDetallado()
        self.ui.setupUi(self.detallePedidoInteligente)
        self.pedidoInteligente.hide()
        self.detallePedidoInteligente.show()
        self.ui.regresarBtn.clicked.connect(self.regresar_detalle_inteligente)

    #FUNCION PARA REGRESAR AL PEDIDO INTELIGENTE DESDE DETALLES PEDIDO INTELIGENTE
    def regresar_detalle_inteligente(self):
        self.detallePedidoInteligente.hide()
        self.pedidoInteligente.show()

    #BOTON PARA ABRIR EL FORMULARIO PARA UN NUEVO PEDIDO
    def nuevo_pedido(self):
        self.formularioPedido = QtWidgets.QMainWindow()
        self.ui = FormularioPedido()
        self.ui.setupUi(self.formularioPedido)
        self.formularioPedido.show()
        self.menuLogistica.close()
        self.ui.btnRegresar.clicked.connect(self.regresar_pedido)

    #BOTON PARA REGRESAR AL MENU LOGISTICA DESDE FORMULARIO PARA PEDIDO
    def regresar_pedido(self):
        self.menu_logistica()
        self.formularioPedido.hide()
        
    #BOTON REGRESAR EN EL MENU LOGISTICA
    def regresar_logistica(self):
        self.menuLogistica.hide()
        self.menuInicio.show()
    
    #FUNCION PARA ABRIR EL MENU DISTRIBUIDORES
    def menu_distribuidores(self):
        self.menuDistribuidores = QtWidgets.QMainWindow()
        self.ui = MenuDistribuidores()
        self.ui.setupUi(self.menuDistribuidores)
        self.menuInicio.hide()
        self.menuDistribuidores.show()
        self.ui.btnRegresar.clicked.connect(self.regresar_menuDistribuidoresPrincipal)
        self.ui.nuevoDistribuidorBtn.clicked.connect(self.formulario_distribuidor)
        self.ui.actualizarDistribuidorBtn.clicked.connect(self.actualizar_distribuidor)

    #FUNCION PARA REGRESAR AL MENU PRINCIPAL DESDE EL MENU DISTRIBUIDORES
    def regresar_menuDistribuidoresPrincipal(self):
        self.menuDistribuidores.hide()
        self.menuInicio.show()

    #FUNCION PARA MOSTRAR EL FORMULARIO PARA AÑADIR UN NUEVO DISTRIBUIDOR
    def formulario_distribuidor(self):
        self.formularioDistribuidor = QtWidgets.QMainWindow()
        self.ui = FormularioDistribuidor()
        self.ui.setupUi(self.formularioDistribuidor)
        self.menuDistribuidores.close()
        self.formularioDistribuidor.show()
        self.ui.regresarBtn.clicked.connect(self.regresar_distribuidores)


    #FUNCION PARA ABRIR EL FORMULARIO PARA BUSCAR O ACTUALIZAR UN DISTRIBUIDOR
    def actualizar_distribuidor(self):
        self.actualizarDistribuidor = QtWidgets.QMainWindow()
        self.ui = ActualizarDistribuidor()
        self.ui.setupUi(self.actualizarDistribuidor)
        self.menuDistribuidores.close()
        self.actualizarDistribuidor.show()
        self.ui.regresarBtn.clicked.connect(self.regresar_actualizarDistribuidor)

    #FUNCION PARA REGRESAR AL MENU DISTRIBUIDOR DESDE EL FORMULARIO PARA BUSCAR
    def regresar_actualizarDistribuidor(self):
        self.actualizarDistribuidor.close()
        self.menu_distribuidores()

    #FUNCION PARA VOLVER AL MENU DISTRIBUIDORES DESDE EL FORMULARIO DISTRIBUIDOR.
    def regresar_distribuidores(self):
        self.formularioDistribuidor.hide()
        self.menuDistribuidores.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    input()

