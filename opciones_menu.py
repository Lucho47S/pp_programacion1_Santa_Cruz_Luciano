import funciones_base as fun
import validaciones as val
import os

def mostrar_menu():
    """
    Funcion que imprime el menu de opciones
    """
    print("""
          --- Ejército Real de Autodefensa de la Tierra ---

          Seleccione una opcion agente:

          1-Crear Matriz
          2-Agregar Personaje
          3-Existencias
          4-Existencias personajes Human
          5-Existencias personajes que no sean Human
          6-Mostrar Detalle
          7-Mostrar Saiyan
          8-Mostrar más poderoso
          9-Mostrar más inteligente
          10-Filtrar Menor velocidad
          11-Filtrar Débiles
          12-Filtrar No-Binarios veloces
          13-Promedios Inteligencia
          14-Filtrar Kryptonian
          15-Filtrar Saiyan Power
          16-Ordenar por Más Inteligente
          17-Ordenar por Menos Inteligente [not Human]
          18-Ordenar por Más Poder [not Human]
          19-Ordenar por Más Velocidad
          22-Cerrar
          """)


def start(nombres:list, alias:list, razas:list, generos:list, poderes:list, inteligencias:list, velocidades:list) -> None:
    """funcion que contiene el bucle principal y las listas dadas por la consigna

    Args:
        nombres (list): lista de nombres de la libreria utn_fra
        alias (list): lista de alias de la libreria utn_fra
        razas (list): lista de razas de la libreria utn_fra
        generos (list): lista de generosde la libreria utn_fra
        poderes (list): lista de poderes de la libreria utn_fra
        inteligencias (list): lista de inteligencias de la libreria utn_fra
        velocidades (list): lista de velocidades de la libreria utn_fra
    """

    matriz = []

    while True:
        mostrar_menu()
        opcion = int(val.validar_modo("Selecciona una opcion: ", "digit"))

        match opcion:
            case 1:
                matriz = fun.rellenar_matriz_con_datos(nombres, alias, razas, generos, poderes, inteligencias, velocidades)
                print("Matriz Creada Correctamente, proceda")

            case 2:
                if val.validacion_existe_matriz(matriz):
                    fun.agregar_personaje_matriz(matriz)
            
            case 3:
                if val.validacion_existe_matriz(matriz):
                    print(f"Existencias de la matriz: {fun.existencias_de_tag(matriz, 2, "")}")

            case 4:
                if val.validacion_existe_matriz(matriz):
                    print(f"Existencias de tipo Human: {fun.existencias_de_tag(matriz, 2, "Human")}")

            case 5:
                if val.validacion_existe_matriz(matriz):
                    print(f"Existencias de tipo diferente a Human: {fun.existencias_de_tag(matriz, 2, "Human", True)}")

            case 6:
                if val.validacion_existe_matriz(matriz):
                    matriz_truncada = fun.recorrido_de_matriz(matriz)
                    fun.mostrar_matriz_personajes(matriz_truncada)

            case 7:
                if val.validacion_existe_matriz(matriz):
                    print(f"{fun.existencias_de_tag(matriz, 2, "Saiyan", False)} Existencias de tipo Saiyan encontradas:")
                    fun.mostrar_matriz_personajes(fun.filtrar_tag(matriz, 2, "Saiyan"))
            
            case 8:
                if val.validacion_existe_matriz(matriz):
                    mas_poderosos = fun.filtrar_por_valor(matriz, 4, "==", fun.buscar_valor_extremo(matriz, 4, "max"))
                    print(f"{len(mas_poderosos)} Existencias encontradas con poder {fun.buscar_valor_extremo(matriz, 4, "max")}: ")
                    fun.mostrar_matriz_personajes(mas_poderosos)
            
            case 9:
                if val.validacion_existe_matriz(matriz):
                    mas_inteligentes = fun.filtrar_por_valor(matriz, 5, "==", fun.buscar_valor_extremo(matriz, 5, "max"))

                    print(f"{len(mas_inteligentes)} Existencias encontradas con inteligencia de {fun.buscar_valor_extremo(matriz, 5, "max")}")
                    fun.mostrar_matriz_personajes(mas_inteligentes)

            case 10:
                if val.validacion_existe_matriz(matriz):
                    promedio_velocidad_general = fun.calcular_promedio(matriz, 6)
                    matriz_lentos_filtrada = fun.filtrar_por_valor(matriz, 6, "<", promedio_velocidad_general)

                    print(f"{len(matriz_lentos_filtrada)} Existencias encontradas menores al promedio de velocidad de {promedio_velocidad_general}")
                    fun.mostrar_matriz_personajes(matriz_lentos_filtrada)
            
            case 11:
                if val.validacion_existe_matriz(matriz):
                    poder_saiyan = fun.buscar_valor_extremo(fun.filtrar_tag(matriz, 2, "Saiyan"), 4, "min")
                    matriz_menor_sayain =  fun.filtrar_por_valor(matriz, 4, "<", poder_saiyan)
                    print(f"{len(matriz_menor_sayain)} Existencias encontradas con poder menor al de los Saiyans:")
                    fun.mostrar_matriz_personajes(matriz_menor_sayain)
            
            case 12:
                if val.validacion_existe_matriz(matriz):
                    velocidad_NB = fun.buscar_valor_extremo(fun.filtrar_tag(matriz, 3, "No-Binario"), 6, "max")
                    matriz_rapido_NB = fun.filtrar_por_valor(fun.filtrar_tag(matriz, 3, "No-Binario"), 6, "==", velocidad_NB)
                    print(f"{len(matriz_rapido_NB)} Existencias encontradas de genero No-Binario con mayor velocidad:")
                    fun.mostrar_matriz_personajes(matriz_rapido_NB)
            
            case 13:
                if val.validacion_existe_matriz(matriz):
                    promedio_androides = fun.calcular_promedio(fun.filtrar_tag(matriz, 2, "Android"), 4) + fun.calcular_promedio(fun.filtrar_tag(matriz, 2, "Android"), 5) / 2
                    promedio_androides = promedio_androides / 2

                    print(f"""
                    Promedio de inteligencia de un Android: {fun.calcular_promedio(fun.filtrar_tag(matriz, 2, "Android"), 5)}
                    Promedio de poder de un Android: {fun.calcular_promedio(fun.filtrar_tag(matriz, 2, "Android"), 4)}
                    Promedio de ambos: {promedio_androides}""")

            case 14:
                if val.validacion_existe_matriz(matriz):
                    matriz_no_kryptonian = fun.filtrar_tag(matriz, 2, "Kryptonian", True)
                    matriz_kryptonian = fun.filtrar_tag(matriz, 2, "Kryptonian")
                    promedio_kryptonian = fun.calcular_promedio(matriz_kryptonian, 4)
                    matriz_anti_kryptonian = fun.filtrar_por_valor(matriz_no_kryptonian, 4, ">=", promedio_kryptonian)

                    print(f"Estos son los no-Kryptonian que superan/igualan el promedio de poder de los Kryptonian: ")
                    fun.mostrar_matriz_personajes(matriz_anti_kryptonian)
            
            case 15:
                if val.validacion_existe_matriz(matriz):
                    saiyan = fun.filtrar_tag(matriz, 2, "Saiyan")
                    no_saiyan = fun.filtrar_tag(matriz, 2, "Saiyan", True)
                    indice_saiyan = (fun.calcular_promedio(saiyan, 4) + fun.calcular_promedio(saiyan, 5) + fun.calcular_promedio(saiyan, 6)) / 3

                    comp_1 = fun.filtrar_por_valor(no_saiyan, 6, "<", indice_saiyan)
                    comp_2 = fun.filtrar_por_valor(comp_1, 5, "<", indice_saiyan)
                    comp_3 = fun.filtrar_por_valor(comp_2, 4, "<", indice_saiyan)

                    print(f"Personajes con stats menores al indice Sayain ({indice_saiyan}): ")
                    fun.mostrar_matriz_personajes(comp_3)
                    
            case 16:
                if val.validacion_existe_matriz(matriz):
                    print(f"Matriz ordenada por inteligencia de forma descendente: ")
                    fun.mostrar_matriz_personajes(fun.selection_sort_matriz(matriz, 5, "DES"))
            
            case 17:
                if val.validacion_existe_matriz(matriz):
                    no_human_tontos = fun.selection_sort_matriz(fun.filtrar_tag(matriz, 2, "Human", True), 5, "ASC")
                    print(f"Matriz ordenada por inteligencia de forma ascendente [No Human]: ")
                    fun.mostrar_matriz_personajes(no_human_tontos)
            
            case 18:
                if val.validacion_existe_matriz(matriz):
                    no_human_poderosos = fun.selection_sort_matriz(fun.filtrar_tag(matriz, 2, "Human", True), 4, "DES")
                    print(f"Matriz ordenada por poder de forma descendente [No Human]: ")
                    fun.mostrar_matriz_personajes(no_human_poderosos)

            case 19:
                if val.validacion_existe_matriz(matriz):
                    print(f"Matriz ordenada por velocidades de forma ascendente: ")
                    fun.mostrar_matriz_personajes(fun.selection_sort_matriz(matriz, 6, "ASC"))
            
            case 22:
                os.system("cls")
                break

            case _:
                print("Opcion Invalida, por favor ingrese denuevo")
