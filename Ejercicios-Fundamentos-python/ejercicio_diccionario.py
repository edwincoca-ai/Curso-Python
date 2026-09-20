emoji_diccionario = {"feliz": "🙂", "amo": "😍", "risa": "🤣", "sonrisa": "😊", "llorar": "😭", "beso": "😘", \
    "aplauso": "👏", "reir": "😁", "fuego": "🔥", "roto": "💔", "pensando": "🤔", \
    "maravillado": "🤩", "aburrido": "😐", "guiño": "😉", "ok": "👌", "abrazo": "🤗", \
    "cool": "😎", "enojado": "😠", "python": "🐍"}

frase = input("Escribe una frase: ")

frase = frase.lower()

palabras = frase.split()

print(palabras)

respuesta = " "

for palabra in palabras:

    if palabra in emoji_diccionario:
        respuesta = respuesta + emoji_diccionario[palabra] + " "

    else:
        respuesta = respuesta + palabra + " "

print(respuesta)     