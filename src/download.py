import os
import json
import requests
from logs import registro_log
from config import ACCESS_TOKEN
from clean import json_to_csv

def api_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

def data_writing(file_path, data,mode="w"):
    
    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, mode,  encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")

        #print(f"Se guardaron {len(data)} elementos en {file_path}")
        registro_log(f"Se guardaron {len(data)} elementos en {file_path}")

# movies
for page in range(1,7):
    movie_url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    movie_data = api_request(movie_url)
    movie_file_path = "data/raw/popular_movies.json"
    if page == 1:
         data_writing(movie_file_path, movie_data["results"],"w")
    else:
         data_writing(movie_file_path, movie_data["results"],"a")


# genres
genre_url = "https://api.themoviedb.org/3/genre/movie/list"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json" 
data_writing(genre_file_path, genre_data["genres"])

# series with pagination (same pages as movies for parity)
series_file_path = "data/raw/popular_series.json"
# clear or create file by writing first page, then append the rest
for page in range(1, 7):
    series_url = f"https://api.themoviedb.org/3/tv/popular?language=en-US&page={page}"
    series_data = api_request(series_url)
    if page == 1:
        data_writing(series_file_path, series_data.get("results", []), mode="w")
    else:
        data_writing(series_file_path, series_data.get("results", []), mode="a")

# géneros de series
series_genres_url = "https://api.themoviedb.org/3/genre/tv/list"
series_genres_data = api_request(series_genres_url)
genres_file_path = "data/raw/tv_genres.json"
data_writing(genres_file_path, series_genres_data.get("genres", []))




    
