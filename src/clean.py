import os
import csv
import json

print("Ejecutando clean.py")

def json_to_csv(file_path, genre_path, output_csv):
    """Convert a raw JSON file of titles into a cleaned CSV.

    Parameters
    ----------
    file_path : str
        Path to the JSON file containing either movies or series.
    genre_path : str
        Path to the JSON file that maps genre IDs to names (movie or tv).
    output_csv : str
        Destination CSV file to write the cleaned data.
    """

    # 1️⃣ Cargar géneros y crear diccionario ID → nombre
    genre_dict = {}
    if os.path.exists(genre_path):
        with open(genre_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    genre = json.loads(line)
                except json.JSONDecodeError:
                    # ignorar líneas no válidas
                    continue
                if isinstance(genre, dict) and "id" in genre and "name" in genre:
                    genre_dict[genre["id"]] = genre["name"]
    # imprimir para debug
    print(f"Géneros cargados desde {genre_path}: {len(genre_dict)}")

    # 2️⃣ Lista donde guardaremos los títulos limpios
    out = []

    # 3️⃣ Leer objetos desde JSON de entrada
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and (line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            guardar = json.loads(line.strip())

            # 4️⃣ Convertir genre_ids a nombres
            genre_string = ", ".join(
                genre_dict.get(id, "") for id in guardar.get("genre_ids", [])
                if id in genre_dict
            )

            # 5️⃣ Crear diccionario limpio para cada entrada
            fila = {
                "id": guardar.get("id"),
                "title": guardar.get("title"),
                "genres": genre_string,
                "popularity": guardar.get("popularity"),
                "vote_average": guardar.get("vote_average")
            }

            out.append(fila)

    # 6️⃣ Escribir CSV de salida
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    fieldnames = ["id", "title", "genres", "popularity", "vote_average"]
    with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)

    print(f"Se guardaron {len(out)} registros en {output_csv}")

# Llamar a la función con el/los archivos JSON cuando se ejecute directamente
def main():
    # Películas
    movies_json = "data/raw/popular_movies.json"
    movies_genres = "data/raw/movie_genres.json"
    movies_out = "data/clean/popular_movies.csv"
    print(f"Procesando películas desde {movies_json}")
    json_to_csv(movies_json, movies_genres, movies_out)

    # Series
    series_json = "data/raw/popular_series.json"
    series_genres = "data/raw/tv_genres.json"
    series_out = "data/clean/popular_series.csv"
    print(f"Procesando series desde {series_json}")
    json_to_csv(series_json, series_genres, series_out)

if __name__ == "__main__":
    main()