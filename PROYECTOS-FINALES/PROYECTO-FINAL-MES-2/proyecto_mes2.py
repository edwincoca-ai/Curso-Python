# ==========================================================
# PROYECTO FINAL - MES 2
# Validación y operaciones de datos
# ==========================================================


# ==========================================================
# RETO 1: LONGITUD DE UNA PALABRA
# ==========================================================

def validar_longitud():
    """
    Esta función solicita una palabra al usuario y verifica
    si su longitud está entre 4 y 8 letras.
    """

    print("\n========================================")
    print(" RETO 1: VALIDAR LONGITUD DE UNA PALABRA")
    print("========================================")

    # Pedimos una palabra al usuario
    palabra = input("Ingresa una palabra: ")

    # Calculamos la cantidad de letras
    cantidad_letras = len(palabra)

    # Verificamos si tiene entre 4 y 8 letras
    if cantidad_letras >= 4 and cantidad_letras <= 8:
        print("La palabra es correcta.")

    # Verificamos si tiene menos de 4 letras
    elif cantidad_letras < 4:
        print(
            f"Hacen falta letras. Solo tiene "
            f"{cantidad_letras} letras."
        )

    # Si tiene más de 8 letras
    else:
        print(
            f"Sobran letras. Tiene "
            f"{cantidad_letras} letras."
        )


# ==========================================================
# RETO 2: ENCUENTRA EL CUADRANTE
# ==========================================================

def encontrar_cuadrante():
    """
    Esta función solicita las coordenadas X y Y
    y determina en cuál de los cuatro cuadrantes
    se encuentra el punto.
    """

    print("\n========================================")
    print(" RETO 2: ENCUENTRA EL CUADRANTE")
    print("========================================")

    # Pedimos las coordenadas al usuario
    x = int(input("Ingrese el valor de X: "))
    y = int(input("Ingrese el valor de Y: "))

    # Verificamos que ninguna coordenada sea 0
    if x == 0 or y == 0:
        print(
            "El punto se encuentra sobre uno de los ejes "
            "y no pertenece a ningún cuadrante."
        )

    # Cuadrante I: X positiva y Y positiva
    elif x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")

    # Cuadrante II: X negativa y Y positiva
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")

    # Cuadrante III: X negativa y Y negativa
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")

    # Cuadrante IV: X positiva y Y negativa
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    """
    Función principal que ejecuta los dos retos.
    """

    print("========================================")
    print("      PROYECTO FINAL DEL MES 2")
    print("   VALIDACIÓN Y OPERACIONES DE DATOS")
    print("========================================")

    # Ejecutamos el primer reto
    validar_longitud()

    # Ejecutamos el segundo reto
    encontrar_cuadrante()

    print("\n========================================")
    print("      PROYECTO FINAL TERMINADO")
    print("========================================")


# Ejecutamos la función principal
if __name__ == "__main__":
    main()