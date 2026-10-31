# ==========================================================
# RETO SEMANA 15 - FUNDAMENTOS DE PYTHON
# CONSULTA DEL CLIMA MEDIANTE LA API DE OPENWEATHER
# ==========================================================

import os
from getpass import getpass
from datetime import datetime, timedelta, timezone

import requests


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

URL = "https://api.openweathermap.org/data/3.0/onecall"

# Coordenadas de ejemplo: Ciudad de México
LATITUD = 19.4326
LONGITUD = -99.1332

DIAS_SEMANA = (
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
)


# ==========================================================
# FUNCIÓN 1: OBTENER LA API KEY
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
# FUNCIÓN 2: CONSULTAR LA API
# ==========================================================

def consultar_clima(api_key):

    parametros = {
        "lat": LATITUD,
        "lon": LONGITUD,
        "exclude": "minutely,hourly,alerts",
        "units": "metric",
        "lang": "es",
        "appid": api_key
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
            print("Error: la respuesta no es un objeto JSON.")
            return None

        return datos

    except requests.exceptions.Timeout:

        print("Error: el servidor tardó demasiado.")
        return None

    except requests.exceptions.HTTPError:

        codigo = respuesta.status_code

        mensajes = {
            400: "Parámetros incorrectos.",
            401: "API Key inválida o acceso no habilitado.",
            403: "Acceso denegado.",
            404: "Información no encontrada.",
            429: "Límite de consultas alcanzado."
        }

        mensaje = mensajes.get(
            codigo,
            "Error inesperado del servidor."
        )

        print(f"Error {codigo}: {mensaje}")

        return None

    except requests.exceptions.RequestException:

        print("Error: no se pudo conectar con OpenWeather.")
        return None

    except ValueError:

        print("Error: la respuesta no contiene JSON válido.")
        return None


# ==========================================================
# FUNCIÓN 3: CONVERTIR FECHA Y HORA
# ==========================================================

def convertir_fecha(timestamp, desfase):

    zona_local = timezone(
        timedelta(seconds=desfase)
    )

    fecha = datetime.fromtimestamp(
        timestamp,
        tz=zona_local
    )

    return fecha


# ==========================================================
# FUNCIÓN 4: MOSTRAR EL CLIMA ACTUAL
# ==========================================================

def mostrar_clima_actual(datos):

    actual = datos["current"]
    hoy = datos["daily"][0]

    desfase = datos["timezone_offset"]

    fecha = convertir_fecha(
        actual["dt"],
        desfase
    )

    descripcion = actual["weather"][0][
        "description"
    ].capitalize()

    temperatura = actual["temp"]

    sensacion = actual["feels_like"]

    humedad = actual["humidity"]

    nubosidad = actual["clouds"]

    presion = actual["pressure"]

    viento = actual["wind_speed"] * 3.6

    uv = actual["uvi"]

    minima = hoy["temp"]["min"]

    maxima = hoy["temp"]["max"]

    print("\n====================================")
    print("          CLIMA ACTUAL")
    print("====================================")

    print(f"Zona horaria: {datos['timezone']}")

    print(
        f"Fecha: {fecha.strftime('%d/%m/%Y %H:%M')}"
    )

    print(f"Condición: {descripcion}")

    print(f"Temperatura: {temperatura:.1f} °C")

    print(f"Sensación térmica: {sensacion:.1f} °C")

    print(f"Temperatura mínima: {minima:.1f} °C")

    print(f"Temperatura máxima: {maxima:.1f} °C")

    print(f"Humedad: {humedad}%")

    print(f"Nubosidad: {nubosidad}%")

    print(f"Presión: {presion} hPa")

    print(f"Velocidad del viento: {viento:.1f} km/h")

    print(f"Índice UV: {uv}")


# ==========================================================
# FUNCIÓN 5: PRONÓSTICO DE LOS PRÓXIMOS 3 DÍAS
# ==========================================================

def mostrar_pronostico(datos):

    desfase = datos["timezone_offset"]

    print("\n====================================")
    print("      PRONÓSTICO DE 3 DÍAS")
    print("====================================")

    for dia in datos["daily"][1:4]:

        fecha = convertir_fecha(
            dia["dt"],
            desfase
        )

        nombre_dia = DIAS_SEMANA[
            fecha.weekday()
        ].capitalize()

        descripcion = dia["weather"][0][
            "description"
        ].capitalize()

        minima = dia["temp"]["min"]

        maxima = dia["temp"]["max"]

        probabilidad_lluvia = dia["pop"] * 100

        print(
            f"\n{nombre_dia} "
            f"{fecha.strftime('%d/%m/%Y')}"
        )

        print(f"Condición: {descripcion}")

        print(f"Mínima: {minima:.1f} °C")

        print(f"Máxima: {maxima:.1f} °C")

        print(
            f"Probabilidad de lluvia: "
            f"{probabilidad_lluvia:.0f}%"
        )


# ==========================================================
# FUNCIÓN 6: PROGRAMA PRINCIPAL
# ==========================================================

def main():

    print("====================================")
    print("       RETO SEMANA 15")
    print("       CLIMA CON OPENWEATHER")
    print("====================================")

    api_key = obtener_api_key()

    print("\nConsultando información meteorológica...")

    datos = consultar_clima(api_key)

    if datos is None:

        print("No fue posible obtener el clima.")
        return

    try:

        mostrar_clima_actual(datos)

        mostrar_pronostico(datos)

    except (KeyError, IndexError, TypeError):

        print(
            "Error: la API no proporcionó "
            "todos los datos esperados."
        )


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()