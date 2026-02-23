import csv
import json
with open( "data/raw/popular_movies.json", "r", encoding="utf-8") as f:
    for fila in f:
        print(fila)
        fila = json.loads(fila)
        fila_out = [fila["id"], fila["title"], fila["genre"], fila[""]]
        print(fila_out)
        break

