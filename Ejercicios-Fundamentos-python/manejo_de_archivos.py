f_archivo = open ('archivo1.txt', 'w') # W = write (escribe) escribir en el archivo sobre escribir el archivo.  
print(f_archivo)
f_archivo.close()

f_archivo = open('archivo1.txt', 'w')
print(f_archivo)
f_archivo.write('Hola mundo!')
f_archivo.close()

f_archivo = open('archivo1.txt')

f_archivo = open ('archivo1.text', 'w')
f_archivo.write ('Este es mi primer archivo')
f_archivo.close()

f_lectura = open('archivo1.txt', 'r') # r = read (leer) leer el archivo
print(f_lectura.read())
f_lectura.close()

print(f_archivo)
print(f_lectura)

# Sentancia with y as 

f_lectura = open('archivo1.txt', 'r')
print(f_lectura.close)
f_lectura.close()
print(f_lectura.close)

with open ('archivo1.txt', 'r') as f_lectura:
     print(f_lectura.close)
print(f_lectura.close)

with open ('archivo1.txt', 'a') as f_archivo: # a = append (agregar) agregar el archivo
 f_archivo.write('\n Este es mi primer archivo 2')
 f_archivo.write('\n Este es mi primer archivo 3')
 f_archivo.write('\n')
 f_archivo.write('\n Este es mi primer archivo 4')

with open('archivo1.txt', 'r') as f_lectura: 
   # print(f_lectura.read())
   contenido = f_lectura.read()
   print(f'*** (contenido)***')
   contenido = f_lectura.read()
   print(f'***(contenido)***')

###############################################################

# Lectura de archivo linea a linea

with open ('archivo1.txt', 'r') as f_lectura:
   numero_de_lineas = 0
   for i in f_lectura:
      numero_de_lineas += 1
      print(f'linea (numero_de_lineas): {i}')
print(f'El archivo tiene {numero_de_lineas} lineas') 

# Creando una lista apartir de un archivo 

with open ('archivo1.txt', 'r') as f_lectura: 
   lista_archivo = f_archivo.readlines()
   print(lista_archivo)

# Print (lista_archivo)

lista_archivo[1] = 'Este es mi primer archivo 2\n' 
lista_archivo.insert(2, 'Este es mi primer archivo 3\n')

print(lista_archivo)

with open('archivo1.txt', 'w') as f_archivo: 
   f_archivo.writelines(lista_archivo)

   
