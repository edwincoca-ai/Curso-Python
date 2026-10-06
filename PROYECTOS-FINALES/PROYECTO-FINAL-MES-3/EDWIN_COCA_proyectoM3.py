# =====================================================
# Proyecto M3 - Simulación de la Máquina de Galton
# Autor: Edwin Coca
# Descripción: simula 3000 canicas que caen por 12 niveles
# de obstáculos y muestra un histograma con los resultados.
# =====================================================

# random: para generar números aleatorios (la "moneda" de cada nivel)
import random
# matplotlib.pyplot: para dibujar el histograma (se abrevia como plt)
import matplotlib.pyplot as plt

# ---------- Datos del problema ----------
# Cantidad de canicas que se sueltan en la simulación
NUMERO_CANICAS = 3000
# Cantidad de niveles de obstáculos por los que cae cada canica
NUMERO_NIVELES = 12


# ---------- Función 1: simular las canicas ----------
def calcular_resultados(num_canicas, niveles):
    """Simula las canicas y devuelve el contenedor final de cada una.

    En cada nivel la canica elige izquierda o derecha al azar.
    El contenedor final es el número de veces que fue a la derecha.
    """
    # Lista donde se guarda el contenedor final de cada canica
    resultados = []

    # Se repite el proceso una vez por cada canica
    for _ in range(num_canicas):
        # Cada canica empieza sin ninguna derecha (contenedor 0)
        contenedor = 0

        # La canica baja por todos los niveles de obstáculos
        for _ in range(niveles):
            # 0 = izquierda, 1 = derecha (50 % de probabilidad cada una)
            direccion = random.randint(0, 1)

            # Si se fue a la derecha, avanza un contenedor
            if direccion == 1:
                contenedor += 1

        # Guardamos el contenedor donde cayó esta canica
        resultados.append(contenedor)

    # Devolvemos los resultados de todas las canicas
    return resultados


# ---------- Función 2: graficar el histograma ----------
def graficar_histograma(resultados, niveles):
    """Dibuja el histograma con la cantidad de canicas por contenedor."""
    # Hay (niveles + 1) contenedores: del 0 al número de niveles.
    # El rango de -0.5 a niveles + 0.5 centra cada barra sobre su número.
    plt.hist(
        resultados,
        bins=niveles + 1,
        range=(-0.5, niveles + 0.5),
        edgecolor="black"
    )

    # Título de la gráfica y nombres de los ejes
    plt.title("Simulación de una Máquina de Galton")
    plt.xlabel("Contenedor")
    plt.ylabel("Cantidad de canicas")

    # Se muestra un número en el eje X por cada contenedor
    plt.xticks(range(niveles + 1))

    # Se muestra la gráfica en pantalla
    plt.show()


# ---------- Programa principal ----------
# Se simulan todas las canicas
resultados = calcular_resultados(NUMERO_CANICAS, NUMERO_NIVELES)

# Se grafican los resultados
graficar_histograma(resultados, NUMERO_NIVELES)