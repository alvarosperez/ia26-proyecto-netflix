def registro_log(mensaje):
    ##mensaje se escriba en fichero de texto logs.txt
    with open("logs.txt", "a") as fOut:
        fOut.write(mensaje + "\n")