import tkinter as tk
from tkinter import filedialog

# Función para tomar la ruta de la imagen
def seleccionarImagen():
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
    )
    if ruta:
        print("Imagen seleccionada:", ruta)

# Creación de interfaz
ventana = tk.Tk()
ventana.title("Subir imagen")
ventana.geometry("900x400")
ventana.configure(bg="gray13")

titulo = tk.Label(ventana, text="Sube una imagen", font=("Instrument Sans", 28, "bold"), fg="honeydew2", bg="gray13")
titulo.pack(pady=20)

boton = tk.Button(ventana, text="Seleccionar imagen", bg="gray25", pady=8, padx=8, fg="honeydew2",font=("Instrument Sans", 14), command=seleccionarImagen)
boton.pack()

ventana.mainloop()