import os
import csv
import json


os.makedirs("data/clean", exist_ok=True)

csv_file_path = "data/clean/popular_movies.csv"

with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "titulo", "generos", "popularidad", "nota"])
    
    with open("data/raw/popular_movies.json", "r", encoding="utf-8") as f:
        movies = [json.loads(line) for line in f]
    
    with open("data/raw/movie_genres.json", "r", encoding="utf-8") as f:
        genre_list = [json.loads(line) for line in f]
    
    genre_dict = {g["id"]: g["name"] for g in genre_list}
    
    for movie in movies:
        movie_id = movie.get("id", "")
        title = movie.get("title", "")
        genre_ids = movie.get("genre_ids", [])
        genres = [genre_dict.get(gid, "") for gid in genre_ids]
        genres_text = ", ".join(genres)
        popularity = movie.get("popularity", "")
        vote_average = movie.get("vote_average", "")
        writer.writerow([movie_id, title, genres_text, popularity, vote_average])

