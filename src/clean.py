import os
import csv
import json

def crear_diccionario (file_path):
    diccionario ={}
    with open("data/raw/movie_genres.json", "r",encoding = "utf-8") as f2:
        for lin in f2:
            if lin.strip() and ( lin.strip() == "[" or lin.strip() == "]" or lin.strip() == ""):
                continue
            else:
                cambiar = json.loads(lin.strip())
               
                diccionario[cambiar.get("id")] = cambiar.get("name")
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        return diccionario


def json_to_csv(file_path):
    out = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and ( line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else :
                guardar = json.loads(line.strip())
                diccionario = crear_diccionario("data/raw/movie_genres.json")
                genres_name=[]
                for genre in guardar.get("genre_ids"):
                    genres_name.append(diccionario[genre])
                fila = {
                    "id": guardar.get("id"),
                    "title": guardar.get("title"),
<<<<<<< Updated upstream
                    "genre_ids": genres_name,
=======
                    "genre_ids": crear_diccionario("data/raw/movie_genres.json"),
>>>>>>> Stashed changes
                    "popularity": guardar.get("popularity"),
                    "vote_average": guardar.get("vote_average")
                }
                out.append(fila)

    fieldnames = ["id","title","genre_ids","popularity","vote_average"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)



json_to_csv("data/raw/popular_movies.json")