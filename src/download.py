import requests
import json 
import os 
from config import ACCESS_TOKEN

url_prueba = "https://api.themoviedb.org/3/authentication"
url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}



def peliculas_populares():
    response = requests.get(url_popular_movies, headers=headers) # Esta variable toma todos los datos de la url indicada, incluyendo los códigos de errores
    informacion = response.json() # La variable informacion toma esos datos y excluye cosas como los códigos de errores para transformarlo en un diccionario 
    lista_peliculas = informacion.get("results", []) # La variable de lista_peliculas busca en ese diccionario el apartado de "results", que es donde se guarda la información de las peliculas
    ruta_archivo = os.path.join("src","..","data", "raw","peliculas populares.txt") # La nueva ruta donde se generará el archivo .txt 
    with open(ruta_archivo,"w", encoding="utf-8") as archivo:
        for peliculas in lista_peliculas: # El programa ya sabe por sí solo cuándo la información de una película termina y comienza la de otra, es por eso que mi bucle for con el "}" fallava anteriormente
            texto = json.dumps(peliculas, ensure_ascii=False) # lista_peliculas es una y archivo.write() no acepta listas, sino texto (A/K/A strings), la variable texto convierte esa lista en un string 
            archivo.write(texto + "\n") # Ecribir la información de cada película y CUANDO ESA INFORMACIÓN ACABE, dejar una línea en blanco 
peliculas_populares() # Hago que el programa ejecute la función peliculas_populares para poder ejecutar el programa

# Notas: inicialmente apenas usaba la librería json, únicamente la veces que las ha usado el profesor (request.get, response.json, informacion.get) puesto que esa librería no la hemos usado jamas.
# la cosa es que intentar convertir la variable lista_peliculas en un str del método tradicional [archivo.write(str(lista_peliculas))]te impide usar el ensure_ascii = False. Esto provoca que
# los carácteres que el ordenador desconozca (ñ,´, º, etc) se transformen en lenguaje ascii. 

# Nota: json es, en pocas palabras, una librería que mejora la representación de la información, así como traducir un lenguaje de programación 
# es por eso que puedo utilizar dicha librería para descartar cosas como los códigos de estado que aparecen si no uso response.json().
# Cabría destacar que response.json() lo usó el profesor pero no estoy muy seguro si esa es la función que cumple 