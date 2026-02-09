
import requests

from config import ACCESS_TOKEN

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN} "
}

print(headers)

response = requests.get(url, headers=headers)

print(response.text)