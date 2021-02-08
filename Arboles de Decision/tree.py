import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # Graficador
import seaborn as sns # Permite Generar mejores visualizaciones
import re
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

from io import StringIO 
from IPython.display import Image, display
import pydotplus

def main():
    print("\t<-----   Arboles de Desicion   ----->")
    # Inicia Seaborn
    sns.set()
    
    # Cargando Data Set
    test_df =  pd.read_csv('titanic_test.csv')
    train_df = pd.read_csv('titanic_train.csv')

    print("Datos de entrenamiento:\n {0}\n Datos de Test:\n {1}\n".format(
        train_df.head(5),
        test_df.head(5)))
    
    print(train_df.info())

    print("\n\n")
    ## Limpieza y poniendo datos a Cualitativos
    # Preprocesamiento
    label_encoder = preprocessing.LabelEncoder()
    encoder_sex = label_encoder.fit_transform(train_df['Sex'])

    # Cambia datos nulos, quitandolos, poniendo la media
    train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
    train_df['Embarked'] = train_df['Embarked'].fillna('S')

    # Predictores
    train_predictors = train_df.drop(['PassengerId','Survived', 'Name', 'Ticket', 'Cabin'], axis=1)

    # Datos Categoricos
    categorical_cols = [cname for cname in train_predictors.columns if 
                        train_predictors[cname].nunique() < 10 and
                        train_predictors[cname].dtype == 'object'
                    ]
    
    # Variables numericas
    numerical_cols = [cname for cname in train_predictors.columns if
                        train_predictors[cname].dtype in ['int64','float64']
                    ]
    
    #union
    cols = categorical_cols + numerical_cols
    train_predictors = train_predictors[cols]

    # Dummp de la informacion
    dummy_encoded_train_predictors = pd.get_dummies(train_predictors)
    print(train_df['Pclass'].value_counts())

    ## Despues de limpieza, ahora si entrenamiento
    y_target = train_df['Survived'].values
    x_features_one = dummy_encoded_train_predictors.values

    x_train, x_validation, y_train, y_validation = train_test_split(x_features_one, y_target, test_size=0.25, random_state=1)

    print("\nIniciando Entrenamiento con el arbol\n")
    tree1 = tree.DecisionTreeClassifier()
    tree1 = tree1.fit(x_features_one, y_target)

    tree1_accuracy = round(tree1.score(x_features_one, y_target),4)
    print("Escore: {0}%".format(tree1_accuracy*100))

    out = StringIO() # Crea una tuberia e salida

    # Exporta lo grafico Por medio de un archivo
    tree.export_graphviz(tree1, out_file=out)

    graph = pydotplus.graph_from_dot_data(out.getvalue())
    graph.write_png('titanic_tree.png')


if __name__ == '__main__':
    main()
    