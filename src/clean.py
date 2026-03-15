import os
import csv
import json

def crear_diccionario_pelis(file_path):
    diccionario = {}
    with open(file_path, "r", encoding="utf-8") as fIn:
        for line in fIn:
            line = line.strip()
            if line.endswith(","):
                line = line[:-1]
            if line and line not in ["[", "]"]:
                datos = json.loads(line)
                diccionario[datos['id']] = datos['name']
    return diccionario

def json_to_csv_peliculas(file_path):
    out = []
    diccionario = crear_diccionario_pelis('data/raw/movie_genres.json')

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.endswith(","):
                line = line[:-1]
                
            if line and line not in ["[", "]"]:
                guardar = json.loads(line)
                
                genre_names = [] 
                for genre in guardar.get("genre_ids"):
                    genre_names.append(diccionario[genre]) 

                fila = {
                    "id": guardar.get("id"),
                    "title": guardar.get("title"), 
                    "genre_ids": genre_names,
                    "popularity": guardar.get("popularity"),
                    "vote_average": guardar.get("vote_average")
                }
                out.append(fila)
    fieldnames = ["id", "title", "genre_ids", "popularity", "vote_average"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)


def crear_diccionario_series(file_path):
    diccionario = {}
    with open(file_path, "r", encoding="utf-8") as fIn:
        for line in fIn:
            line = line.strip()
            if line.endswith(","):
                line = line[:-1]
            if line and line not in ["[", "]"]:
                datos = json.loads(line)
                diccionario[datos['id']] = datos['name']
    return diccionario

def json_to_csv_series(file_path):
    out = []
    diccionario = crear_diccionario_series('data/raw/series_genre.json')
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.endswith(","):
                line = line[:-1]
                
            if line and line not in ["[", "]"]:
                guardar = json.loads(line)
                genre_names = [] 
                for genre in guardar.get("genre_ids"):
                    nombre_genero = diccionario.get(genre, "Desconocido")
                    genre_names.append(nombre_genero) 

                fila = {
                    "id": guardar.get("id"),
                    "title": guardar.get("name"), 
                    "genre_ids": genre_names,
                    "popularity": guardar.get("popularity"),
                    "vote_average": guardar.get("vote_average")
                }
                out.append(fila)

    fieldnames = ["id", "title", "genre_ids", "popularity", "vote_average"]
    with open("data/clean/popular_series.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)
json_to_csv_peliculas("data/raw/popular_movies.json")
json_to_csv_series("data/raw/popular_series.json")