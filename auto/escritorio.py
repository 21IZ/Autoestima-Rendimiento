import tkinter as tk
from tkinter import ttk
import subprocess
import os
import time
import threading

# Obtener el directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))

def ejecutar_autoestima_calificaciones():
    hilo = threading.Thread(target=ejecutar_script, args=(os.path.join(script_dir, "Autocalif"), "Ros.py", "Plots.png", 3))
    hilo.start()

def ejecutar_combinado():
    hilo = threading.Thread(target=ejecutar_script, args=(os.path.join(script_dir, "Combinado"), "Comb.py", "Plot_Combinado.png", 1))
    hilo.start()

def ejecutar_grado():
    hilo = threading.Thread(target=ejecutar_script, args=(os.path.join(script_dir, "Grado"), "Grado.py", "Grado.png", 1))
    hilo.start()

def ejecutar_script(directorio, script, imagen, tiempo_espera):
    os.chdir(directorio)
    print(f"Ejecutando {script}...")
    subprocess.run(["py", script])
    time.sleep(tiempo_espera)  # Espera el tiempo especificado para generar la imagen
    subprocess.Popen(["explorer", imagen])  # Abre la imagen en el explorador de Windows

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Autoestima / Rendimiento")
ventana.geometry("400x300")  # Establecer el tamaño de la ventana
ventana.resizable(True, True)  # Hacer que la ventana no sea redimensionable

# Estilo de los botones
estilo = ttk.Style()
estilo.theme_use("clam")  # Usar un tema de estilo diferente

# Crear los botones
boton_autoestima = ttk.Button(ventana, text="Autoestima y Calificaciones", command=ejecutar_autoestima_calificaciones, width=30)
boton_combinado = ttk.Button(ventana, text="Combinado", command=ejecutar_combinado, width=30)
boton_grado = ttk.Button(ventana, text="Grado", command=ejecutar_grado, width=30)

# Colocar los botones en la ventana
boton_autoestima.pack(pady=20)
boton_combinado.pack(pady=20)
boton_grado.pack(pady=20)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()