import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

def main():
    print("\t <----   Regresion Logistica   ---->")

    print("Base de datos: diabetes.csv")
    diabetes = pd.read_csv('diabetes.csv')
    print("Tamaño (filas,Columnas) = {0}".format(diabetes.shape))
    print(diabetes.head(5))
    
    columnas_designadas = ['Pregnancies','Insulin', 'BMI', 'Age', 'Glucose', 'BloodPressure','DiabetesPedigreeFunction']

    x = diabetes[columnas_designadas]
    y = diabetes.Outcome # Atributo Clasificador

    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    # Entrenamiento
    logreg = LogisticRegression()
    logreg.fit(X_train, Y_train)

    # 0 Es no tiene diabetes, e 1 Si
    y_pred = logreg.predict(X_test)

    print(y_pred)

    # Matriz de confucion
    matriz_conf = metrics.confusion_matrix(Y_test, y_pred)
    print("Matriz de confucion: {0}".format(matriz_conf))

    class_name = [0,1]
    fig, ax = plt.subplots()
    tick_marks = np.arange(len(class_name))
    plt.xticks(tick_marks, class_name)
    plt.yticks(tick_marks, class_name)

    sns.heatmap(pd.DataFrame(matriz_conf), annot=True, cmap='Blues_r', fmt='g')
    ax.xaxis.set_label_position('top')
    plt.tight_layout()
    plt.title("Matriz de Confusion",y=1.1)
    plt.ylabel('Etiqueta Actual')
    plt.xlabel('Etiqueta Prediccion')

    plt.savefig('Matriz_confusion.png')

    print("Exactitud : {0}%".format(metrics.accuracy_score(Y_test, y_pred)*100))
    

if __name__ == '__main__':
    main()
    
