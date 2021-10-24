import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='logisticsdb'
        )

        self.cursor =self.connection.cursor()

        print("Conexion establecida exitosamente")



