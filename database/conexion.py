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

    def select_all_users(self):
         sql = 'SELECT usuario, contraseña FROM usuarios'

         try:
             self.cursor.execute(sql)
             users = self.cursor.fetchall()

             for user in users:
                 print("Usuario:",user[0])
                 print("Contraseña:",user[1])

         except Exception as e:
            raise

database = DataBase()

database.select_all_users()