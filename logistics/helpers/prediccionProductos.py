from time import process_time_ns
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


class RegresionProductos:
    def __init__(self):
        current_dir = os.path.dirname(os.path.realpath(__file__)) 
        filename = os.path.join(current_dir, "VentasOctubreData.csv")
        datos = pd.read_csv(filename, header=0)
        #OBTENEMOS Y ORGANIZAMOS LAS LISTAS DE DATOS DE CADA PRODUCTO EN NUESTRO INVENTARIO
        criterio = datos["Producto"] == "Callo de acha"
        datosCallo = datos[criterio].values
        self.diaCallo = []
        self.ventaCallo = []
        for dato in datosCallo:
            self.diaCallo.append(dato[1])
            self.ventaCallo.append(dato[2])

        criterio = datos["Producto"] == "Camaron Coctelero"
        datosCamaronC = datos[criterio].values
        self.diaCamaronC = []
        self.ventaCamaronC = []
        for dato in datosCamaronC:
            self.diaCamaronC.append(dato[1])
            self.ventaCamaronC.append(dato[2])

        criterio = datos["Producto"] == "Camaron Gigante"
        datosCamaronG = datos[criterio].values
        self.diaCamaronG = []
        self.ventaCamaronG = []
        for dato in datosCamaronG:
            self.diaCamaronG.append(dato[1])
            self.ventaCamaronG.append(dato[2])

        
        criterio = datos["Producto"] == "Filete de Pescado"
        datosFilete = datos[criterio].values
        self.diaFilete = []
        self.ventaFilete = []
        for dato in datosFilete:
            self.diaFilete.append(dato[1])
            self.ventaFilete.append(dato[2])

        criterio = datos["Producto"] == "Medallon de Atun"
        datosAtun = datos[criterio].values
        self.diaAtun = []
        self.ventaAtun = []
        for dato in datosAtun:
            self.diaAtun.append(dato[1])
            self.ventaAtun.append(dato[2])

        criterio = datos["Producto"] == "Ostion"
        datosOstion = datos[criterio].values
        self.diaOstion = []
        self.ventaOstion = []
        for dato in datosOstion:
            self.diaOstion.append(dato[1])
            self.ventaOstion.append(dato[2])

        criterio = datos["Producto"] == "Pescado Entero"
        datosPescado = datos[criterio].values
        self.diaPescado = []
        self.ventaPescado = []
        for dato in datosPescado:
            self.diaPescado.append(dato[1])
            self.ventaPescado.append(dato[2])

        criterio = datos["Producto"] == "Pulpo"
        datosPulpo = datos[criterio].values
        self.diaPulpo = []
        self.ventaPulpo = []
        for dato in datosPulpo:
            self.diaPulpo.append(dato[1])
            self.ventaPulpo.append(dato[2])

    
        #print(self.aplicar_regresion(self.diaPescado,self.ventaPescado))

        
        
    def aplicar_regresion(self,dias,ventas):
        x_train = np.array(dias).reshape(-1,1)
        y_train = ventas
        self.regr = linear_model.LinearRegression()
        self.regr.fit(x_train,y_train)
        y_pred = self.regr.predict(x_train)
        #print("Valores Predecidos:", y_pred)
      
        #plt.scatter(dias,ventas)
        return (self.prediccion_semanal(22,29))
        #plt.show()

    def prediccion_semanal(self,diaInicio,diaFin):
        totalSemanal = 0
        ventasDiarias = []
        diaDelMes = []
        for i in range(diaInicio,diaFin):
            prediccion = self.prediccion_diaria(i)
            convertedArray = float(prediccion)
            ventasDiarias.append(round(convertedArray,2))
            diaDelMes.append(i)
            totalSemanal = totalSemanal + convertedArray
        plt.plot(diaDelMes,ventasDiarias)
        plt.scatter(diaDelMes,ventasDiarias)
        productoRequerido = "Unidades de producto estimadas a la semana: " + str(round(totalSemanal,2))
        plt.title("Estimacion Unidades De Producto Semanales")
        datos = [totalSemanal,diaDelMes,ventasDiarias]
        #print(datos)
        ejeyTitulo =  max(ventasDiarias)
        plt.text(9,ejeyTitulo,productoRequerido)
        #plt.show()
        return datos

       #FUNCION PARA PREDECIR LA UNIDAD DE PRODUCTO REQUERIDO PARA UN DETERMINADO DIA DEL MES
    def prediccion_diaria(self,dia):
        y_pred = self.regr.predict([[dia]])
        #print("Prediccion Diaria:", y_pred)
        #plt.plot(dia,y_pred)
        #plt.scatter(dia,y_pred)
        #plt.show()
        return y_pred






    """ #PREPARAMOS LOS DATOS PARA ENTRENAR NUESTRA RED NEURONAL
        self.x_train = np.array(self.dia).reshape(-1,1)
        self.y_train = self.venta
        
        #APLICAMOS LA REGRESION LINEAR A NUESTROS DATOS
        self.regr = linear_model.LinearRegression()
        self.regr.fit(self.x_train, self.y_train)
        
        #OBTENEMOS LOS VALORES DE PREDICCION DE NUESTRO SET DE DATOS
        self.y_pred = self.regr.predict(self.x_train)

    #FUNCION PARA GRAFICAR LOS RESULTADOS DE NUESTRA REGRESION
    def regresion_graficar(self):
        plt.plot(self.x_train,self.y_pred)
        plt.scatter(self.dia,self.venta)
        plt.show()
    
 

    def prediccion_semanal(self,diaInicio,diaFin):
        totalSemanal = 0
        ventasDiarias = []
        diaDelMes = []
        for i in range(diaInicio,diaFin):
            prediccion = self.prediccion_diaria(i)
            convertedArray = float(prediccion)
            ventasDiarias.append(round(convertedArray,2))
            diaDelMes.append(i)
            totalSemanal = totalSemanal + convertedArray
            
        datos = []
        datos.append(round(totalSemanal,2))
        datos.append(ventasDiarias)
        datos.append(diaDelMes)
        print(datos)
        return datos"""
            
ejemplo = RegresionProductos()



