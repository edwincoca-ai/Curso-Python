# Proyecto Final - Calculadora de IMC

## Autor

Edwin Antonio Coca Navarro

## Descripción

Este proyecto consiste en desarrollar una Calculadora de Índice de Masa Corporal (IMC) utilizando Python.

El programa solicita al usuario los siguientes datos:

- Nombre
- Apellido paterno
- Apellido materno
- Edad
- Peso en kilogramos
- Estatura en metros

Posteriormente valida que los datos sean correctos, calcula el IMC y muestra la clasificación correspondiente.

## Validaciones implementadas

El programa valida que:

- El nombre no esté vacío.
- Los apellidos no estén vacíos.
- La edad sea un número mayor que cero.
- El peso sea mayor que cero.
- La estatura sea mayor que cero.
- Si el usuario introduce letras donde se esperan números, el programa muestra un mensaje de error y solicita nuevamente el dato.

## Fórmula utilizada

IMC = Peso / (Estatura²)

## Clasificación del IMC

- Delgadez severa
- Delgadez moderada
- Delgadez leve
- Peso normal
- Sobrepeso
- Obesidad grado I
- Obesidad grado II
- Obesidad grado III

## Reflexión del Bootcamp

Durante este bootcamp aprendí los fundamentos de Python y comprendí la importancia de escribir código de manera ordenada y estructurada.

Con este proyecto reforcé el uso de:

- Variables
- Entrada y salida de datos
- Condicionales (if, elif y else)
- Ciclos while
- Manejo de errores con try y except
- Validación de datos
- Operadores aritméticos
- Cálculo del Índice de Masa Corporal (IMC)

También aprendí que la indentación en Python es fundamental para el correcto funcionamiento de los programas y que resolver errores forma parte del proceso de aprendizaje.

Este proyecto representa mi primer programa completo desarrollado en Python.

## Cómo ejecutar el programa

1. Abrir la terminal.
2. Entrar a la carpeta del proyecto.
3. Ejecutar:

bash
python calculadora_imc.py


4. Capturar los datos solicitados por el programa.