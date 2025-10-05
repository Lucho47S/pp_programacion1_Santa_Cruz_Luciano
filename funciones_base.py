import validaciones as val


def rellenar_matriz_con_datos (nombres:list, alias:list, razas:list, generos:list, poderes:list, inteligencias:list, velocidades:list):

    matriz = [] #creo una matriz para concatenar los datos de las listas dadas

    for i in range(len(nombres)): #recorre toda la lista de nombres para poder acceder a los datos de cada posicion 
        fila = [nombres[i], alias[i], razas[i], generos[i], poderes[i], inteligencias[i], velocidades[i]] # define el indice que ocupara cada lista
        
        matriz.append(fila) #lleno la matriz con las filas con los datos cargados 
    
    return matriz

def agregar_personaje_input ():
    """Retorna todos los datos ingresados por el usuario para añadir un personaje

    Returns:
        
        nombres[str]: nombre del personaje

        alias[str]: apodo del personaje

        razas[str]: raza del personaje

        generos[str]: genero del personaje

        poderes[int]: nivel de poder del personaje

        inteligencias[int]: nivel de inteligencia del personaje
        
        velocidades[int]: nivel de velocidad del sujeto
    """
    nombres = input("Ingresa el nombre del sujeto: ")
    alias = input("Ingresa el alias del sujeto: ")
    razas = input("Ingresa las razas del sujeto: ")
    generos = input("Ingresa el genero del sujeto: ")
    poderes = val.validar_modo("Ingresa el nivel de poder del sujeto: ", "digit")
    inteligencias = val.validar_modo("Ingresa la inteligencia del sujeto: ", "digit")
    velocidades = val.validar_modo("Ingresa las velocidades del sujeto: ", "digit")

    return [nombres, alias, razas, generos, poderes, inteligencias, velocidades]

def agregar_personaje_matriz (matriz:list[list]):
    """Appendea un personaje a la matriz

    Args:
        matriz[list[list]]: matriz a appendear

    Returns:
        matriz[list[list]]: matriz modificada
    """
    confirmacion = True

    while confirmacion == True:

        nuevo_personaje = agregar_personaje_input()

        matriz.append(nuevo_personaje)

        confirmacion = val.validacion_input_booleano("Quieres agregar un personaje mas?")
    
    return matriz

def mostrar_matriz_personajes (matriz):

    for fila in matriz:
        print(f"Nombre: {fila[0]} | Alias: {fila[1]} | Raza: {fila[2]} | Genero: {fila[3]} | Poder: {fila[4]} | inteligencia: {fila[5]} | velocidad: {fila[6]} ")


def existencias_de_raza (matriz:list[list], filtro:str, excluir:bool):

    contador = 0
    for fila in matriz:
        if excluir == False:
            if filtro in fila[2]:
                contador += 1
        else:
            if filtro not in fila[2]:
                contador += 1

    return contador


def mostrar_raza_saiyan (matriz:list[list]):

    matriz_saiyan = []
    raza = "Saiyan"

    for fila in matriz:
        if fila[2] == raza:

            matriz_saiyan.append(fila)
    
    return matriz_saiyan

def mas_poderoso_una_pasada(matriz):
    matriz_poderosa = []
    mas_poderoso = None

    for fila in matriz:
        val = fila[4]
        if mas_poderoso is None or val > mas_poderoso:
            top_val = val
            top = [fila]
        elif val == top_val:
            top.append(fila)

    return top, len(top), top_val
