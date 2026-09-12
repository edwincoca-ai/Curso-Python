# ==========================================
# RETO SEMANA 8 - Fundamentos de Python
# Diccionario de colores del arcoíris en inglés y noruego
# ==========================================

# Diccionario de colores del arcoíris en inglés
colores_ingles = {
    "rojo": "red",
    "naranja": "orange",
    "amarillo": "yellow",
    "verde": "green",
    "azul": "blue",
    "violeta": "purple",
}

# Diccionario de colores del arcoíris en noruego
colores_noruego = {
    "rojo": "rød",
    "naranja": "oransje",
    "amarillo": "gul",
    "verde": "grønn",
    "azul": "blå",
    "violeta": "fiolett",
}


def elegir_idioma():
    """Muestra los idiomas disponibles y pide al usuario que elija uno."""
    print("Idiomas disponibles:")
    print("1. Inglés")
    print("2. Noruego")

    while True:
        opcion = input("¿A cuál idioma quieres traducir? (1/2): ").strip()
        if opcion == "1":
            return "inglés", colores_ingles
        elif opcion == "2":
            return "noruego", colores_noruego
        else:
            print("Opción no válida. Escribe 1 o 2.")


def buscar_color(oracion, diccionario_colores):
    """Busca si alguno de los colores del arcoíris aparece en la oración."""
    palabras = oracion.lower().split()
    for palabra in palabras:
        # se limpia la palabra de signos de puntuación (coma, punto, etc.)
        palabra_limpia = palabra.strip(".,;:!?")
        if palabra_limpia in diccionario_colores:
            return palabra_limpia
    return None


def main():
    print("==========================================")
    print("   DICCIONARIO DE COLORES DEL ARCOÍRIS")
    print("==========================================\n")

    nombre_idioma, diccionario_colores = elegir_idioma()

    oracion = input(
        "\nEscribe una oración en español que incluya un color del arcoíris: "
    )

    color_encontrado = buscar_color(oracion, diccionario_colores)

    print("\n------------------------------------------")
    if color_encontrado:
        traduccion = diccionario_colores[color_encontrado]
        print(
            f'El color "{color_encontrado}" se dice "{traduccion}" en {nombre_idioma}.'
        )
    else:
        print(
            "No encontré ningún color del arcoíris (rojo, naranja, amarillo, "
            "verde, azul, violeta) en tu oración. Intenta de nuevo."
        )
    print("------------------------------------------")


if __name__ == "__main__":
    main()