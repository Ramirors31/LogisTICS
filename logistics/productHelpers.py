import pymysql
from conexion import DataBase

class ProductHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
    codigoProducto = ""
    nombre = ""
    descripcion = ""
    precioVenta = 0
    precioCompra = 0
    distribuidor = ""
    stock = 0

    def __init__(self,codigoProducto,nombre,descripcion,precioVenta,precioCompra,distribuidor,stock):
        self.codigoProducto = codigoProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioVenta = int(precioVenta)
        self.precioCompra =int (precioCompra)
        self.distribuidor = distribuidor
        self.stock = int(stock)

        DataBase.__init__(self)

    #INSERTAR PRODUCTOS EN LA BASE DE DATOS
    def insertar(self):

        sql = "INSERT INTO productos(idproducto,nombre_producto,descripcion_producto,precioventa_producto,preciocompra_producto,distribuidor_producto,stock_producto) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(self.codigoProducto,self.nombre,self.descripcion,self.precioVenta,self.precioCompra,self.distribuidor,self.stock)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.connection.commit()
            self.cursor.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))

    #CARGAR DATOS A LA TABLA PRODUCTOS DENTRO DEL MENU INVENTARIO
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
        

    #BUSCAR DATOS PARA MODIFICAR O ELIMINAR UN REGISTRO
    def buscar_registro(self,id):
        self.id = id
        sql = ("SELECT * FROM productos WHERE idproducto='{}'").format(self.id)
        try:
            self.cursor.execute(sql)
            self.busqueda =self.cursor.fetchone()
            self.connection.commit()
            self.connection.close()
            resultadoBusqueda = self.busqueda
            return resultadoBusqueda
        except pymysql.Error as err:
            print("Algo salio mal", format(err))

    def eliminar_registro(self,id):
        self.id = id
        sql = ("DELETE FROM productos WHERE idproducto='{}'").format(self.id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except pymysql.Error as err:
            print("Algo salio mal", format(err))
            
