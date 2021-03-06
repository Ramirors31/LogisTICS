from matplotlib.pyplot import connect
import pymysql
from conexion import DataBase

class DistribuidorHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
    nombre = ""
    ubicacion = ""
    telefono = ""
    contacto = ""

    def __init__(self,nombre,ubicacion,telefono,contacto):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.contacto = contacto

        DataBase.__init__(self)
        

    #INSERTAR DISTRIBUIDORES NUEVOS EN LA BASE DE DATOS
    def insertar(self):

        sql = "INSERT INTO distribuidores(nombre_distribuidor,ubicacion_distribuidor,telefono_distribuidor,contacto_distribuidor) VALUES ('{}','{}','{}','{}')".format(self.nombre,self.ubicacion,self.telefono,self.contacto)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
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



    #BUSCAR DATOS PARA MODIFICAR O ELIMINAR UN REGISTRO
    def buscar_registro(self):
        sql = ("SELECT * FROM distribuidores WHERE nombre_distribuidor='{}'").format(self.nombre)
        try:
            self.cursor.execute(sql)
            self.busqueda =self.cursor.fetchone()
            self.connection.commit()
            self.connection.close()
            resultadoBusqueda = self.busqueda
            return resultadoBusqueda
        except pymysql.Error as err:
            print("Algo salio mal:", format(err))

    #FUNCION PARA ELIMINAR UN REGISTRO DE LA TABLA DISTRIBUIDORES
    def eliminar_registro(self):
        sql = ("DELETE FROM distribuidores WHERE nombre_distribuidor='{}'").format(self.nombre)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except pymysql.Error as err:
            print("Algo salio mal", format(err))
    #FUNCION PARA ACTUALIZAR ALGUN PRODUCTO
    def actualizar_registro(self):
        sql = "UPDATE distribuidores SET nombre_distribuidor = '{}',ubicacion_distribuidor = '{}',telefono_distribuidor = '{}',contacto_distribuidor = '{}' WHERE nombre_distribuidor = '{}'".format(self.nombre, self.ubicacion,self.telefono,self.contacto,self.nombre)        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
            print("Modificacion Exitosa", self.telefono)
        except pymysql.Error as err:
            print("Algo salio mal ",format(err))

        
ejemplo = DistribuidorHelper("","","","")
print(ejemplo.cargar_distribuidores())
