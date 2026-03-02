import os
import csv
import json

print("Ejecutando clean.py")

def json_to_csv(file_path):

    # 1️⃣ Cargar géneros y crear diccionario ID → nombre
    genre_dict = {}
    if os.path.exists("data/raw/movie_genres.json"):
        with open("data/raw/movie_genres.json", "r", encoding="utf-8") as f:
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
    print(f"Géneros cargados: {len(genre_dict)}")

    # 2️⃣ Lista donde guardaremos las películas limpias
    out = []

    # 3️⃣ Leer películas desde JSON
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and (line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            guardar = json.loads(line.strip())

            # 4️⃣ Convertir genre_ids a nombres
            genre_string = ", ".join(
                genre_dict[id] for id in guardar.get("genre_ids", []) if id in genre_dict
            )

            # 5️⃣ Crear diccionario limpio para cada película
            fila = {
                "id": guardar.get("id"),
                "title": guardar.get("title"),
                "genres": genre_string,
                "popularity": guardar.get("popularity"),
                "vote_average": guardar.get("vote_average")
            }

            out.append(fila)

    # 6️⃣ Escribir CSV
    os.makedirs("data/clean", exist_ok=True)
    fieldnames = ["id", "title", "genres", "popularity", "vote_average"]
    with open("data/clean/popular_movies.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)

    print(f"Se guardaron {len(out)} películas en data/clean/popular_movies.csv")


# Llamar a la función con tu archivo JSON solo cuando se ejecute directamente
def main():
    ruta = "data/raw/popular_movies.json"
    print(f"Procesando {ruta}")
    json_to_csv(ruta)

if __name__ == "__main__":
    main()