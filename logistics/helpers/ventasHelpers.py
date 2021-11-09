import pymysql
from pymysql.err import raise_mysql_exception
from conexion import DataBase

class VentasHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
    motivo = ""
    cantidad = 0
    fecha = ""

    def __init__(self,motivo,cantidad,fecha):
        self.motivo = motivo
        self.cantidad = cantidad
        self.fecha = fecha
    

        DataBase.__init__(self)
        

    #GUARDAR REPORTE DE VENTA NUEVO EN LA BASE DE DATOS
    def insertar(self):

        sql = "INSERT INTO reportes(motivo_reporte,cantidad_reporte,fecha_reporte) VALUES ('{}','{}','{}')".format(self.motivo,self.cantidad,self.fecha)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.connection.commit()
            
            #print(self.idVenta[0])
            #self.cursor.close()


        except pymysql.Error as err:
            print("Algo salio mal ", format(err))

    def registrar_detalles(self,listaVenta):
        try:
            self.cursor.execute("SELECT * FROM reportes ORDER BY idreporte DESC")
            self.idVenta = self.cursor.fetchone()
            print(listaVenta)
            for producto in listaVenta:
                self.producto = producto[0]
                self.cantidadProducto = producto[2]
                self.subtotal = producto[3]
                sql = "INSERT INTO detalles_venta(id_venta,producto_venta,cantidad_venta,subtotal_venta,fecha_venta) VALUES ('{}','{}','{}','{}','{}')".format(self.idVenta[0],self.producto,self.cantidadProducto,self.subtotal,self.fecha)
                self.cursor.execute(sql)
                print("Insertados en detalle ventas")

            self.connection.commit()
            self.connection.close()

        
        except pymysql.Error as err:
            print("Algo salio mal ", format(err))


        
        #self.cursor.execute()
        

    def mostrar_tabla(self):
        sql = "SELECT * FROM reportes"
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
        
    #FUNCION PARA GRAFICAR VENTAS
    def graficar_ventas(self):
        sql = "SELECT cantidad_reporte, fecha_reporte FROM reportes WHERE motivo_reporte='VENTA'"
        try:
            self.cursor.execute(sql)
            self.data = self.cursor.fetchall()
            #print(self.data)
            ventas = list(self.data)
            datosVentas = []
            fechas = []
            montos = []
            n=0
            for venta in ventas:
                #FUNCION PARA CONVERTIR DATOS DE SQL A VALOR FLOTANTE PYTHON
                #venta = float('.'.join(str(ele) for ele in self.data[n]))
                venta = list(ventas[n])
                fecha = venta[1]
                self.montosDiarios = []
                montoDiario = 0
                dia = fecha.split('-')
                montos.append(venta[0])
                fechas.append(int(dia[0]))
                n = n+1

            for i in range(len(fechas)):
              
                if(i < len(fechas)-1):

                    if (fechas[i] == fechas[i+1]):
                        montoDiario = montoDiario + montos[i] + montos[i+1]
                        self.montosDiarios.append(0)
                    else:
                        montoDiario = montoDiario + montos[i]
                        self.montosDiarios.append(montoDiario)

                else:
                    montoDiario = montoDiario + montos[i]
                    self.montosDiarios.append(montoDiario)

            datosVentas.append(fechas)
            datosVentas.append(self.montosDiarios)
            self.connection.commit()
            self.connection.close()
            return datosVentas
        except pymysql.Error as err:
            print('Algo salio mal',format(err))

    def ventas_mensuales(self):
        ventaMensual = 0
        for i in range(len(self.montosDiarios)):
            ventaMensual = ventaMensual + self.montosDiarios[i]

        return ventaMensual

