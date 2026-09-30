# ==========================================================
# MÓDULO m_retosemanal.py
# Funciones para el reto de la semana 11
# ==========================================================


def pedir_entero_positivo(mensaje):
    """
    Pide un número entero mayor que 0 y repite la pregunta
    hasta que el usuario escriba un valor válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: debes ingresar un número entero.")
            continue

        if valor <= 0:
            print("Error: el número debe ser mayor que 0.")
            continue

        return valor


def crear_lista(numero_lista):
    """
    Pide al usuario la longitud de una lista y cada uno de
    sus elementos. Devuelve la lista ya construida.
    """
    longitud = pedir_entero_positivo(
        f"¿Cuántos elementos tendrá la lista {numero_lista}?: "
    )

    lista = []
    for i in range(longitud):
        elemento = input(f"  Elemento {i + 1} de la lista {numero_lista}: ").strip()
        lista.append(elemento)

    return lista


def crear_listas():
    """
    Pregunta cuántas listas se van a crear, las construye
    una por una y devuelve una lista de listas.
    """
    cantidad = pedir_entero_positivo("¿Cuántas listas quieres crear?: ")

    listas = []
    for numero in range(1, cantidad + 1):
        print(f"\n--- Lista {numero} ---")
        listas.append(crear_lista(numero))

    return listas


def eliminar_repetidos(listas):
    """
    Recibe una lista de listas y devuelve una lista de listas nueva
    donde, a cada lista, se le quitan los elementos que aparecen
    en cualquiera de las listas posteriores.
    Las listas originales no se modifican.
    """
    resultado = []

    for indice in range(len(listas)):
        lista_actual = listas[indice]
        posteriores = listas[indice + 1:]   # todas las listas que van después

        lista_filtrada = []
        for elemento in lista_actual:
            repetido = False
            for otra in posteriores:
                if elemento in otra:
                    repetido = True
                    break
            if not repetido:
                lista_filtrada.append(elemento)

        resultado.append(lista_filtrada)

    return resultado


def imprimir_listas(listas, titulo):
    """
    Imprime un título y cada lista numerada.
    """
    print("\n========================================")
    print(titulo)
    print("========================================")
    for numero, lista in enumerate(listas, start=1):
        print(f"Lista {numero}: {lista}")