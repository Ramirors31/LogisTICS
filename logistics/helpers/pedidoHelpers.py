import pymysql
from conexion import DataBase

class PedidoHelper(DataBase):
    #CONSTRUCTOR, RECIBE PARAMETROS QUE SERÁN AÑADIDOS A LA TABLA
    motivo = ""
    cantidad = 0
    fecha = ""
    estado = ""
    fechaRecibido = ""
    distribuidor = ""
    formaPago = ""


    def __init__(self,motivo,cantidad,fecha,estado, fechaRecibido, distribuidor,formaPago):
        self.motivo = motivo
        self.cantidad = cantidad
        self.fecha = fecha
        self.estado = estado
        self.fechaRecibido = fechaRecibido
        self.distribuidor =  distribuidor
        self.formaPago = formaPago
    

        DataBase.__init__(self)
        

    #INSERTAR REPORTE DE PEDIDO NUEVO EN LA TABLA REPORTES
    def insertar(self):

        sql = "INSERT INTO reportes(motivo_reporte,cantidad_reporte,fecha_reporte) VALUES ('{}','{}','{}')".format(self.motivo,self.cantidad,self.fecha)
        try:
            self.cursor.execute(sql)
            print("Registro Añadido a la base de datos")
            self.connection.commit()
            #self.cursor.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))

    #FUNCION PARA GRAFICAR PEDIDOS
    def graficar_pedidos(self):
        sql = "SELECT cantidad_reporte, fecha_reporte FROM reportes WHERE motivo_reporte='PEDIDO'"
        try:
            self.cursor.execute(sql)
            self.data = self.cursor.fetchall()
            #print(self.data)
            pedidos = list(self.data)
            datosPedidos = []
            fechas = []
            montos = []
            n=0
            for pedido in pedidos:
                #FUNCION PARA CONVERTIR DATOS DE SQL A VALOR FLOTANTE PYTHON
                #venta = float('.'.join(str(ele) for ele in self.data[n]))
                pedido = list(pedidos[n])
                fecha = pedido[1]
                self.montosDiarios = []
                montoDiario = 0
                dia = fecha.split('-')
                montos.append(pedido[0])
                fechas.append(int(dia[0]))
                n = n+1
    
            

            for i in range(len(fechas)):
                #print(fechas[i])
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
            datosPedidos.append(fechas)
            datosPedidos.append(self.montosDiarios)
            self.connection.commit()
            self.connection.close()
            return datosPedidos
        except pymysql.Error as err:
            print('Algo salio mal',format(err))

    def pedidos_mensuales(self):
        pedidosMensual = 0
        for i in range(len(self.montosDiarios)):
            pedidosMensual = pedidosMensual + self.montosDiarios[i]
        return pedidosMensual

    #FUNCION PARA INSERTAR LOS DETALLES DE UN PEDIDO.

    def registrar_detalles(self,listaPedido,distribuidor):
        try:
            self.cursor.execute("SELECT * FROM reportes ORDER BY idreporte DESC")
            self.idPedido = self.cursor.fetchone()
            for producto in listaPedido:
                self.producto = producto[0]
                self.cantidadProducto = producto[2]
                self.subtotal = producto[3]
                sql = "INSERT INTO detalles_pedido(id_reporte,producto_pedido,cantidad_pedido,subtotal_pedido,distribuidor_pedido,fecha_pedido) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.idPedido[0],self.producto,self.cantidadProducto,self.subtotal,distribuidor,self.fecha)
                self.cursor.execute(sql)
            #INSERCION DEL PEDIDO EN LA TABLA PEDIDOS 
            sql = "INSERT INTO pedidos(id_reporte,fecha_pedido,estado_pedido,fecharecibido_pedido,distribuidor_pedido,monto_pedido,formapago_pedido) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(self.idPedido[0],self.fecha,self.estado,self.fechaRecibido,self.distribuidor,self.cantidad,self.formaPago)
            self.cursor.execute(sql)            
            self.connection.commit()
            self.connection.close()

        except pymysql.Error as err:
            print("Algo salio mal ", format(err))


    #FUNCION PARA MOSTRAR LA TABLA CON EL HISTORIAL DE PEDIDOS.

    def mostrar_tabla(self):
        sql = "SELECT * FROM pedidos"
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


    #FUNCION PARA BUSCAR UN PEDIDO EN LA BASE DE DATOS
    def buscar_registro(self, idreporte):
        sql = ("SELECT * FROM pedidos WHERE id_reporte='{}'").format(idreporte)
        try:
            self.cursor.execute(sql)
            self.busqueda =self.cursor.fetchone()
            self.connection.commit()
            self.connection.close()
            resultadoBusqueda = self.busqueda
            return resultadoBusqueda
        except pymysql.Error as err:
            print("Algo salio mal:", format(err))


    #FUNCION PARA ACTUALIZAR EL ESTADO DE UN PEDIDO 
    def actualizar_registro(self,idpedido,estadopedido):
        sql = "UPDATE pedidos SET estado_pedido = '{}' WHERE id_reporte = '{}'".format(estadopedido,idpedido)        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
            print("Modificacion Exitosa")
        except pymysql.Error as err:
            print("Algo salio mal ",format(err))



