# ==========================================================
# AGENDA DE CONTACTOS
# Agrega personas a una agenda y las guarda en un archivo
# ==========================================================

ARCHIVO = 'agenda.txt'

MENU = '''
1. Agregar persona a la agenda.
2. Guardar datos en un archivo.
'''


# ==========================================================
# FUNCIONES PARA PEDIR Y VALIDAR CADA DATO
# ==========================================================

def pedir_texto(mensaje, nombre_dato):
    """Pide un texto y repite la pregunta mientras esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == '':
            print(f'No has introducido tu {nombre_dato}')
        else:
            return texto


def pedir_edad():
    """Pide la edad: debe ser un número entero entre 0 y 120."""
    while True:
        try:
            edad = int(input('Introduce tu edad: '))
        except ValueError:
            print('Debes introducir un número')
            continue

        if edad < 0 or edad > 120:
            print('La edad debe estar entre 0 y 120')
            continue

        return edad


def pedir_correo():
    """Pide el correo: debe tener una @ y un punto."""
    while True:
        correo = input('Introduce tu correo: ').strip()
        if '@' in correo and '.' in correo:
            return correo
        print('El correo debe tener una @ y un punto')


def pedir_telefono():
    """Pide el teléfono: debe contener solo números."""
    while True:
        telefono = input('Introduce tu teléfono: ').strip()
        if telefono.isdigit():
            return telefono
        print('Debes introducir solo números')


# ==========================================================
# FUNCIONES DE LA AGENDA
# ==========================================================

def agregar_persona(personas):
    """Pide todos los datos de una persona y la agrega a la lista."""
    nombre = pedir_texto('Ingresa tu nombre: ', 'nombre')
    apellido = pedir_texto('Ingresa tu apellido: ', 'apellido')
    edad = pedir_edad()
    correo = pedir_correo()
    telefono = pedir_telefono()

    # Un diccionario por persona: cada dato se busca por su nombre,
    # no por una posición (así no se pueden confundir)
    persona = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'correo': correo,
        'telefono': telefono,
    }
    personas.append(persona)
    print(f'{nombre} {apellido} se agregó a la agenda.')


def guardar_agenda(personas):
    """
    Guarda las personas en el archivo.
    Devuelve True si se guardó, False si no se pudo.
    """
    # Evita sobrescribir el archivo con uno vacío
    if len(personas) == 0:
        print('Todavía no hay personas. Agrega al menos una (opción 1).')
        return False

    try:
        with open(ARCHIVO, 'w', encoding='utf-8') as archivo:
            for p in personas:
                archivo.write(
                    f"{p['nombre']} {p['apellido']} "
                    f"edad: {p['edad']} "
                    f"telefono: {p['telefono']} "
                    f"correo: {p['correo']}\n"
                )
    except OSError:
        print('Error: no se pudo guardar el archivo.')
        return False

    print(f'Datos guardados en {ARCHIVO}')
    return True


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    personas = []

    while True:
        print(MENU)
        opcion = input('Ingrese una opción: ').strip()

        if opcion == '1':
            agregar_persona(personas)
        elif opcion == '2':
            if guardar_agenda(personas):
                break   # solo termina si realmente se guardó
        else:
            print('Opción inválida')
            print('Volver a intentar')


if __name__ == '__main__':
    main()