# Ejemplo final combinado
from tkinter import *

ventana = Tk()

# Configuración de la cuadrícula
for i in range(3):
    ventana.grid_rowconfigure(i, weight=1)  # Filas expandibles
ventana.grid_columnconfigure(0, weight=1)  # Columna expandible

# Widgets
Label(ventana, text="Título", font=("Arial", 18)).grid(row=0, column=0, pady=10)
Entry(ventana).grid(row=1, column=0, padx=20, pady=5, sticky="ew")
Button(ventana, text="Aceptar").grid(row=2, column=0, pady=10)

ventana.mainloop()
