def validacion_usuario (texto:str):
    
    dato = None
    confirmacion = input(str(texto("s/n")))

    if confirmacion == "n":
        dato == True
    else:
        dato == False

    return dato


def ingreso_de_usuario (texto:str):

    obtener_algo = input(texto)

    return obtener_algo