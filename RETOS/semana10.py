# ==========================================================
# RETO SEMANA 10 - FUNDAMENTOS DE PYTHON
# Listas: crear y eliminar elementos repetidos
# ==========================================================


# ==========================================================
# FUNCIÓN: CREAR UNA LISTA
# ==========================================================

def crear_lista(nombre_lista):
    """
    Esta función pregunta al usuario cuántos elementos
    quiere en la lista y luego le pide cada elemento,
    uno por uno. Devuelve la lista ya construida.
    """

    # Pedimos la longitud de la lista
    longitud = int(input(f"¿Cuántos elementos tendrá {nombre_lista}?: "))

    lista = []   # lista: aquí se van a ir guardando los elementos que escriba el usuario

    for i in range(longitud):
        elemento = input(f"  Elemento {i + 1} de {nombre_lista}: ")
        lista.append(elemento)

    return lista


# ==========================================================
# FUNCIÓN: ELIMINAR ELEMENTOS REPETIDOS
# ==========================================================

def eliminar_repetidos(lista_1, lista_2):
    """
    Esta función recibe dos listas y devuelve una lista nueva
    con los elementos de lista_1 que NO aparecen en lista_2.
    """

    # lista_resultado: nueva lista, solo con lo que sobrevive del filtro
    lista_resultado = []

    for elemento in lista_1:
        # Si el elemento NO está en la segunda lista, lo conservamos
        if elemento not in lista_2:
            lista_resultado.append(elemento)

    return lista_resultado


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    print("========================================")
    print("     RETO SEMANA 10 - LISTAS")
    print("========================================\n")

    # Creamos la primera lista
    print("--- Lista 1 ---")
    lista_1 = crear_lista("la lista 1")

    # Creamos la segunda lista
    print("\n--- Lista 2 ---")
    lista_2 = crear_lista("la lista 2")

    # Mostramos las listas originales
    print("\n========================================")
    print("LISTAS ORIGINALES")
    print("========================================")
    print(f"Lista 1: {lista_1}")
    print(f"Lista 2: {lista_2}")

    # Eliminamos de la lista 1 los elementos que también están en la lista 2
    lista_1_filtrada = eliminar_repetidos(lista_1, lista_2)

    # Mostramos el resultado
    print("\n========================================")
    print("LISTA 1 SIN LOS ELEMENTOS REPETIDOS EN LISTA 2")
    print("========================================")
    print(f"Lista 1 filtrada: {lista_1_filtrada}")


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()