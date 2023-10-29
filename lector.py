import os
import tkinter as tk
from tkinter import filedialog

# Abre un cuadro de diálogo para que el usuario seleccione un directorio
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal de tkinter
ruta_directorio = filedialog.askdirectory(title="Selecciona un directorio")

if not ruta_directorio:
    print("No se seleccionó ningún directorio. Saliendo del programa.")
    exit()

# Lista todos los archivos en el directorio y subdirectorios
def listar_archivos(ruta):
    lista_archivos = []
    for foldername, subfolders, filenames in os.walk(ruta):
        for filename in filenames:
            lista_archivos.append(os.path.join(foldername, filename))
    return lista_archivos

# Lee el contenido de un archivo como una secuencia de bytes
def leer_contenido(archivo):
    with open(archivo, 'rb') as file:
        return file.read()

# Obtiene la lista de archivos y sus contenidos
archivos = listar_archivos(ruta_directorio)
datos_archivos = []

for archivo in archivos:
    nombre_archivo = os.path.basename(archivo)
    contenido_archivo = leer_contenido(archivo)
    # Decodifica los bytes utilizando 'latin-1' (puedes ajustar esto según el formato de codificación del archivo)
    contenido_decodificado = contenido_archivo.decode('latin-1', errors='replace')
    datos_archivos.append(f'NOMBRE_DEL_ARCHVIO: {nombre_archivo}\CONTENIDO_CODIGOS:\n{contenido_decodificado}\n{"="*50}')

# Obtiene la ruta completa del archivo de texto en el directorio seleccionado
ruta_archivo_txt = os.path.join(ruta_directorio, 'codigos.txt')

# Escribe los datos en el archivo de texto (modo de adición)
with open(ruta_archivo_txt, 'a', encoding='utf-8') as file:
    file.write('\n'.join(datos_archivos))

print(f'Archivos y contenidos agregados a {ruta_archivo_txt}')
