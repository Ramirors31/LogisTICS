import pymysql
from conexion import DataBase

class PedidoHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
    motivo = ""
    cantidad = 0
    fecha = ""

    def __init__(self,motivo,cantidad,fecha):
        self.motivo = motivo
        self.cantidad = cantidad
        self.fecha = fecha
    

        DataBase.__init__(self)
        

    #INSERTAR REPORTE DE PEDIDO NUEVO EN LA TABLA REPORTES
    def insertar(self):

        sql = "INSERT INTO reportes(motivo_reporte,cantidad_reporte,fecha_reporte) VALUES ('{}','{}','{}')".format(self.motivo,self.cantidad,self.fecha)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.connection.commit()
            self.cursor.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))