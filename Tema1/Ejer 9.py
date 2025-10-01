# Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación para cada letra, como en el Scrabble.
# El programa le pedirá una palabra al usuario y se mostrará por pantalla la puntuación que tiene la palabra en total.

# Creamos un diccionario con todas las letras a 0.
diccionario = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,
    "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
    "ñ": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
    "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

# Preguntamos la frase al usuario.
frase = str(input("Introduce una frase: "))

# Quitamos los espacios de la frase.
lista = frase.split(" ")

# Hacemos uso de un bucle anidado para que recorra la lista y a su misma vez recorra las letras de las palabras de la lista.
for palabras in lista:
    
    # Recorremos las letras de la palabra.
    for letras in palabras:
        
        # Incrementamos en 1 el valor de la key.
        diccionario[letras.lower()] += 1

# Imprimimos el diccionario.
print(diccionario)
