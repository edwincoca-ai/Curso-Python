print("Impares menores a 10")
x = 1 
while x <= 10: 
    print(x)
    x += 2


factorial = 5
contador = factorial -1 
while contador > 0: 
    factorial *= contador
    contador -= 1 

print("El factorial de 5 es: ", factorial)


suma = 0 
numero = 1
while numero <= 10:
    suma += numero 
    numero += 1

print("La suma del 1 al 10 es: ", suma)


numero_secreto = 7 
intento = 0
intentos = 0 

while intento != numero_secreto: 
    intento = int(input("Adivida el número (1 - 10): "))
    intentos += 1

    if intento < numero_secreto: 
        print("El número secreto es mayor.")
    elif intento > numero_secreto: 
        print("El número secreto es menor.")

        print("¡Correcto!")
        print("Lo lograste en", intentos,"intentos.")
