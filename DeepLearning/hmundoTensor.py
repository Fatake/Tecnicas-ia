import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Crear modelo secuencial
model = keras.Sequential([keras.layers.Flatten(input_shape = (28, 28)), keras.layers.Dense(128, activation = tf.nn.relu), keras.layers.Dense(10, activation = tf.nn.softmax)])

# Compilación del modelo
model.compile(optimizer = tf.optimizers.Adam(), loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# Entrenamiento
model.fit(train_images, train_labels, epochs=5)

# Evaluación del modelo
test_loss, test_acc = model.evaluate( test_images, test_labels )

# Predicción del modelo:
model.predict(test_images)