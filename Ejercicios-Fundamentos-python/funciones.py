# Función simple

def funcion_simple():
    pass

print("Antes de llamar a la funcion")
funcion_simple()
print("Ya se ha llamado a la funcion")


# Función que saluda al mundo

def saluda():
    print("Hola mundo")

print("Antes de llamar a la funcion")

funcion_simple()   # ← Esta línea vuelve a llamar a la función vacía
saluda()           # ← Esta es la función que quieres probar

print("Ya se ha llamado a la funcion")

help(saluda)
help(funcion_simple)