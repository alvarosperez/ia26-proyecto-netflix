import json
import csv
import os

# 1. Configuración de rutas
current_dir = os.path.dirname(__file__)      # Carpeta 'src'
project_root = os.path.dirname(current_dir)  # Raíz del proyecto

# Rutas de entrada y salida
ruta_json = os.path.join(project_root, 'data', 'raw', 'popular_movies.json')
carpeta_clean = os.path.join(project_root, 'data', 'clean')
ruta_csv = os.path.join(carpeta_clean, 'popular_movies.csv')

# 2. Crear la carpeta 'clean' si no existe
if not os.path.exists(carpeta_clean):
    os.makedirs(carpeta_clean)
    print(f"Carpeta creada: {carpeta_clean}")

# 3. Leer el JSON línea por línea
datos = []
try:
    with open(ruta_json, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                datos.append(json.loads(linea))
    
    # 4. Escribir el CSV en la carpeta 'clean'

        with open(ruta_csv, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=datos[0].keys())
            escritor.writeheader()
            escritor.writerows(datos)
except FileNotFoundError:
    print("No se encontro el archivo json")
        
