#Registra los cambios en el código 
from datetime import datetime

def registro_log(mensaje):
    #fecha y hora actual 
    ahora = datetime.now()

    #primero lo escribo por consola y luego se escribe en el fichero
    print(ahora, "-", mensaje)
    #mensaje se escriba en un fichero 
    with open("data/logs.txt", "a") as fOut:
        fOut.write(str(ahora) + "-" + mensaje + "\n")
