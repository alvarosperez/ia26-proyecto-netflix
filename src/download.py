import os

from config import ACCESS_TOKEN

url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

def api_request():
    headers = {    
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
     
    response = requests.get(url, headers=headers)
    return response.json()


def data_writing():
     
    os.makedirs("data/raw", exist_ok=True)
    
    with open(file_path, "w", encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")

    print(f"Se guardaron {len(movies)} elementos en {file_path}")


#movies
movie_url= "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
movie_data = api_request(movie_url)
movie_file_path = "data/raw/popular_movies.json"
data_writing(movie_file_path, movie_data["results"])

#genres
gene_url = "https://api.theoviedb.org/3/genre/movie/list"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json"
data_writing(genre_file_path, genre_data["genres"] )


