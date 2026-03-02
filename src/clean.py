import os
import json
import csv

os.makedirs("data/clean", exist_ok=True)
def clean_movies(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        movies = json.load(f)

    cleaned_movies = []
    for movie in movies:
        cleaned_movie = {
            "id": movie.get("id"),
            "title": movie.get("title"),
            "release_date": movie.get("release_date"),
            "genre_ids": movie.get("genre_ids"),
            "vote_average": movie.get("vote_average"),
            "overview": movie.get("overview")
        }
        cleaned_movies.append(cleaned_movie)

    with open(output_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=cleaned_movies[0].keys())
        writer.writeheader()
        writer.writerows(cleaned_movies)


clean_movies("data/raw/popular_movies.json", "data/clean/popular_movies.csv")