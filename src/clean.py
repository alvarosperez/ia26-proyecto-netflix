import os
import csv
import json


def crear_diccionario_generos(file_path):
    diccionario = {}
    with open(file_path, "r", encoding="utf-8") as fIn:
        for line in fIn: 
            line = json.loads(line)
            diccionario[line['id']] = line['name']
    return diccionario


def json_to_csv(file_path):
    out = []
    diccionario = crear_diccionario_generos('data/raw/movie_genres.json') 

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            guardar = json.loads(line.strip())

            genre_names = []
            for genre in guardar.get("genre_ids", []):
                if genre in diccionario:
                    genre_names.append(diccionario[genre])

            fila = {
                "id": guardar.get("id"),
                "title": guardar.get("title"),
                "genre": genre_names("genre"),
                "popularity": guardar.get("popularity"),
                "vote_average": guardar.get("vote_average")
            }
            out.append(fila)

    fieldnames = ["id", "title", "genre", "popularity", "vote_average"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)
