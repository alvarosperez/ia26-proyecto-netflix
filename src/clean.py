import json
import csv
from pathlib import Path


def limpiar_peliculas():
    input_path = Path("data/raw/popular_movies.json")
    output_path = Path("data/clean/popular_movies.csv")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    peliculas_totales = []

    # ✅ leer JSON lines (tu caso)
    with open(input_path, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            peli = json.loads(linea)
            peliculas_totales.append(peli)

    # ✅ escribir csv
    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "titulo", "generos", "popularidad", "nota"])

        for peli in peliculas_totales:
            writer.writerow([
                peli.get("id"),
                peli.get("title"),
                ",".join(map(str, peli.get("genre_ids", []))),
                peli.get("popularity"),
                peli.get("vote_average"),
            ])

    print(f"CSV generado con {len(peliculas_totales)} registros")


if __name__ == "__main__":
    limpiar_peliculas()