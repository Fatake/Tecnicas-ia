import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("\t<-----  Trabajando con Deep Learning  ----->")
    
    # Cargando dataset Fashion
    data_set = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = data_set.load_data()

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 
                    'Dress', 'Coat', 'Sandal', 'Shirt', 
                    'Sneaker', 'Bag', 'Ankle boot']

    print("Tamaño de la BD: ",train_images.shape)

    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid('off')
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    
    # Crea las capas, en este caso 3
    model = keras.Sequential([keras.layers.Flatten(input_shape = (28, 28)), 
                            keras.layers.Dense(128, activation = tf.nn.relu), 
                            keras.layers.Dense(10, activation = tf.nn.softmax)])
    
    # Compilar 
    model.compile(optimizer = tf.optimizers.Adam(), 
                loss = 'sparse_categorical_crossentropy', 
                metrics = ['accuracy'])

    # Entrenamiento
    model.fit(train_images, train_labels, epochs = 5)

    # Evaluacion
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Porcentaje del Modelo {0}%'.format(test_acc*100))

    predictions = model.predict(test_images)

    plt.figure(figsize = (10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid('off')
        plt.imshow(test_images[i], cmap = plt.cm.binary)
        predicted_label = np.argmax(predictions[i])
        true_label = test_labels[i]
        if predicted_label == true_label:
            color = 'blue'
        else: 
            color = 'red'
            
        plt.xlabel('{} ({})'.format(class_names[predicted_label], class_names[true_label]), color = color)

    plt.show()

if __name__ == '__main__':
    main()
