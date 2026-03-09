from datetime import datetime


def registro_log(mensaje):
    ahora= datetime.now()
    print(ahora, " - ",mensaje)
    with open("data/logs.txt","a") as fOut:
        fOut.write(str(ahora)+ " - " + mensaje + "\n")
        
