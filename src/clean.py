#tarea: despues de crear archivo, crear csv ordenado 
import json
import csv

movies = []

with open("data/raw/popular_movies.json", "r", encoding="utf-8") as f:
    for line in f:
        movies.append(json.loads(line))

with open("data/clean/popular_movies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    
    writer.writerow(["id", "título", "géneros", "popularidad", "nota"])
    
    for movie in movies:
        writer.writerow([
            movie.get("id"),
            movie.get("titulo"),
            "|".join(str(g) for g in movie.get("genero_ids", [])),
            movie.get("popularidad"),
            movie.get("vote_average")
        ])

print("csv con peliculas")