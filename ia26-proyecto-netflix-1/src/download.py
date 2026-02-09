
import requests
 
from config import ACCESS_TOKEN
 
url = "https://api.themoviedb.org/3/authentication"
url_pelis = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1%22"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
 
response = requests.get(url, headers=headers)
 
print(response.text)