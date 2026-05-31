import os
import csv
import json

def crear_diccionario_generos(file_path):
    diccionario = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = json.loads(line)
            diccionario[line['id']]=line['name']
    return diccionario

def json_to_csv(file_path, output_path, genres_path, name_key):
    out = []
    diccionario = crear_diccionario_generos(genres_path)

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and ( line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else :
                guardar = json.loads(line.strip())
                genre_names = []
                for genre in guardar.get("genre_ids", []):
                    genre_names.append(diccionario.get(genre, "Unknown"))

                fila = {
                    "id": guardar.get("id"),
                    "title": guardar.get("title"),
                    "genre_ids": genre_names,
                    "popularity": guardar.get("popularity"),
                    "vote_average": guardar.get("vote_average")
                }
                out.append(fila)

    fieldnames = ["id","title","genre_ids","popularity","vote_average"]

    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)


movie_input = "data/raw/popular_movies.json"
movie_output = "data/clean/popular_movies.csv"
movie_genres = "data/raw/movie_genres.json"
json_to_csv(movie_input, movie_output, movie_genres, "title")

# series
series_input = "data/raw/popular_series.json"
series_output = "data/clean/popular_series.csv"
series_genres = "data/raw/series_genre.json"
json_to_csv(series_input, series_output, series_genres, "name")
