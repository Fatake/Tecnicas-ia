from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("\t<-----   K-means Iris   ----->")

    # Carga el data set de iris
    iris_ds = datasets.load_iris()
    print("Iris Data Base:")

    x_iris = iris_ds.data
    y_iris = iris_ds.target

    # Creando Data Frame
    x = pd.DataFrame(iris_ds.data, columns=['Sepal Lenght','Sepal Width','Petal Lenght','Petal Width'])
    y = pd.DataFrame(iris_ds.target, columns=['Target'])

    print(x.head(10))

    # Seleccion de mejor modelo
    wcss = []
    for i in range(1, 11):
        print("\t<-----  Entrenamiento {0}  ----->".format(i))
        modelo = KMeans(n_clusters=i, max_iter=1000, random_state=0)
        modelo.fit(x)

        y_label = modelo.labels_
        y_kmeans = modelo.predict(x)

        print("Predicciones :\n",y_kmeans)

        # Valor de entrada y valor de prediccion
        accuracy = metrics.adjusted_rand_score(y_iris, y_kmeans)
        print("Procentaje de Precision : {0}%\n\n".format(accuracy*100))

        wcss.append(modelo.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.axhline(100,color='r',)
    plt.title('Metodo del Codo')
    plt.xlabel('#Clusters')
    plt.ylabel('WCSS')
    #plt.savefig('MetodoCodo.png')
    plt.show()


if __name__ == '__main__':
    main()
    