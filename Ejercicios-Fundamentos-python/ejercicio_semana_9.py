# Utilizar al menos 2 funciones
# Preguntar cuantos alumnos se registraran en caso de No ingrese una cantidad,
# se asume que se registraran 3 alumnos
# Preguntar el nombre y 2 calificaciones
# Mostrar el nombre en pantalla con inicial en mayuscula y promedio
# Al finalizar el programa se mostrará una lista con el nombre de cada alumno
# y sus calificaciones


def captura_alumnos(numero=3):
    '''
    Registra alumnos y dos calificaciones.
    Recibe como parametro la cantidad de alumnos a registrar.
    Si no se especifica el numero de alumnos, se registraran 3.
    '''

    lista_alumnos = []

    for i in range(numero):
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificación de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))

        lista_alumnos.append([nombre, calificacion1, calificacion2])

        promedio(nombre, calificacion1, calificacion2)

    print('\nLista de alumnos y calificaciones:')
    print(lista_alumnos)


def promedio(nombre, calificacion1, calificacion2):
    '''
    Calcula el promedio de un alumno y lo despliega en pantalla.
    Recibe como parámetros el nombre y dos calificaciones del alumno.
    '''

    promedio = (calificacion1 + calificacion2) / 2

    print(f'El promedio de {nombre} es: {promedio}')


numero_alumnos = input('¿Cuántos alumnos desea registrar? ')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()