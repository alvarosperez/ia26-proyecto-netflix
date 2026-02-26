import os
import csv
import json
def json_to_csv(file_path):
    out = []
    with open("data/raw/popular_movies.json", "r", encoding="utf-8") as f:
        encabezado = [{"ID"},{"Titulo"},{"Genero_ids"},{"Popularity"},{"Vote_averange"}]
        for line in f:
            if line.strip():
                datos = json.loads(line.strip())
                fila={
                    "id":datos.get("id"),
                    "title":datos.get("title"),
                    "genre_ids":datos.get("genre_ids"),
                    "popularity":datos.get("popularity"),
                    "vote_averange":datos.get("vote_averange")
                    }
                out.append(fila)
                
    fieldnames =["id","title","genre_ids","popularity","vote_averange"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames ,extrasaction="ignore")
        writer.writeheader(encabezado)
        writer.writerows(out)
json_to_csv("data/raw/popular_movies.json")