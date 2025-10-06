import validaciones as val


def rellenar_matriz_con_datos (nombres:list, alias:list, razas:list, generos:list, poderes:list, inteligencias:list, velocidades:list) -> list[list]:
    """Crea una matriz con las listas dadas

    Args:
        nombres (list): lista de nombres de los personajes
        alias (list): lista de alias de los personajes
        razas (list): lista de razas de los personajes
        generos (list): lista de generos de los personajes
        poderes (list): niveles de poder de los personajes
        inteligencias (list): iq de los personajes
        velocidades (list): nivel de velocidad de los personajes

    Returns:
    
        list[list]: matriz nueva con todas las listas dadas
    """
    matriz = []

    for i in range(len(nombres)):
        fila = [nombres[i], alias[i], razas[i], generos[i], poderes[i], inteligencias[i], velocidades[i]]
        
        matriz.append(fila)
    
    return matriz

def agregar_personaje_input() ->list:
    """Retorna todos los datos ingresados por el usuario para añadir un personaje

    Returns:
        list: lista con todos los valores del personaje ingresado
    """
    entrada = []

    nombres = val.validar_modo("Ingresa el nombre del sujeto: ", "alnum")
    alias = str(input("Ingresa el alias del sujeto: "))
    razas = str(input("Ingresa las razas del sujeto: "))
    generos = str(input("Ingresa el genero del sujeto: "))
    poderes = int(val.validar_modo("Ingresa el nivel de poder del sujeto: ", "digit"))
    inteligencias = int(val.validar_modo("Ingresa la inteligencia del sujeto: ", "digit"))
    velocidades = int(val.validar_modo("Ingresa las velocidades del sujeto: ", "digit"))
    
    entrada = [nombres, alias, razas, generos, poderes, inteligencias, velocidades]
    return entrada

def agregar_personaje_matriz(matriz:list[list]) -> list[list]:
    """Añade un personaje elejido por el usuario a la matriz

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

def mostrar_matriz_personajes(matriz:list[list]):
    """Impreme todas los datos de cada personaje dentro de la matriz asignada

    Args:
        list[list]: matriz cuyas filas se imprimiran
    """
    for fila in matriz:
        print(f"Nombre: {fila[0]} | Alias: {fila[1]} | Raza: {fila[2]} | Genero: {fila[3]} | Poder: {fila[4]} | inteligencia: {fila[5]} | velocidad: {fila[6]} ")


def existencias_de_tag(matriz:list[list], indice_fila : int, tag:str, excluir:bool = False) -> int:
    """Recorre la matriz y contea cada elemento con la etiqueta asignada o la falta de esta

    Args:
        matriz (list[list]): matriz a recorrer
        indice_fila (int): indice de la matriz a recorrer
        tag (str): etiqueta a buscar en la lista
        excluir (bool, optional): decide si buscamos elementos con la tag, o elementos sin la misma. False por defecto

    Returns:
        int: numero de elementos que poseen(o no) la etiqueta
    """
    contador = 0
    for fila in matriz:
        if excluir == False:
            if tag in fila[indice_fila]:
                contador += 1
        else:
            if tag not in fila[indice_fila]:
                contador += 1

    return int(contador)


def filtrar_tag(matriz:list[list], indice_fila: int, tag: str, excluir: bool = False) -> list[list]:
    """Filtra una matriz buscando los elementos que poseen una cierta etiqueta

    Args:
        matriz (list[list]): Matriz a filtrar
        indice_fila (int): Indice de la matriz a filtrar
        tag (str): etiqueta a buscar en la lista
        excluir (bool, optional): decide si debe buscar la tag o buscar elementos sin ella. False por defecto

    Returns:
        list[list]: matriz con los elementos que tienen(o no) la etiqueta
    """
    matriz_filtrada = []

    for fila in matriz:
        if excluir == False:
            if fila[indice_fila] == tag:
                matriz_filtrada.append(fila)
        else:
            if fila[indice_fila] != tag:
                matriz_filtrada.append(fila)
    
    return matriz_filtrada

def recorrido_de_matriz(matriz: list[list]) -> list[list]:
    """ Recorre cada fila de la matriz truncando los datos

    args:
        matriz: list[list] (la matriz a truncar)
    
    returns:
        matriz_detallada (la matriz con los elementos ya truncados)
    """
    matriz_detallada = []

    for fila in matriz:
        fila_limitada = truncando(fila)
        matriz_detallada.append(fila_limitada)

    return matriz_detallada


def truncando(fila) -> list:
    """ Trunca los elementos en cada posicion 

    Args: 
        fila (donde se quedo la anterior iteracion)
    
    Returs:
        nueva_fila (los elementos de cada fila truncados)
    """
    nueva_fila = []

    for elemento in fila:
        texto = str(elemento)[0:15]
        nueva_fila.append(texto)
    
    return nueva_fila

def buscar_valor_extremo(matriz: list[list], indice: int, modo: str) -> float:
    """
    Devuelve el valor máximo o mínimo de una columna según el modo elegido.

    Args:
        matriz (list[list]): matriz a recorrer
        indice (int): índice del campo numérico a comparar
        modo (str): 'max' para máximo o 'min' para mínimo

    Returns:
        int: valor máximo o mínimo encontrado
    """
    valor_extremo = matriz[0][indice]

    for fila in matriz:
        if modo == "max" and fila[indice] > valor_extremo:
            valor_extremo = fila[indice]
        elif modo == "min" and fila[indice] < valor_extremo:
            valor_extremo = fila[indice]

    return int(valor_extremo)


def filtrar_por_valor(matriz: list[list], indice: int, comparador: str, valor: float) -> list[list]:
    """
    Filtra la matriz según una comparación numérica.

    Args:
        matriz (list[list]): matriz base
        indice (int): índice de la columna a comparar
        comparador (str): puede ser '==', '>', '<', '>=', '<='
        valor (float): valor contra el que se compara

    Returns:
        list[list]: nueva matriz con las filas que cumplen la condición
    """
    matriz_filtrada = []

    for fila in matriz:
        num = fila[indice]

        match comparador:
            case "==":
                if num == valor:
                    matriz_filtrada.append(fila)
            case ">":
                if num > valor:
                    matriz_filtrada.append(fila)
            case "<":
                if num < valor:
                    matriz_filtrada.append(fila)
            case ">=":
                if num >= valor:
                    matriz_filtrada.append(fila)
            case "<=":
                if num <= valor:
                    matriz_filtrada.append(fila)

    return matriz_filtrada

def calcular_promedio(matriz: list[list], indice: int) -> float:
    """Calcula el promedio de una columna numérica.

    Args:
        matriz (list[list]): matriz a recorrer
        indice (int): indice de la matriz a recorrer

    Returns:
        float: promedio del indice dado
    """
    total = 0
    contador = 0
    for fila in matriz:
        total += fila[indice]
        contador += 1
    
    if contador == 0:
        return 0.0
    
    return total / contador

def selection_sort_matriz(matriz: list[list], indice_columna: int, modo: str ="ASC") -> list[list]:
    """Ordena la matriz según el indice_columna en orden ascendente o descendente.

    Args:
        matriz (list[list]): matriz a ordenar
        indice_columna (int): columna a ordenar
        modo (str, optional): decide si se ordena de forma DES o ASC. "ASC" por defecto

    Returns:
        list[list]: matriz ordenada
    """
    for inicio in range(len(matriz)):  
        indice_extremo = buscar_extremo_matriz(matriz, inicio, indice_columna, modo)

        temporal = matriz[inicio]
        matriz[inicio] = matriz[indice_extremo]
        matriz[indice_extremo] = temporal
        
    return matriz

def buscar_extremo_matriz(matriz: list[list], inicio: int, indice_columna: int, modo: str ="ASC") -> int:
    """Devuelve el indice del valor extremo, en la columna, desde la posición "inicio"

    Args:
        matriz (list[list]): matriz a ordenar
        inicio (int): valor inicial del ordenamiento
        indice_columna (int): columna a ordenar
        modo (str, optional): decide si se ordena de forma DES o ASC. "ASC" por defecto

    Returns:
        int: ultimo indice de la matriz
    """
    extremo = inicio
    for i in range(inicio + 1, len(matriz)): 

        if modo == "DES":
            if matriz[i][indice_columna] > matriz[extremo][indice_columna]:
                extremo = i

        elif modo == "ASC":
            if matriz[i][indice_columna] < matriz[extremo][indice_columna]:
                extremo = i
        else:                
            print("ERROR, modo de ordenamiento invalido")
    return extremo