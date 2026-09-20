cuadrados = []

for numero in range(10):
    numero = numero ** 2
    cuadrados.append(numero)

print(cuadrados)


cubos = [cubo ** 3 for cubo in range(10)]

print(cubos)


#######################################

# Crear un diccionario por medio de la comprensión de listas

cubos = {numero: numero ** 3 for numero in range(10)}

print(cubos)


pares = [numero for numero in range(1, 11) if numero % 2 == 0]

impares = [numero for numero in range(1, 11) if numero % 2 != 0]

print(pares)
print(impares)


nombres = ["ana", "fernando", "carlos", "priscila"]

print("Lista antes de la compresión:", nombres)

nombres = [nombre.capitalize() for nombre in nombres]

print("Lista después de la compresión:", nombres)