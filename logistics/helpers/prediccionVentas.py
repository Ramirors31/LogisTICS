import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
plt.style.use('ggplot')
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

current_dir = os.path.dirname(os.path.realpath(__file__)) 
filename = os.path.join(current_dir, "ventas_octubre.csv")
datos = pd.read_csv(filename, header=0)
#datos.drop(['Dia', 'Total Venta'], 1).hist()
dia = datos["Dia"].values
venta = datos["Total Venta"]


X_train = np.array(dia).reshape(-1,1)
y_train = venta

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_train)

plt.plot(X_train,y_pred)
 
# Veamos los coeficienetes obtenidos, En nuestro caso, serán la Tangente
"""print('Coefficients: \n', regr.coef_)
# Este es el valor donde corta el eje Y (en X=0)
print('Independent term: \n', regr.intercept_)
# Error Cuadrado Medio
print("Mean squared error: %.2f" % mean_squared_error(y_train, y_pred))
# Puntaje de Varianza. El mejor puntaje es un 1.0
print('Variance score: %.2f' % r2_score(y_train, y_pred))"""
y_Dosmil = regr.predict([[19]])
print(int(y_Dosmil))

plt.scatter(dia,venta)
plt.show()

