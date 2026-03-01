import csv
import json

peliculas_procesadas = []

with open("data/raw/popular_movies.json", "r", encoding="utf-8") as f:
    
    for fila in f:            
        fila = json.loads(fila)
        
        fila_out = [
            fila.get("id", ""), 
            fila.get("title", ""), 
            fila.get("genre", ""),       
            fila.get("popularity", ""), 
            fila.get("vote_average", "")
        ]
        
        peliculas_procesadas.append(fila_out)

with open("data/clean/popular_movies.csv", "w", encoding="utf-8", newline="") as f2:
    writer = csv.writer(f2, delimiter=',') 
    
    writer.writerow(["id", "titulo", "genero", "popularidad", "nota"])
    
    for n in peliculas_procesadas:
        writer.writerow(n)

print(f"Se han procesado {len(peliculas_procesadas)} películas y guardado correctamente.")
