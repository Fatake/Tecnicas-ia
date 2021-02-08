import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

FILE_PATH = 'Salario_Experiencia.csv'

def main():
    print("\t<--   Ejemplo de Regresion lineal   -->\n")

    dataset = pd.read_csv(FILE_PATH)

    print("Leeyendo Data set: "+FILE_PATH)
    print(dataset.head(5))

    print("(filas,Columnas) = {0}".format(dataset.shape))

    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values

    # 70% de dato de entrenamiento 30 de test
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()

    # Entrenamiento
    regressor.fit(X_train,Y_train)

    # Graficacion De entrenamiento
    vista = plt
    vista.scatter(X_train, Y_train, color='blue')
    vista.plot(X_train, regressor.predict(X_train), color='black')

    vista.title('Salario vs Experiencia Entrenamiento')
    vista.xlabel('Experiencia')
    vista.ylabel('Salario')
    vista.savefig('Lineal_train.png')
    vista.show()
    
    # Graficacion De Prueba
    vista = plt
    vista.scatter(X_test, Y_test, color='red')
    vista.plot(X_train, regressor.predict(X_train), color='black')

    vista.title('Salario vs Experiencia Prueba')
    vista.xlabel('Experiencia')
    vista.ylabel('Salario')
    vista.savefig('Lineal_test.png')
    vista.show()
    
    print("Score: {0}%".format( regressor.score(X_test,Y_test)*100 ))

if __name__ == "__main__":
    main()