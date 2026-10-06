import matplotlib.pyplot as plt


# Pedimos el rango de años
año_inicial = int(input("Ingresa el año inicial: "))
año_final = int(input("Ingresa el año final: "))

# Listas para guardar los años y las ventas
años = []
ventas = []


# Recorremos todos los años del rango
for año in range(año_inicial, año_final + 1):

    venta = float(input(f"Ingresa las ventas del año {año}: "))

    años.append(año)
    ventas.append(venta)


# Creamos la gráfica de líneas
plt.plot(años, ventas, marker="o")

# Agregamos título y nombres a los ejes
plt.title(f"Ventas del {año_inicial} al {año_final}")
plt.xlabel("Año")
plt.ylabel("Ventas")

# Mostramos cada año en el eje X
plt.xticks(años)

# Mostramos la gráfica
plt.show()