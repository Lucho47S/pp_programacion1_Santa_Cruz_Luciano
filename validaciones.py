def validacion_input_booleano(texto:str):
    """
    Hace una pregunta al usuario que puede responderse con si o no y valida recursivamente
    
    Args:

        texto[str]: pregunta a imprimir

    Returns:

        dato[str]: respuesta del usuario
    """
    dato = None
    print(texto)
    confirmacion = str(validar_modo("s/n: ", "alpha")).lower()

    if confirmacion == "s":
        dato = True
    elif confirmacion == "n":
        dato = False
    
    else:
        print("Opcion Invalida")
        return validacion_input_booleano(texto)
    
    return dato

def validacion_existe_matriz(matriz: list[list]):
    if matriz:
        return True
    else:
        print("La matriz aun no fue creada, inicialize la matriz primero")
        return False
    
def validar_modo(mensaje: str, modo: str) -> str:
    """Pide al usuario un valor y valida recursivamente que respete su modo

    Args:

        mensaje[str]: texto a imprimir

        modo[str]: tipo de validación ('digit', 'alpha', 'alnum')

    Returns:

        Entrada: input del usuario ya validado
    """
    entrada = input(mensaje)
    error = None

    match modo:
        case "digit":
            if not entrada.isdigit():
                error = "Debe ser un numero válido"
        case "alpha":
            if not entrada.isalpha():
                error = "Debe contener solo letras"
        case "alnum":
            if not entrada.isalnum():
                error = "Debe contener solo letras o numeros"
        case _:
            error = "Modo invalido, usa: digit, alpha o alnum"

    if error:
        print(error)
        return validar_modo(mensaje, modo)

    return entrada