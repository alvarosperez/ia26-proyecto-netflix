from datetime import datetime
import os

def registro_log(mensaje):
    """Registra un mensaje con fecha y hora en consola y en archivo."""
    ahora = datetime.now()
    # Imprimir por consola
    print(str(ahora) + " - " + mensaje)
    
    # Escribir en fichero de texto logs.txt
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/logs.txt", "a") as fOut:
        fOut.write(str(ahora) + " - " + mensaje + "\n")
