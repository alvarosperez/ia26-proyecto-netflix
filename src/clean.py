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
                fila = {
                    "id": guardar.get("id"),
                    "title": guardar.get("title"),
                    "genre_ids": guardar.get("genre_ids"),
                    "popularity": guardar.get("popularity"),
                    "vote_average": guardar.get("vote_average")
                }
                out.append(fila)

    fieldnames = ["id","title","genre_ids","popularity","vote_average"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)
json_to_csv("data/raw/popular_movies.json")
