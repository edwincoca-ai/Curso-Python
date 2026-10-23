
# ==========================================================
# RETO SEMANA 14 - FUNDAMENTOS DE PYTHON
# UCAMP - MODIFICAR CONTACTOS
# Autor: Edwin Antonio Coca Navarro
# ==========================================================

from pathlib import Path
import os
import tempfile

# Archivo de contactos en la misma carpeta del programa
ARCHIVO = Path(__file__).resolve().parent / "contactos.txt"

CAMPOS = {
    1: "nombre",
    2: "telefono",
    3: "correo"
}

ETIQUETAS = {
    "nombre": "nombre",
    "telefono": "teléfono",
    "correo": "correo"
}


# ==========================================================
# FUNCIÓN PARA LEER CONTACTOS
# ==========================================================

def leer_contactos():
    contactos = []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if linea == "":
                    continue

                partes = linea.split(",")

                if len(partes) != 3:
                    print("Error: formato incorrecto en contactos.txt.")
                    print("Formato esperado: nombre,telefono,correo")
                    print("No se modificará el archivo.")
                    return None

                contactos.append({
                    "nombre": partes[0].strip(),
                    "telefono": partes[1].strip(),
                    "correo": partes[2].strip()
                })

    except FileNotFoundError:
        print("Error: no se encontró contactos.txt.")
        return None

    except (OSError, UnicodeError):
        print("Error: no se pudo leer el archivo.")
        return None

    return contactos


# ==========================================================
# FUNCIÓN PARA GUARDAR CONTACTOS
# ==========================================================

def guardar_contactos(contactos):
    temporal = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=ARCHIVO.parent,
            prefix="contactos_",
            suffix=".tmp",
            delete=False
        ) as archivo:

            temporal = Path(archivo.name)

            for contacto in contactos:
                archivo.write(
                    f"{contacto['nombre']},"
                    f"{contacto['telefono']},"
                    f"{contacto['correo']}\n"
                )

        os.replace(temporal, ARCHIVO)
        return True

    except OSError:
        print("Error: no se pudo guardar el archivo.")
        return False

    finally:
        if temporal is not None:
            try:
                temporal.unlink(missing_ok=True)
            except OSError:
                pass


# ==========================================================
# FUNCIÓN PARA MOSTRAR CONTACTOS
# ==========================================================

def mostrar_contactos(contactos):
    print("\n========================================")
    print("          CONTACTOS GUARDADOS")
    print("========================================")

    for numero, contacto in enumerate(contactos, start=1):
        print(f"\n{numero}. {contacto['nombre']}")
        print(f"   Teléfono: {contacto['telefono']}")
        print(f"   Correo:   {contacto['correo']}")


# ==========================================================
# FUNCIÓN PARA VALIDAR NÚMEROS
# ==========================================================

def pedir_entero(mensaje, minimo, maximo):

    while True:
        try:
            numero = int(input(mensaje))

            if minimo <= numero <= maximo:
                return numero

            print(f"Error: elige entre {minimo} y {maximo}.")

        except ValueError:
            print("Error: introduce un número entero.")


# ==========================================================
# FUNCIÓN PARA ELEGIR QUÉ MODIFICAR
# ==========================================================

def elegir_campo():
    print("\n¿Qué dato deseas modificar?")
    print("1. Nombre")
    print("2. Teléfono")
    print("3. Correo")
    print("0. Volver")

    opcion = pedir_entero("Elige una opción: ", 0, 3)

    if opcion == 0:
        return None

    return CAMPOS[opcion]


# ==========================================================
# FUNCIÓN PARA VALIDAR DATOS
# ==========================================================

def validar_valor(campo, valor):

    if valor == "":
        return "El dato no puede estar vacío."

    if "," in valor or "\n" in valor:
        return "No utilices comas ni saltos de línea."

    if campo == "telefono":
        if not valor.isascii() or not valor.isdigit():
            return "El teléfono debe contener solo números."

        if len(valor) != 10:
            return "El teléfono debe tener 10 dígitos."

    if campo == "correo":
        if valor.count("@") != 1:
            return "El correo debe contener una sola @."

        usuario, dominio = valor.split("@")

        if (
            usuario == ""
            or "." not in dominio
            or dominio.startswith(".")
            or dominio.endswith(".")
            or " " in valor
        ):
            return "Introduce un correo válido."

    return None


# ==========================================================
# FUNCIÓN PARA SOLICITAR UN NUEVO VALOR
# ==========================================================

def pedir_nuevo_valor(campo):

    while True:
        valor = input(
            f"Introduce el nuevo {ETIQUETAS[campo]}: "
        ).strip()

        error = validar_valor(campo, valor)

        if error is None:
            return valor

        print(f"Error: {error}")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    print("========================================")
    print("    RETO SEMANA 14 - MODIFICAR CONTACTOS")
    print("========================================")

    contactos = leer_contactos()

    if contactos is None:
        return

    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return

    while True:

        mostrar_contactos(contactos)

        numero = pedir_entero(
            "\nSelecciona un contacto (0 para salir): ",
            0,
            len(contactos)
        )

        if numero == 0:
            print("Programa terminado. ¡Hasta pronto!")
            break

        contacto = contactos[numero - 1]

        campo = elegir_campo()

        if campo is None:
            continue

        valor_anterior = contacto[campo]
        nuevo_valor = pedir_nuevo_valor(campo)

        contacto[campo] = nuevo_valor

        if guardar_contactos(contactos):
            print("\nContacto actualizado correctamente.")

        else:
            contacto[campo] = valor_anterior
            print("No se guardaron los cambios.")


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()
