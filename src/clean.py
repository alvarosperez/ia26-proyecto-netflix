import os
import csv
import json

def json_to_csv(file_path):
    out = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and ( line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else :
                guardar = json.loads(line.strip())

                #print(guardar.get("genre_ids"))
                #genre_ids = [28, 80]
                #genre_ids = ["Accion", "aventuras"]

                diccionario = crear_diccionario_generos('data/raw/movie_genres.json')
                genre_names = []
                for genre in guardar.get("genre_ids"):
                    genre_names.append(diccionario[genre])

                fila = {
                    "id": guardar.get("id"),
                    "title": guardar.get("title"),
                    "genre_ids": genre_names, # guardar.get("genre_ids"),
                    "popularity": guardar.get("popularity"),
                    "vote_average": guardar.get("vote_average")
                }
                out.append(fila)

    fieldnames = ["id","title","genre_ids","popularity","vote_average"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)

def crear_diccionario_generos(file_path):
    diccionario = {}
    
    with open(file_path, "r") as fIn:
        for line in fIn:
            line = json.loads(line)
            diccionario[line['id']] = line['name']

    return diccionario


json_to_csv("data/raw/popular_movies.json")
