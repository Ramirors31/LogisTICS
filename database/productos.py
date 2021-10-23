import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from ..database.productos import Ui_MainWindow
from conexion import DataBase

class Producto():
    def __init__(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addBtn.clicked.connect(self.añadirProducto)

    def añadirProducto(self):
        self.nombreProducto = self.ui.productoTxt.text()
        self.descripcion = self.ui.descripcionTxt.text()
        self.precioCompra = self.ui.precioCompra.text()
        self.precioVenta = self.ui.precioVenta.text()
        self.distribuidor = self.ui.distribuidorCombo.text()

        mensaje = QMessageBox()
        mensaje.setText('Producto: {}, Descripcion: {}, Precio Compra: {}, Precio Venta: {}, Distribuidor: {}').format(self.nombreProducto, self.descripcion, self.precioCompra, self.precioVenta, self.distribuidor)

        mensaje.exec_()

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ui_MainWindow()
    ventana.show()
    sys.exit(app.exec_())
