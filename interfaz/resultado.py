import tkinter as tk
from PIL import Image, ImageTk
import os

def mostrar_resultado():
    try:
        ruta = os.path.join(os.path.dirname(__file__), "..", "resultado.txt")
        with open(ruta, "r") as f:
            lineas = f.readlines()

        if lineas[0].startswith("ERROR"):
            lbl_error.config(text="Error al procesar la imagen:\n" + "".join(lineas[1:]))
            return

        datos = {}
        for linea in lineas:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = valor.strip()

        lbl_imagen.config(text="Imagen: " + datos["Imagen"])
        lbl_clase.config(text="Clase: " + datos["Clase"])
        lbl_confianza.config(text="Confianza: " + datos["Confianza"])

        imagen = Image.open(datos["Ruta"])
        imagen.thumbnail((300, 300))
        imagen_tk = ImageTk.PhotoImage(imagen)
        panel_imagen.config(image=imagen_tk)
        panel_imagen.image = imagen_tk

    except Exception as e:
        lbl_error.config(text="Error al cargar resultados\n" + str(e))

ventana = tk.Tk()
ventana.title("Resultado")
ventana.geometry("500x600")
ventana.configure(bg="gray13")

panel_imagen = tk.Label(ventana, bg="gray13")
panel_imagen.pack(pady=10)

lbl_imagen = tk.Label(ventana, text="Imagen:", fg="white", bg="gray13")
lbl_imagen.pack()

lbl_clase = tk.Label(ventana, text="Clase:", fg="white", bg="gray13")
lbl_clase.pack()

lbl_confianza = tk.Label(ventana, text="Confianza:", fg="white", bg="gray13")
lbl_confianza.pack()

lbl_error = tk.Label(ventana, text="", fg="red", bg="gray13")
lbl_error.pack()

tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)

ventana.after(100, mostrar_resultado)
ventana.mainloop()