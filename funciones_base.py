from pedir_datos_confirmaciones import validacion_usuario, ingreso_de_usuario




def rellenar_matriz_con_datos (nombres:str, alias:str, razas:str, generos:str, poderes:int, inteligencias:int, velocidades:int):

    matriz = [] #creo una matriz para concatenar los datos de las listas dadas

    for i in range(len(nombres)): #recorre toda la lista de nombres para poder acceder a los datos de cada posicion 
        fila = [nombres[i], alias[i], razas[i], generos[i], poderes[i], inteligencias[i], velocidades[i]] # define el indice que ocupara cada lista
        
        matriz.append(fila) #lleno la matriz con las filas con los datos cargados 
    
    return matriz


def agregar_personaje_matriz (matriz:list[list], nombres:str, alias:str, razas:str, generos:str, poderes:int, inteligencias:int, velocidades:int):

    confirmacion = False

    while confirmacion == False:

        nuevo_personaje = [nombres, alias, razas, generos, poderes, inteligencias, velocidades]

        matriz.append(nuevo_personaje)

        confirmacion = validacion_usuario("Quieres agregar un personaje mas?")
    
    return matriz

def mostrar_matriz_personajes (matriz):

    for fila in matriz:
        print(f"Nombre: {fila[0]} | Alias: {fila[1]} | Raza: {fila[2]} | Genero: {fila[3]} | Poder: {fila[4]} | inteligencia: {fila[5]} | velocidad: {fila[6]} ")


def existencias_de_raza (matriz:list[list], filtro:str):

    contador = 0
    for fila in matriz:
        if filtro in fila[2]:
            contador += 1

    return contador

def filtrar_raza (matriz:list[list], filtro:str):

    contador = 0
    for fila in matriz:
        if filtro != fila[2]:
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
