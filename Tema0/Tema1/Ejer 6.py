# Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.

# Preguntamos el texto.
cadena = str(input("Introduce la frase: "))

# Guardamos las palabras en una lista.
palabras = cadena.split(" ")
 
# Creamos un diccionario vacío.
diccionario = {}

# Recorremos la lista.
for palabra in palabras:
    
    # Comprobamos si la palabra existe en el diccionario.
    if palabra in diccionario:
        
        # Si existe, incrementamos su valor en 1.
        diccionario[palabra] += 1
    
    # Si no se cumple la condición.
    else:
        
		# Si no existe, le damos el valor de 1.
        diccionario[palabra] = 1

# Imprimimos el diccionario.
print(diccionario)