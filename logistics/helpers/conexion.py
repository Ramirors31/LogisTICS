import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='logisticsdb'
        )
        try:
            self.cursor =self.connection.cursor()
            print("Conexion establecida exitosamente")

        except pymysql.Error as err:
            print("Algo salio mal ",format(err))


