from datetime import datetime

<<<<<<< HEAD
def registro_logs(mensaje):
    #fecha y hora actual
    ahora= datetime.now()

    #primero imprimo por consola
    print(ahora, "  -  ", mensaje)
    
    #y luego se escribe en un fichero
    with open("data/logs.txt", "a") as fOut:      
        fOut.write(str(ahora) + "  -  " + mensaje + "\n")
=======

def registro_log(mensaje):
    ahora= datetime.now()
    print(ahora, " - ",mensaje)
    with open("data/logs.txt","a") as fOut:
        fOut.write(str(ahora)+ " - " + mensaje + "\n")
    
        
>>>>>>> main
