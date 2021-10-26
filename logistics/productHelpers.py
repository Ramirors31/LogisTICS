import pymysql
from conexion import DataBase

class ProductHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
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

    #INSERTAR PRODUCTOS EN LA BASE DE DATOS
    def insertar(self):

        sql = "INSERT INTO productos(nombre_producto,descripcion_producto,precioventa_producto,preciocompra_producto,distribuidor_producto) VALUES ('{}','{}','{}','{}','{}')".format(self.nombre,self.descripcion,self.precioVenta,self.precioCompra,self.distribuidor)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.connection.commit()
            self.cursor.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))

    #CARGAR DATOS A LA TABLA PRODUCTOS
    def mostrar_tabla(self):
        sql = "SELECT * FROM productos"
        try:
            self.cursor.execute(sql)
            self.rows = self.cursor.fetchall()
            tabRows = []
            for row in self.rows:
                tabRows.append(row)
                self.connection.commit() 
                
            self.connection.close()
            return tabRows
        except pymysql.Error as err:
            print("Algo Salio mal ", format(err))
        

