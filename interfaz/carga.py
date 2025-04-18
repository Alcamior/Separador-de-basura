import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import sys
from PIL import Image, ImageTk  # Importar PIL


def seleccionarImagen():
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
    )
    if ruta:
        try:
            # Obtener el directorio base del proyecto
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # 1. Guardar la ruta de la imagen
            temp_path = os.path.join(base_dir, "temp_image.txt")
            with open(temp_path, "w") as f:
                f.write(ruta)

            # 2. Ejecutar evaluacion.py (que está en la raíz)
            eval_path = os.path.join(base_dir, "evaluacion.py")
            subprocess.run([sys.executable, eval_path], check=True)

            # 3. Abrir resultado.py (que está en interfaz/)
            res_path = os.path.join(base_dir, "interfaz", "resultado.py")
            subprocess.Popen([sys.executable, res_path])

        except Exception as e:
            tk.messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")


# Resto del código de la interfaz
ventana = tk.Tk()
ventana.title("Subir imagen")
ventana.geometry("900x500")
ventana.configure(bg="#5F8575")


# Cargar imagen
ruta_imagen = "fondo.png"
imagen_original = Image.open(ruta_imagen)
imagen_redimensionada = imagen_original.resize((450, 200))
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Mostrar imagen en la ventana
label_imagen = tk.Label(ventana, image=imagen_tk, bg="#5F8575")
label_imagen.pack(pady=10)


# Título principal
titulo = tk.Label(ventana, text=" ♻️ Sistema separador de basura ♻️", 
                  font=("Instrument Sans", 28, "bold"), fg="white", bg="#5F8575")
titulo.pack(pady=30)

# Subtítulo para subir la imagen
titulo = tk.Label(ventana, text="Sube una imagen", 
                  font=("Instrument Sans", 26, "bold"), fg="honeydew2", bg="#5F8575")
titulo.pack(pady=20)

# Título del botón
boton = tk.Button(ventana, text="Seleccionar imagen", bg="dark green", pady=8, padx=8, fg="honeydew2",
                  font=("Instrument Sans", 14, "bold"), command=seleccionarImagen)
boton.pack()

ventana.mainloop()