texto_variado = "palabra 123 +-" #%&
print(type(texto_variado))

# podemos utilizar comillas triples para que el texto se muestre 
print('''
funcionamiento de programa: (opciones)
     -1 para acceder a opciones 
          -2 para salir
      ''')

# subscripting e indexado 

texto = "python"

print(texto[0])
print(texto[5])
print(texto[-1])
print(texto[-6])

# print([6]) # error! No podemos acceder a una posicion que no existe 
# print([-7]) # error! No podemos acceder a una posicon que no existe 

letra = texto[0]
print(letra) 

texto_compuesto = letra + texto[1]  #concatenacion 
print(texto_compuesto)

################################################################################################################

# Slicing o Substringing 
texto = "python"

print(texto[0:3])
print(texto[0:-3])
print(texto[0:-2])
print(texto[2:])
print(texto[:3])

print(texto[-3::-1])

print(texto[::-1])
