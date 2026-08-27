# ==========================================
# REGISTRO DE CALIFICACIONES - SEMANA 7
# Fundamentos de Python (versión mejorada)
# ==========================================


def pedir_entero(mensaje, minimo=None, maximo=None):
    """Pide un número entero validado, repitiendo hasta que sea correcto."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: debes ingresar un número entero. Intenta de nuevo.")
            continue

        if minimo is not None and valor < minimo:
            print(f"Error: el valor no puede ser menor que {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"Error: el valor no puede ser mayor que {maximo}.")
            continue
        return valor


def pedir_calificaciones():
    """Pide calificaciones (0-10) para un alumno, mínimo 3."""
    calificaciones = []
    while True:
        calificaciones.append(pedir_entero("Ingrese una calificación (0-10): ", 0, 10))

        if len(calificaciones) >= 3:
            respuesta = input("¿Desea agregar otra calificación? (s/n): ").strip().lower()
            if respuesta == "n":
                break
            elif respuesta != "s":
                print("Respuesta no válida. Continuamos agregando calificaciones.")
    return calificaciones


NUM_ALUMNOS = 3  # Cantidad fija de alumnos a registrar


def registrar_alumnos():
    """Registra el nombre y las calificaciones de exactamente NUM_ALUMNOS alumnos."""
    alumnos = {}

    for i in range(NUM_ALUMNOS):
        print(f"\n--- Alumno {i + 1} ---")
        nombre = input("Ingrese el nombre del alumno: ").strip()

        if nombre == "":
            print("No ingresaste un nombre. Se omite este alumno.")
            continue

        alumnos[nombre] = pedir_calificaciones()

    return alumnos


def mostrar_resultados(alumnos):
    """Muestra el registro final con promedio de cada alumno."""
    print("\n==========================================")
    print("       REGISTRO DE CALIFICACIONES")
    print("==========================================")

    if not alumnos:
        print("No se registraron alumnos.")
        return

    for nombre, calificaciones in alumnos.items():
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"\nAlumno: {nombre}")
        print(f"Calificaciones: {calificaciones}")
        print(f"Promedio: {promedio:.2f}")


def main():
    alumnos = registrar_alumnos()
    mostrar_resultados(alumnos)


if __name__ == "__main__":
    main()