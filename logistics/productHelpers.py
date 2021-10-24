import pymysql
from conexion import DataBase

class ProductHelper(DataBase):
    nombre = ""
    descripcion = ""
    precioVenta = 0
    precioCompra = 0
    distribuidor = ""

    def __init__(self,nombre,descripcion,precioVenta,precioCompra,distribuidor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioVenta = int(precioVenta)
        self.precioCompra =int (precioCompra)
        self.distribuidor = distribuidor

        DataBase.__init__(self)
    
    def insertar(self):

        
        sql = "INSERT INTO productos(nombre_producto,descripcion_producto,precioventa_producto,preciocompra_producto,distribuidor_producto) VALUES ('{}','{}','{}','{}','{}')".format(self.nombre,self.descripcion,self.precioVenta,self.precioCompra,self.distribuidor)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.connection.commit()
            self.cursor.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))