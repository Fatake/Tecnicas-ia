# Modificar dataset agregando columan de país y hacer regresión múltiple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.model_selection import train_test_split #para dividir los datos
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

dataset = pd.read_csv('Salario_Experiencia.csv')

#Agregar columna países
paises = ['CO', 'MX', 'PE', 'BR', 'US'] 
dataset['Pais'] = [paises[np.random.randint(0,len(paises))] for i in range(len(dataset)) ]
dataset['IDPais'] = pd.factorize(dataset['Pais'])[0]
print('Dataset inicial\n\n', dataset.head())

#Asigno valores para x,y
x = dataset[['Aexperiencia','IDPais']]
y = dataset['Salario']
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size = 0.3, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)
ajuste = regressor.score(X_test,Y_test)
print('\nEl porcentaje de ajuste es: ', ajuste*100, '%\n')

#Grafico de los resultados de entrenamiento
fig = plt.figure(dpi=150)
viz_train = fig.add_subplot(111, projection='3d')
viz_train.scatter(X_train['Aexperiencia'], X_train['IDPais'], Y_train, color = 'blue', label = 'Train')
viz_train.scatter(X_test['Aexperiencia'], X_test['IDPais'], regressor.predict(X_test), color = 'red', label = 'Test')
viz_train.plot_trisurf(X_train['Aexperiencia'],X_train['IDPais'], regressor.predict(X_train),color = 'black', alpha = 0.5)
viz_train.set_title('Salario, Experiencia y País')
viz_train.set_xlabel('Experiencia (años)')
viz_train.set_ylabel('País')
viz_train.set_zlabel('Salario')
viz_train.set_yticks(range(len(paises)))
viz_train.set_yticklabels(paises)
plt.legend(loc="upper left") 
fig.savefig('Lineal_pais.png')

fig.show()
