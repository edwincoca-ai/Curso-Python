
# RETO SEMANA 13 - UCAMP
# Registro de alumnos y calificaciones
# Autor: Edwin Antonio Coca Navarro

alumnos = []

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar un nuevo alumno")
    print("2. Ver alumnos y calificaciones")
    print("S. Salir")

    opcion = input("Selecciona una opción: ").strip().upper()

    if opcion == "1":

        # Validar nombre
        while True:
            nombre = input("Introduce el nombre del alumno: ").strip()

            if nombre == "":
                print("Error: No has introducido un nombre.")
            else:
                break

        # Validar cantidad de calificaciones
        while True:
            try:
                cantidad = int(input("¿Cuántas calificaciones deseas agregar?: "))

                if cantidad <= 0:
                    print("Error: Debes agregar al menos una calificación.")
                else:
                    break

            except ValueError:
                print("Error: Debes introducir un número entero.")

        # Registrar calificaciones
        calificaciones = []

        for i in range(cantidad):
            while True:
                try:
                    calificacion = float(
                        input(f"Introduce la calificación {i + 1}: ")
                    )

                    if 0 <= calificacion <= 10:
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("Error: La calificación debe estar entre 0 y 10.")

                except ValueError:
                    print("Error: Debes introducir un número válido.")

        # Guardar alumno
        alumnos.append({
            "nombre": nombre,
            "calificaciones": calificaciones
        })

        print("Alumno registrado correctamente.")

    elif opcion == "2":

        if len(alumnos) == 0:
            print("Todavía no hay alumnos registrados.")

        else:
            print("\n--- ALUMNOS REGISTRADOS ---")

            for alumno in alumnos:
                promedio = (
                    sum(alumno["calificaciones"])
                    / len(alumno["calificaciones"])
                )

                print(f"\nAlumno: {alumno['nombre']}")
                print(f"Calificaciones: {alumno['calificaciones']}")
                print(f"Promedio: {promedio:.2f}")

    elif opcion == "S":

        while True:
            confirmar = input(
                "¿Estás seguro de cerrar el programa? (S/N): "
            ).strip().upper()

            if confirmar == "S":
                print("Cerrando el programa. ¡Hasta pronto!")
                break

            elif confirmar == "N":
                print("Regresando al menú principal.")
                break

            else:
                print("Error: Responde S o N.")

        if confirmar == "S":
            break

    else:
        print("Opción no válida. Inténtalo nuevamente.")
