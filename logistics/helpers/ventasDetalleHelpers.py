from matplotlib.pyplot import connect
import pymysql
from conexion import DataBase

class DetallesVentaHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
    idventa = 0
    producto = ""
    subtotal = 0

    def __init__(self,idventa,producto,subtotal):
        self.idventa = idventa
        self.producto = producto
        self.subtotal = subtotal

        DataBase.__init__(self)
        

    #INSERTAR DETALLES DE VENTA EN LA BASE DE DATOS
    def insertar(self):
        sql = "INSERT INTO detalles_venta(id_venta,producto_venta,subtotal_venta) VALUES ('{}','{}','{}')".format(self.idventa,self.producto,self.subtotal)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.cursor.execute("SELECT id_detalle FROM detalles_venta")
            self.idVenta = self.cursor.fetchone()
            print(self.idVenta)
            self.connection.commit()
            self.cursor.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))

    def mostrar_tabla(self):
        sql = "SELECT * FROM distribuidores"
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

    #FUNCION PARA CARGAR DISTRIBUIDORES EN FORMULARIO DE VENTA
    def cargar_distribuidores(self):
        sql = "SELECT nombre_distribuidor FROM distribuidores"
        try:
            self.cursor.execute(sql)
            self.distribuidores = self.cursor.fetchall()
            listaDistribuidores = []
            for distribuidor in self.distribuidores:
                listaDistribuidores.append(distribuidor[0])

            self.connection.commit()
            self.connection.close()
            
            return listaDistribuidores

        except pymysql.Error as err:
            print("Algo salio mal", format(err))

        
ejemplo = DetallesVentaHelper(0,"",0)
print(ejemplo.cargar_distribuidores())