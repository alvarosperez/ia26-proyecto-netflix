from datetime import datetime
<<<<<<< HEAD
import os

def registro_log(mensaje):
    ##mensaje con fecha y hora
    ahora = datetime.now()
    ## primero imprimo por consola el mensaje
    print(str(ahora) +  " - " +mensaje)
    
    ## mensaje se escriba en fichero de texto logs.txt
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/logs.txt", "w") as fOut:
        fOut.write(str(ahora) +  " - " + mensaje + "\n")
=======


def registro_log(mensaje):
    ahora= datetime.now()
    print(ahora, " - ",mensaje)
    with open("data/logs.txt","a") as fOut:
        fOut.write(str(ahora)+ " - " + mensaje + "\n")
    
        
>>>>>>> main
