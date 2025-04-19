from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Convolution2D, MaxPooling2D


#Ruta de las imágenes

entrenamiento = "../dataset/entrenar"
validacion = "../dataset/validar"

#Definir los hiperparámetros
epocas = 100
altura,anchura = 50,50
batch_size = 8
pasos = 80
#Definir la profundidad de la red neuronal convolucional
kernels1 = 32
kernels2 = 64
kernels3 = 128
kernel1_size = (3,3)
kernel2_size = (3,3)
kernel3_size = (3,3)
size_pooling = (2,2)
clases = 5

#Generar datos sintéticos para el entrenamiento

entrenar = ImageDataGenerator(rescale=1/255,
                              shear_range=0.20,
                              zoom_range=0.2,
                              horizontal_flip=True,
                              vertical_flip=True)
validar = ImageDataGenerator(rescale=1/255)

imagenes_entrenamiento = entrenar.flow_from_directory(entrenamiento,target_size=(altura,anchura),batch_size=batch_size,class_mode="categorical")
imagenes_validacion=validar.flow_from_directory(validacion,target_size=(altura,anchura),batch_size=batch_size,class_mode="categorical")

#Definir la arquitectura de la red neuronal convolucional
CNN=Sequential()

#Definir la primera capa convolucional
CNN.add(Convolution2D(kernels1,kernel1_size,padding="same",input_shape=(altura,anchura,3),activation="relu"))
CNN.add(MaxPooling2D(pool_size=size_pooling))

#Definir la segunda capa convolucional
CNN.add(Convolution2D(kernels2,kernel2_size,padding="same",activation="relu"))
CNN.add(MaxPooling2D(pool_size=size_pooling))

#Definir la tercera capa convolucional
CNN.add(Convolution2D(kernels3,kernel3_size,padding="same",activation="relu"))
CNN.add(MaxPooling2D(pool_size=size_pooling))

#Aplicar flatten
CNN.add(Flatten())

#Conectar con un perceptron multicapa (MLP)
#Primera capa oculta
CNN.add(Dense(128,activation="relu"))
#Segunda capa oculta
CNN.add(Dense(64,activation="relu"))
#Tercera capa oculta
CNN.add(Dense(32,activation="relu"))
#Apagar un % de neuronas
CNN.add(Dropout(0.55))
#Capa de salida
CNN.add(Dense(5,activation="softmax"))

#Establecer los parámetros iniciales del entrenamiento
CNN.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["acc","mse"])

#Entrenar la red neuronal convolucional
historico = CNN.fit(imagenes_entrenamiento,validation_data=imagenes_validacion,epochs=epocas,validation_steps=pasos,verbose=1)

#Guardar el modelo
CNN.save("../modelo/cnn1.h5")
CNN.save_weights("../modelo/cnn1_pesos.weights.h5")