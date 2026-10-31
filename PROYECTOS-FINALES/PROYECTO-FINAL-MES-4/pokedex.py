# ==========================================================
# PROYECTO FINAL MES 4 - FUNDAMENTOS DE PYTHON
# CONSTRUYE UNA POKEDEX
# ==========================================================
#
# Objetivo:
# Buscar un Pokemon mediante PokeAPI, mostrar sus datos,
# abrir su imagen y guardar la informacion en formato JSON.
#
# Biblioteca externa necesaria:
# requests
#
# ==========================================================

import json
import webbrowser
from pathlib import Path

import requests


# ==========================================================
# CONFIGURACION
# ==========================================================

URL_API = "https://pokeapi.co/api/v2/pokemon/"

# Carpeta donde esta guardado este programa.
CARPETA_PROYECTO = Path(__file__).resolve().parent

# Carpeta donde guardaremos los archivos JSON.
CARPETA_POKEDEX = CARPETA_PROYECTO / "pokedex"


# ==========================================================
# FUNCION 1: SOLICITAR EL NOMBRE
# ==========================================================

def solicitar_pokemon():
    """
    Solicita el nombre de un Pokemon.
    No permite que el usuario introduzca un dato vacio.
    """

    while True:

        nombre = input(
            "\nIntroduce el nombre de un Pokemon: "
        ).strip().lower()

        if nombre == "":
            print("Error: debes escribir un nombre.")
            continue

        return nombre


# ==========================================================
# FUNCION 2: CONSULTAR LA API
# ==========================================================

def consultar_pokemon(nombre):
    """
    Consulta PokeAPI mediante una peticion HTTP GET.

    Devuelve un diccionario si la consulta funciona.
    Devuelve None si ocurre algun error.
    """

    try:

        respuesta = requests.get(
            URL_API + nombre,
            timeout=10
        )

        # Revisamos los codigos HTTP.
        if respuesta.status_code == 200:

            return respuesta.json()

        elif respuesta.status_code == 404:

            print(
                f"\nError 404: el Pokemon '{nombre}' "
                "no fue encontrado."
            )

        elif respuesta.status_code == 429:

            print(
                "\nError 429: demasiadas solicitudes. "
                "Intenta nuevamente mas tarde."
            )

        else:

            print(
                f"\nError HTTP {respuesta.status_code}: "
                "no se pudo completar la consulta."
            )

    except requests.exceptions.Timeout:

        print(
            "\nError: el servidor tardo demasiado "
            "en responder."
        )

    except requests.exceptions.RequestException:

        print(
            "\nError: no se pudo conectar con PokeAPI. "
            "Revisa tu conexion a internet."
        )

    except ValueError:

        print(
            "\nError: la respuesta de la API "
            "no contiene un JSON valido."
        )

    return None


# ==========================================================
# FUNCION 3: ORGANIZAR LOS DATOS
# ==========================================================

def organizar_datos(datos):
    """
    Extrae la informacion que solicita el proyecto.
    La devuelve organizada en un diccionario.
    """

    nombre = datos["name"]
    numero = datos["id"]

    # PokeAPI entrega el peso en hectogramos.
    peso_kg = datos["weight"] / 10

    # PokeAPI entrega la altura en decimetros.
    altura_m = datos["height"] / 10

    tipos = [
        elemento["type"]["name"]
        for elemento in datos["types"]
    ]

    habilidades = [
        elemento["ability"]["name"]
        for elemento in datos["abilities"]
    ]

    movimientos = [
        elemento["move"]["name"]
        for elemento in datos["moves"]
    ]

    # Obtenemos el enlace de la imagen frontal.
    imagen = datos["sprites"]["front_default"]

    pokemon = {
        "numero": numero,
        "nombre": nombre,
        "peso_kg": peso_kg,
        "altura_m": altura_m,
        "tipos": tipos,
        "habilidades": habilidades,
        "movimientos": movimientos,
        "imagen_frontal": imagen
    }

    return pokemon


# ==========================================================
# FUNCION 4: MOSTRAR LA INFORMACION
# ==========================================================

def mostrar_pokemon(pokemon):
    """
    Muestra en pantalla los datos del Pokemon.
    """

    print("\n========================================")
    print("             MI POKEDEX")
    print("========================================")

    print(f"\nNumero: {pokemon['numero']}")
    print(f"Nombre: {pokemon['nombre'].capitalize()}")

    print(f"Peso: {pokemon['peso_kg']:.1f} kg")
    print(f"Altura: {pokemon['altura_m']:.1f} m")

    print("\nTIPOS:")

    for tipo in pokemon["tipos"]:
        print(f"- {tipo}")

    print("\nHABILIDADES:")

    for habilidad in pokemon["habilidades"]:
        print(f"- {habilidad}")

    print("\nMOVIMIENTOS:")

    for movimiento in pokemon["movimientos"]:
        print(f"- {movimiento}")

    print("\nIMAGEN FRONTAL:")

    if pokemon["imagen_frontal"]:

        print(pokemon["imagen_frontal"])

    else:

        print("Imagen no disponible.")


# ==========================================================
# FUNCION 5: MOSTRAR LA IMAGEN
# ==========================================================

def mostrar_imagen(pokemon):
    """
    Abre la imagen frontal en el navegador.
    """

    imagen = pokemon["imagen_frontal"]

    if not imagen:

        print("\nEste Pokemon no tiene imagen frontal.")
        return

    try:

        abierto = webbrowser.open(imagen)

        if abierto:
            print("\nSe intento abrir la imagen en el navegador.")
        else:
            print("\nNo se pudo abrir el navegador automaticamente.")

    except Exception as error:

        print(
            "\nNo fue posible abrir la imagen: "
            f"{error}"
        )


# ==========================================================
# FUNCION 6: GUARDAR EL ARCHIVO JSON
# ==========================================================

def guardar_pokemon(pokemon):
    """
    Crea la carpeta pokedex si no existe.

    Guarda toda la informacion del Pokemon
    dentro de un archivo JSON.
    """

    try:

        CARPETA_POKEDEX.mkdir(
            parents=True,
            exist_ok=True
        )

        nombre_archivo = (
            f"{pokemon['nombre']}.json"
        )

        ruta_archivo = (
            CARPETA_POKEDEX / nombre_archivo
        )

        with open(
            ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                pokemon,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(
            "\nPokemon guardado correctamente en:"
        )

        print(ruta_archivo)

        return True

    except OSError as error:

        print(
            "\nError al guardar el archivo JSON: "
            f"{error}"
        )

        return False


# ==========================================================
# FUNCION 7: MENU PRINCIPAL
# ==========================================================

def main():

    print("========================================")
    print("       PROYECTO FINAL - MES 4")
    print("          POKEDEX EN PYTHON")
    print("========================================")

    while True:

        print("\n1. Buscar un Pokemon")
        print("2. Salir")

        opcion = input(
            "\nSelecciona una opcion: "
        ).strip()

        if opcion == "1":

            nombre = solicitar_pokemon()

            print("\nConsultando PokeAPI...")

            datos = consultar_pokemon(nombre)

            if datos is None:
                continue

            try:

                pokemon = organizar_datos(datos)

            except (KeyError, IndexError, TypeError, ValueError):

                print(
                    "\nError: la API no devolvio "
                    "los datos esperados."
                )

                continue

            mostrar_pokemon(pokemon)

            mostrar_imagen(pokemon)

            guardar_pokemon(pokemon)

        elif opcion == "2":

            print(
                "\nGracias por utilizar mi Pokedex."
            )

            print("Programa finalizado.")

            break

        else:

            print(
                "\nOpcion incorrecta. "
                "Selecciona 1 o 2."
            )


# ==========================================================
# EJECUCION DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()