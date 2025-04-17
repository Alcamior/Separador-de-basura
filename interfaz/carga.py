import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import sys


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
ventana.geometry("900x400")
ventana.configure(bg="gray13")

titulo = tk.Label(ventana, text="Sube una imagen", font=("Instrument Sans", 28, "bold"), fg="honeydew2", bg="gray13")
titulo.pack(pady=20)

boton = tk.Button(ventana, text="Seleccionar imagen", bg="gray25", pady=8, padx=8, fg="honeydew2",
                  font=("Instrument Sans", 14), command=seleccionarImagen)
boton.pack()

ventana.mainloop()