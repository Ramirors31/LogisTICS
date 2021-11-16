import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

class RegresionVentas:
    def __init__(self):
        current_dir = os.path.dirname(os.path.realpath(__file__)) 
        filename = os.path.join(current_dir, "ventas_octubre.csv")
        datos = pd.read_csv(filename, header=0)
        #GUARDAMOS EN LISTAS LOS DATOS DE NUESTRO CSV
        self.dia = datos["Dia"].values
        self.venta = datos["Total Venta"]

        #PREPARAMOS LOS DATOS PARA ENTRENAR NUESTRA RED NEURONAL
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
    
    #FUNCION PARA PREDECIR LAS VENTAS UN DETERMINADO DIA DEL MES
    def prediccion_diaria(self, dia):
        ventasDelDia = self.regr.predict([[dia]])
        return ventasDelDia

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
        plt.plot(diaDelMes,ventasDiarias)
        #plt.show()
        print(datos)
        return datos
            
            

ejemplo = RegresionVentas()
ejemplo.prediccion_semanal(9,16)


 
        # Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
"""print('Coefficients: \n', regr.coef_)
# Este es el valor donde corta el eje Y (en X=0)
print('Independent term: \n', regr.intercept_)
# Error Cuadrado Medio
print("Mean squared error: %.2f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Variance score: %.2f' % r2_score(y_train, y_pred))"""


        

