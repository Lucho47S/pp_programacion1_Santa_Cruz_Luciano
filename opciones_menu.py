import funciones_base as fun
import validaciones as val
import os

def mostrar_menu():
    print("""
          --- Ejército Real de Autodefensa de la Tierra ---

          Seleccione una opcion agente:

          1-Crear matriz
          2-Agregar Personaje
          3-Existencias
          4-Existencias Humans
          5-Existencias no Human
          6-Mostrar Detalle
          22-Cerrar
          """)


def start(nombres:list, alias:list, razas:list, generos:list, poderes:list, inteligencias:list, velocidades:list) -> None:

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
                    print(f"Existencias de la matriz: {fun.existencias_de_raza(matriz, "", False)}")

            case 4:
                if val.validacion_existe_matriz(matriz):
                    print(f"Existencias de tipo human: {fun.existencias_de_raza(matriz, "Human", False)}")

            case 5:
                if val.validacion_existe_matriz(matriz):
                    print(f"Existencias de tipo human: {fun.existencias_de_raza(matriz, "Human", True)}")
            case 6:
                if val.validacion_existe_matriz(matriz):
                    fun.mostrar_matriz_personajes(matriz)

            case 22:
                os.system("cls")
                break

            case _:
                print("Opcion Invalida, por favor ingrese denuevo")
