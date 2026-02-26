import os
import csv
import json
<<<<<<< HEAD
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
=======


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

>>>>>>> 59501f9a56ca4d781659845a7391354d4dcbafee
