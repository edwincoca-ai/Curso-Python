#### Reto de la semana - 5 ####
#### Programa para calcular años transcurridos o faltantes #####
#### Autor: Edwin Antonio Coca Navarro ####

año_actual = int(input("Introduce el año actual: "))
otro_año = int(input("Introduce otro año para calcular: "))

if año_actual == otro_año:
    print("Has introducido el mismo año que el actual")

elif otro_año < año_actual:
    diferencia = año_actual - otro_año
    if diferencia == 1:
        print(f"Desde el año {otro_año} ha pasado 1 año")
    else: 
        print(f"Han pasado {diferencia} años desde el año que has introducido") 
else:
    diferencia = otro_año - año_actual 
    print(f"Faltan {diferencia} años para llegar al año que has introducido")       
