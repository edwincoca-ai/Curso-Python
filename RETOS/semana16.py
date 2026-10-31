# ==========================================================
# RETO SEMANA 16 - FUNDAMENTOS DE PYTHON
# CONSULTOR DEL CLIMA CON OPENWEATHER
# ==========================================================
#
# OBJETIVO:
# Consultar el clima utilizando:
# 1. Nombre de ciudad y código del país.
# 2. Latitud y longitud.
#
# Incluye validación de datos y manejo de excepciones.
#
# REQUISITO:
# Instalar requests con:
# python -m pip install requests
#
# ==========================================================

import os
from getpass import getpass

import requests


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

URL = "https://api.openweathermap.org/data/2.5/weather"


# ==========================================================
# FUNCIÓN 1: OBTENER API KEY
# ==========================================================

def obtener_api_key():

    api_key = os.environ.get(
        "OPENWEATHER_API_KEY", ""
    ).strip()

    while not api_key:

        api_key = getpass(
            "Introduce tu API Key de OpenWeather: "
        ).strip()

        if not api_key:
            print("Error: la API Key no puede estar vacía.")

    return api_key


# ==========================================================
# FUNCIÓN 2: SOLICITAR CIUDAD
# ==========================================================

def solicitar_ciudad():

    while True:

        ubicacion = input(
            "\nIntroduce CIUDAD,CODIGO_PAIS "
            "(ejemplo: Mexico City,MX): "
        ).strip()

        partes = ubicacion.split(",")

        if len(partes) != 2:
            print(
                "Error: utiliza el formato CIUDAD,CODIGO_PAIS."
            )
            continue

        ciudad = partes[0].strip()
        pais = partes[1].strip().upper()

        if not ciudad:
            print("Error: el nombre de la ciudad está vacío.")
            continue

        if not pais:
            print("Error: el código del país está vacío.")
            continue

        if not pais.isalpha() or len(pais) != 2:
            print(
                "Error: el país debe tener dos letras, "
                "por ejemplo MX, US o JP."
            )
            continue

        return ciudad, pais


# ==========================================================
# FUNCIÓN 3: SOLICITAR COORDENADAS
# ==========================================================

def solicitar_coordenadas():

    while True:

        try:

            latitud = float(
                input("\nIntroduce la latitud: ")
            )

            if not -90 <= latitud <= 90:
                print(
                    "Error: la latitud debe estar "
                    "entre -90 y 90."
                )
                continue

            longitud = float(
                input("Introduce la longitud: ")
            )

            if not -180 <= longitud <= 180:
                print(
                    "Error: la longitud debe estar "
                    "entre -180 y 180."
                )
                continue

            return latitud, longitud

        except ValueError:

            print(
                "Error: las coordenadas deben "
                "ser números válidos."
            )


# ==========================================================
# FUNCIÓN 4: ELEGIR TIPO DE CONSULTA
# ==========================================================

def elegir_ubicacion():

    while True:

        print("\n====================================")
        print("       SELECCIONAR UBICACIÓN")
        print("====================================")

        print("1. Buscar por ciudad y país")
        print("2. Buscar por coordenadas")

        opcion = input(
            "\nSelecciona una opción (1 o 2): "
        ).strip()

        if opcion == "1":

            ciudad, pais = solicitar_ciudad()

            return {
                "q": f"{ciudad},{pais}"
            }

        elif opcion == "2":

            latitud, longitud = solicitar_coordenadas()

            return {
                "lat": latitud,
                "lon": longitud
            }

        else:

            print(
                "Error: selecciona únicamente 1 o 2."
            )


# ==========================================================
# FUNCIÓN 5: CONSULTAR OPENWEATHER
# ==========================================================

def consultar_clima(api_key, ubicacion):

    parametros = {
        **ubicacion,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    try:

        respuesta = requests.get(
            URL,
            params=parametros,
            timeout=10
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        if not isinstance(datos, dict):
            print(
                "Error: formato de respuesta incorrecto."
            )
            return None

        return datos

    except requests.exceptions.Timeout:

        print(
            "Error: el servidor tardó demasiado "
            "en responder."
        )

    except requests.exceptions.HTTPError:

        codigo = respuesta.status_code

        if codigo == 400:

            print(
                "Error 400: los datos enviados "
                "son incorrectos."
            )

        elif codigo == 401:

            print(
                "Error 401: API Key inválida "
                "o todavía no activada."
            )

        elif codigo == 404:

            print(
                "Error 404: no se encontró la ciudad "
                "o ubicación solicitada."
            )

        elif codigo == 429:

            print(
                "Error 429: se alcanzó el límite "
                "de consultas."
            )

        else:

            print(
                f"Error HTTP {codigo}: "
                "no se pudo completar la consulta."
            )

    except requests.exceptions.RequestException:

        print(
            "Error: revisa tu conexión a internet."
        )

    except ValueError:

        print(
            "Error: la respuesta no contiene "
            "un JSON válido."
        )

    return None


# ==========================================================
# FUNCIÓN 6: MOSTRAR RESULTADOS
# ==========================================================

def mostrar_clima(datos):

    try:

        ciudad = datos["name"]

        pais = datos["sys"]["country"]

        descripcion = datos["weather"][0][
            "description"
        ]

        temperatura = datos["main"]["temp"]

        sensacion = datos["main"]["feels_like"]

        humedad = datos["main"]["humidity"]

        viento = datos["wind"]["speed"] * 3.6

        print("\n====================================")
        print("        RESULTADO DEL CLIMA")
        print("====================================")

        print(
            f"\nEl clima en {ciudad}, {pais} "
            f"es {descripcion}."
        )

        print(f"\nTemperatura: {temperatura:.1f} °C")

        print(
            f"Sensación térmica: {sensacion:.1f} °C"
        )

        print(f"Humedad: {humedad}%")

        print(
            f"Velocidad del viento: "
            f"{viento:.1f} km/h"
        )

    except (KeyError, IndexError, TypeError, ValueError):

        print(
            "Error: la API no proporcionó "
            "todos los datos esperados."
        )


# ==========================================================
# FUNCIÓN 7: PROGRAMA PRINCIPAL
# ==========================================================

def main():

    print("====================================")
    print("          RETO SEMANA 16")
    print("       CONSULTOR DEL CLIMA")
    print("====================================")

    api_key = obtener_api_key()

    ubicacion = elegir_ubicacion()

    print("\nConsultando el clima...")

    datos = consultar_clima(
        api_key,
        ubicacion
    )

    if datos is None:

        print(
            "\nNo fue posible obtener "
            "la información meteorológica."
        )

        return

    mostrar_clima(datos)

    print("\nConsulta finalizada.")


# ==========================================================
# EJECUCIÓN
# ==========================================================

if __name__ == "__main__":
    main()