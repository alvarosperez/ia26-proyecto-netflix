from datetime import datetime


def registro_log(mensaje):
    ##mensaje con fecha y hora
    ahora = datetime.now()
    ## primero imprimo por consola el mensaje
    print(str(ahora) +  " - " +mensaje)
    
    ##mensaje se escriba en fichero de texto logs.txt
    with open("data/raw/logs.txt", "a") as fOut:
        fOut.write(str(ahora) +  " - " +mensaje + "\n")
        
        
