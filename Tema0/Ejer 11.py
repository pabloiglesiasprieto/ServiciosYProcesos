# Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.

# Creamos la función para comprobar que sea una vocal.
def isAVowel(char):
    
    # Creamos una lista con las posibles vocales.
    vocales = ["a","e","i","o","u"]
    
    # Comprobamos que la letra está en la lista.
    return vocales.__contains__(char)

# Creamos un main.
def main():
    
    # Preguntamos la letra.
    letra = str(input("Introduce una letra: "))
    
    # Llamamos a la función.
    if isAVowel(letra):
        
        # Si es true, imprimimos que es una vocal.
        print("Es una vocal.")
    
    # Si no se cumple el condicional.
    else:
        
        # Si es false, imprimimos que no es una vocal.
        print("No es una vocal.")
        
# Ejecutamos el main.
if __name__ == "__main__":
        
    main()