import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # Graficador
import seaborn as sns # Permite Generar mejores visualizaciones
import re
from sklearn import tree
from sklearn.model_selection import train_test_split

def main():
    # Inicia Seaborn
    sns.set()
    print("\t<-----   Arboles de Desicion   ----->")

    # Cargando Data Set
    test_df =  pd.read_csv('titanic_test.csv')
    train_df = pd.read_csv('titanic_train.csv')

    print("Datos de entrenamiento:\n {0}\n Datos de Test:\n {1}".format(
        train_df.head(5),
        test_df.head(5)))
    

if __name__ == '__main__':
    main()
    