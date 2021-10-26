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
        
helper = DistribuidorHelper("","","","")
helper.mostrar_tabla()
