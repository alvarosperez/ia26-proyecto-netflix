from datetime import datetime

def registro_logs(mensaje):
    ahora=datetime.now()
    #primero imprimo por consola
    print(ahora,"-", mensaje)
    #mensaje se escribe en un fichero
    with open ("data/logs.txt") as fOut:
        fOut.write(mensaje + "\n")
