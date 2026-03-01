import csv
import json

peliculas = {}

with open("data/raw/popular_movies.json", "r", encoding="utf-8") as f:
    for line in f:
        peliculas.append(json.loads(line))
    
with open("data/clean/popular_movies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "title", "genres", "popularity", "callification"])
    for pelicula in peliculas:
        writer.writerow([
            pelicula.get("id"),
            pelicula.get("title"),
            "|".join(str(g) for g in pelicula.get("genre_ids", [])),
            pelicula.get("popularity"),
            pelicula.get("callification")
        ])
print("csv con peliculas limpio")

