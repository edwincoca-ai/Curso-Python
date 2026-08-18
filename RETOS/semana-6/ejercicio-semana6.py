# Reto de la semana 6
# Verificación de contraseña

errores = 0

while errores < 3:

    contraseña = input("Ingrese una contraseña: ")

    # Verificamos que la contraseña comience con un número
    if not contraseña[0].isdigit():
        print("La contraseña debe comenzar con un número")
        errores += 1
        continue

    # Pedimos nuevamente la contraseña
    confirmacion = input("Ingrese la contraseña nuevamente: ")

    # Comparamos las dos contraseñas
    if contraseña == confirmacion:
        print("Contraseña correcta")
        break
    else:
        print("Las contraseñas no coinciden")
        errores += 1

if errores == 3:
    print("Has cometido tres errores.")
    
print("Fin del programa")