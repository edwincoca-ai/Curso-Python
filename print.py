# Ejemplos de la funcion print()

print("hola mundo")
print("hola mundo", "otra vez")
print("son las", 9, "de la mañana")

print("El resultado de 3 * 4 es:", 3*4)

# Ejemplos de cadenas formateadas
print("El numero 15 en sistema decimal el %d, en sistema octal es %o, en el sistema hexadecimal es %x," % (15, 15, 15))

pi = 3.141592
r = 5 
print(f'El radio de un circulo es {r} y el area de ese circulo es {pi * r ** 2 : .2f}')

# Impresion de caracteristicas especiales 
print('La letra beta es: \n\t \u03B2')

# Caracteristicas de escape 
print('hola mundo', end = ' ')
print('otra vez', end = '\t')
print('y otra vez')