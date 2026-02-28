import json
import csv
import os

with open("data/raw/popular_movies.json", "r", encoding="utf-8") as fichero_json:
    datos = json.load(fichero_json)

lista_peliculas = datos["results"]

os.makedirs("data/clean", exist_ok=True)

columnas = ["id", "título", "géneros", "popularidad", "nota"]

with open("data/clean/popular_movies.csv", "w", encoding="utf-8", newline="") as fichero_csv:
    escritor = csv.DictWriter(fichero_csv, fieldnames=columnas)
    
    escritor.writeheader()
    
    for peli in lista_peliculas:
        escritor.writerow({
            "id": peli["id"],
            "título": peli["title"],
            "géneros": peli["genre_ids"],
            "popularidad": peli["popularity"],
            "nota": peli["vote_average"]
        })

print("El archivo CSV ha sido creado correctamente.")