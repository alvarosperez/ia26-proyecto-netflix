# El proposito de este archivo es crear un sistema de registros con fecha de los datos obtenidos.
# importamos la librería de datetime para poder crear fechas
from datetime import datetime
# Creamos la función de registro y la importamos al documento de download 
def registros(mensaje):
    # Fecha y hora actual
    ahora = datetime.now()
    # Se imprime por consola, aunque realmente no es necesario tener este print
    print(ahora, "-", mensaje)
    # Y con esto se escribe en el archivo de logs.txt
    with open("data/log.txt", "a") as fOut: 
        fOut.write(str(ahora) + "-" + mensaje + "\n")

        
    