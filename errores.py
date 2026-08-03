numHuevos = 12 

# Opcion 1 
print('Tengo' + str(numHuevos) + 'Huevos')

# Opcion 2 
print('Tengo %s huevos.' %(numHuevos))

# error tipo logica. 
# Calcular la superficie o area de un cuadrado

lado = int(input("Ingrese la medida del lado del cuadrado: "))
superficie = lado * lado * lado  # El mal planteamiento de la formula ya seria de tipo logica. 
print("La superficie del cuadrado es: " + str(superficie))