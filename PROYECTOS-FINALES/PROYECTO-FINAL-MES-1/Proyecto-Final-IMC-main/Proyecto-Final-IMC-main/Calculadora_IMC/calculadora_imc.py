print("=" * 40)
print("     CALCULADORA DE IMC")
print("=" * 40)

# Nombre
while True:
    nombre = input("Nombre: ").strip()
    if nombre:
        break
    print("Error: El nombre no puede estar vacío.")

# Apellido paterno
while True:
    apellido_p = input("Apellido paterno: ").strip()
    if apellido_p:
        break
    print("Error: El apellido paterno no puede estar vacío.")

# Apellido materno
while True:
    apellido_m = input("Apellido materno: ").strip()
    if apellido_m:
        break
    print("Error: El apellido materno no puede estar vacío.")

# Edad
while True:
    try:
        edad = int(input("Edad: "))
        if edad > 0:
            break
        print("La edad debe ser mayor a 0.")
    except ValueError:
        print("Ingresa una edad válida.")

# Peso
while True:
    try:
        peso = float(input("Peso (kg): "))
        if peso > 0:
            break
        print("El peso debe ser mayor a 0.")
    except ValueError:
        print("Ingresa un peso válido.")

# Estatura
while True:
    try:
        estatura = float(input("Estatura (m): "))
        if estatura > 0:
            break
        print("La estatura debe ser mayor a 0.")
    except ValueError:
        print("Ingresa una estatura válida.")

# Calcular IMC
imc = peso / (estatura ** 2)

# Clasificación
if imc < 16:
    clasificacion = "Delgadez severa"
elif imc < 17:
    clasificacion = "Delgadez moderada"
elif imc < 18.5:
    clasificacion = "Delgadez leve"
elif imc < 25:
    clasificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
elif imc < 35:
    clasificacion = "Obesidad grado I"
elif imc < 40:
    clasificacion = "Obesidad grado II"
else:
    clasificacion = "Obesidad grado III"

print("\n" + "=" * 40)
print("RESULTADOS")
print("=" * 40)

print(f"Nombre completo: {nombre} {apellido_p} {apellido_m}")
print(f"Edad: {edad} años")
print(f"Peso: {peso:.2f} kg")
print(f"Estatura: {estatura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Clasificación: {clasificacion}")

print("\nGracias por utilizar la Calculadora de IMC.")