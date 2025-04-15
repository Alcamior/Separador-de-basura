import numpy as np
from tensorflow.keras.utils import load_img,img_to_array
from keras.models import load_model
import os.path

#Leer la imagen a evaluar

imagen = "trash.jpg"

#Recortar la imagen

altura,anchura = 50,50
#Leer el modelo entrenado y sus pesos
modelo = "modelo/cnn1.h5"
pesos = "modelo/cnn1_pesos.weights.h5"

#Cargar el modelo entrenado
cnn = load_model(modelo)
cnn.load_weights(pesos)

#Transformar la imagen a clasificar
imagen_clasificar = load_img(imagen,target_size=(altura,anchura))
imagen_clasificar = img_to_array(imagen_clasificar)
imagen_clasificar = np.expand_dims(imagen_clasificar,axis =0)

#Evaluar la imagen
clase = cnn.predict(imagen_clasificar)
print(clase)
arg_max = np.argmax(clase)

if arg_max == 0:
  print("Aluminio")
elif(arg_max == 1):
  print("Basura")
elif(arg_max == 2):
  print("Orgánico")
elif(arg_max == 3):
  print("Papel/Cartón")
elif(arg_max == 4):
  print("Plástico")
elif(arg_max == 5):
  print("Vidrio")