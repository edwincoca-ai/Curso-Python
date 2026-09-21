def sumar(parametro1, parametro2):
    '''Funcion que suma dos parametros y los imprime en pantalla'''
    print('suma:', parametro1 + parametro2)


argumento1 = 5
argumento2 = 7

# Invocando a la funcion por medio de parametros, variables.

sumar(argumento1, argumento2)

# Invocando a la funcion por medio de parametros de valor.

sumar('Mundo ', 'Hola')
sumar('Hola ', 'Mundo')


#########################################################

# Parametros Operacionales.

def muestra_alumno(nombre, edad=18, sexo='F'):
    '''
    Es una función que muestra en pantalla el nombre, la edad, y el sexo del alumno.
    Recibe tres parámetros.
    1.- Nombre
    2.- Edad = 18
    3.- Sexo = 'F'
    '''
    print(f'nombre: {nombre}, edad: {edad}, sexo: {sexo}')


# Ejecución utilizando el parametro obligatorio
muestra_alumno('maria')

# Ejecución utilizando el parametro obligatorio y uno opcional
muestra_alumno('maria', 22)

# Ejecución de funcion con el primer y ultimo parametro
muestra_alumno('juan', sexo='m')