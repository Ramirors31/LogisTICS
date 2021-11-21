from PyQt5.QtCore import pyqtRemoveInputHook
import pymysql
from pymysql import cursors
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
            return format(err)

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
            print(tabRows)
                
            return tabRows
        except pymysql.Error as err:
            print("Algo salio mal:".format(err))
        

    #BUSCAR DATOS PARA MODIFICAR O ELIMINAR UN REGISTRO
    def buscar_registro(self):
        sql = ("SELECT * FROM productos WHERE idproducto='{}'").format(self.codigoProducto)
        try:
            self.cursor.execute(sql)
            self.busqueda =self.cursor.fetchone()
            self.connection.commit()
            self.connection.close()
            resultadoBusqueda = self.busqueda
            return resultadoBusqueda
        except pymysql.Error as err:
            print("Algo salio mal:", format(err))

    #FUNCION PARA ELIMINAR UN REGISTRO DE LA TABLA PRODUCTOS
    def eliminar_registro(self):
        sql = ("DELETE FROM productos WHERE idproducto='{}'").format(self.codigoProducto)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except pymysql.Error as err:
            print("Algo salio mal", format(err))
    #FUNCION PARA ACTUALIZAR ALGUN PRODUCTO
    def actualizar_registro(self):
        sql = "UPDATE productos SET (idproducto,nombre_producto,descripcion_producto,precioventa_producto,preciocompra_producto,distribuidor_producto,stock_producto) VALUES ('{}','{}','{}','{}','{}','{}','{}') WHERE idproducto = '{}'".format(self.codigoProducto,self.nombre,self.descripcion,self.precioVenta,self.precioCompra,self.distribuidor,self.stock,self.codigoProducto)        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except pymysql.Error as err:
            print("Algo salio mal ",format(err))

    #FUNCION PARA GRAFICAR PRODUCTOS EN EL INVENTARIO
    def graficar_productos(self):
        sql = "SELECT nombre_producto, stock_producto FROM productos"
        productos = []
        stock = []
        datosInventario = []
        try:
            self.cursor.execute(sql)
            self.data = self.cursor.fetchall()

            for i in range(len(self.data)):
                item = list(self.data[i])
                productos.append(item[0])
                stock.append(item[1])
                #print(item)

            datosInventario.append(productos)
            datosInventario.append(stock)

            self.connection.commit()
            self.connection.close()
            return datosInventario


        except pymysql.Error as err:
            print("Algo salio mal: ", format(err))


    #FUNCION PARA CARGAR PRODUCTOS EN COMBO BOX
    def cargar_combobox(self):
        sql = "SELECT nombre_producto FROM productos"
        try:
            self.cursor.execute(sql)
            self.productos = self.cursor.fetchall()
            listaProductos = []
            for producto in self.productos:
                listaProductos.append(producto[0])

            self.connection.commit()
            self.connection.close()
            
            return listaProductos

        except pymysql.Error as err:
            print("Algo salio mal", format(err))

    #FUNCION PARA BUSCAR UN REGISTRO EN ANALISIS DETALLADO
    def buscar_producto(self):
        sql = ("SELECT * FROM productos WHERE nombre_producto='{}'").format(self.nombre)
        try:
            self.cursor.execute(sql)
            self.busqueda =self.cursor.fetchone()
            self.connection.commit()
            self.connection.close()
            resultadoBusqueda = self.busqueda
            return resultadoBusqueda
        except pymysql.Error as err:
            print("Algo salio mal:", format(err))

    #FUNCION PARA RECUPERAR PRECIO DE PRODUCTOS 
    def buscar_precioProducto(self):
        sql = ("SELECT preciocompra_producto FROM productos WHERE nombre_producto='{}'").format(self.nombre)
        try:
            self.cursor.execute(sql)
            self.busqueda =self.cursor.fetchone()
            self.connection.commit()
            self.connection.close()
            resultadoBusqueda = self.busqueda
            return resultadoBusqueda
        except pymysql.Error as err:
            print("Algo salio mal:", format(err))



ejemplo = ProductHelper("","","",0,0,"",0)
