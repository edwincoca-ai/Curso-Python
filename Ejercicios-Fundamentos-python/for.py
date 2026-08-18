for i in 1, 2, 3: 
    print(i)

for i in range(5): 
    print(i)


for i in ["Ale", "Ivan", "Monse", "Luis", "Rafa", "Luca",]:
    print(i)


for i in "Hola mundo" :
    if i == "m":
        pass
    else:
        print(i, end=" ") 

print("\n--- Contador de vocales---")

palabra = "inteligencia"
vocales = 0

for letra in palabra: 
    if letra in "aeiou": 
        vocales += 1

print("La palabra es: ", palabra)
print("Tiene", vocales, "vocales.")
