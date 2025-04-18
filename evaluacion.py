import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import os

try:
    # Ubicarse en la raíz del proyecto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_temp = os.path.join(base_dir, "temp_image.txt")

    # Leer la imagen desde archivo temporal
    with open(ruta_temp, "r") as f:
        ruta_imagen = f.read().strip()

    # Preparar imagen
    img = load_img(ruta_imagen, target_size=(50, 50))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Cargar modelo
    modelo = load_model(os.path.join(base_dir, "modelo", "cnn1.h5"))
    modelo.load_weights(os.path.join(base_dir, "modelo", "cnn1_pesos.weights.h5"))

    # Predecir
    pred = modelo.predict(img_array)
    clase = np.argmax(pred)
    confianza = np.max(pred) * 100

    etiquetas = {
        0: "Aluminio/Metal",
        1: "Orgánico",
        2: "Papel/Cartón",
        3: "Plástico",
        4: "Vidrio"
    }

    resultado = etiquetas.get(clase, "Desconocido")

    # Guardar resultados en la raíz del proyecto
    ruta_resultado = os.path.join(base_dir, "resultado.txt")
    with open(ruta_resultado, "w") as f:
        f.write(f"Imagen: {os.path.basename(ruta_imagen)}\n")
        f.write(f"Clase: {resultado}\n")
        f.write(f"Confianza: {confianza:.2f}%\n")
        f.write(f"Ruta: {ruta_imagen}\n")

except Exception as e:
    # También guardar errores en la raíz
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_resultado = os.path.join(base_dir, "resultado.txt")
    with open(ruta_resultado, "w") as f:
        f.write("ERROR\n")
        f.write(str(e))