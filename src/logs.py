from datetime import datetime

def registro_log(mensaje):

    #fecha y hora actual
    ahora = datetime.now()
    #primero  imprimo por consola
    print (ahora, "-", mensaje)
    #y luego se escirbe en un fichero
    with open("data/logs.txt", "a") as fOut:
        fOut.write(str(ahora) + "-" + mensaje + "\n")