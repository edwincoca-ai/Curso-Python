# MANEJO DE ERRORES Y EXCEPCIONES EN PYTHON

numerador = 10
denominador = 0
cadena = "3"
numerico = 5

# Ejemplo 1: División entre cero
try:
    print(numerador / denominador)

except ZeroDivisionError:
    print('Ha ocurrido un error: división entre cero')


# Ejemplo 2: Error de tipo
try:
    print(cadena + numerico)

except TypeError:
    print('Ha ocurrido un error de tipo')


print('Fin de los primeros ejemplos')


# Ejemplo 3: Múltiples excepciones
try:
    print(10 / 10)

except TypeError:
    print('Ha ocurrido un error de tipo')

except Exception:
    print('Ha ocurrido un error desconocido')


# -----------------------------------------
# MANEJO DE ERRORES CON EXCEPCIONES Y CICLOS
# -----------------------------------------

while True:

    try:
        dividendo = int(input('Ingrese el dividendo: '))
        divisor = int(input('Ingrese el divisor: '))

        resultado = dividendo / divisor

        print('El resultado es:', resultado)

        break

    except ValueError:
        print('Error: Debe ingresar un número válido.')

    except ZeroDivisionError:
        print('Error: No se puede dividir entre cero.')


print('Fin del programa')