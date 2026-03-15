import json
import csv
import os

def cargar_datos_json(ruta):
    lista_objetos = []
    with open(ruta, "r", encoding="utf-8-sig") as f:
        for linea in f:
            limpia = linea.strip().rstrip(",") 
            if limpia in ["[", "]", ""]: continue 
            try:
                lista_objetos.append(json.loads(limpia))
            except:
                continue
    return lista_objetos

def json_to_csv_final(input_path):
    # Cargar géneros
    generos_raw = cargar_datos_json("data/raw/series_genre.json")
    diccionario_generos = {item["id"]: item["name"] for item in generos_raw}
    
    # Cargar series
    series_raw = cargar_datos_json(input_path)
    
    out = []
    for serie in series_raw:
        g_ids = serie.get("genre_ids", [])
        nombres = [diccionario_generos.get(i, "N/A") for i in g_ids]
        
        out.append({
            "id": serie.get("id"),
            "name": serie.get("name"),
            "genre_ids": ", ".join(nombres),
            "popularity": serie.get("popularity"),
            "vote_average": serie.get("vote_average")
        })

    os.makedirs("data/clean", exist_ok=True)
    with open("data/clean/popular_series.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id","name","genre_ids","popularity","vote_average"])
        writer.writeheader()
        writer.writerows(out)

json_to_csv_final("data/raw/popular_series.json")