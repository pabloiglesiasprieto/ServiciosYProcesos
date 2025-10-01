# Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
# El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. 
# Para ello, cada vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente en el conjunto 2.

# Creamos el diccionario con la correspondencia de los 2 conjuntos.
correspondencia_str = {'e': 'p', 'i': 'v', 'k': 'i', 'm': 'u', 'p': 'm', 'q': 't', 'r': 'e', 's': 'r', 't': 'k', 'u': 'q', 'v': 's'}

# Le preguntamos la frase al usuario.
frase = str(input("Introduce la frase a encriptar: "))

# Creamos una variable string vacia.
fraseCrypted = ""

# Creamos un bucle que recorra la frase.
for letra in frase:
    
    # Vamos comprobando la correspondencia.
    fraseCrypted += correspondencia_str.get(letra, letra) 
    
# Imprimimos la frase encriptada.
print(fraseCrypted)