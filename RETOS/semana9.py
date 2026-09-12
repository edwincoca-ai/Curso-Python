# ==========================================================
# RETO SEMANA 9 - FUNDAMENTOS DE PYTHON
# Letra anterior y siguiente usando ord() y chr()
# ==========================================================


def letras_adyacentes(letra):
    """
    Recibe una letra y muestra
    la letra anterior y la siguiente.
    """

    codigo = ord(letra)

    # Letra anterior
    if codigo == ord("a"):
        anterior = "No existe"
    else:
        anterior = chr(codigo - 1)

    # Letra siguiente
    if codigo == ord("z"):
        siguiente = "No existe"
    else:
        siguiente = chr(codigo + 1)

    print(f"Letra ingresada: {letra}")
    print(f"Letra anterior: {anterior}")
    print(f"Letra siguiente: {siguiente}")


def main():

    print("========================================")
    print("     RETO SEMANA 9 - ALFABETO")
    print("========================================")
    print("Escribe una letra para conocer su")
    print("letra anterior y siguiente.")
    print("Para salir, escribe: salir")
    print("========================================")

    while True:

        letra = input("\nIngresa una letra: ").strip()

        if letra.lower() == "salir":
            print("\nPrograma terminado. ¡Hasta luego!")
            break

        if len(letra) != 1:
            print("Error: debes ingresar solamente una letra.")
            continue

        letra = letra.lower()

        if letra < "a" or letra > "z":
            print("Error: ingresa una letra del alfabeto.")
            continue

        letras_adyacentes(letra)


if __name__ == "__main__":
    main()