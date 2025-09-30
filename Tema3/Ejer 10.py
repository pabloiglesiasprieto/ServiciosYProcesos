# Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.

# Creamos la función que recibe los 2 valores y devuelve el más grande.
def maxNumber(numero1,numero2):
    
    # Calculamos el mayor.
    maximo = numero1 if numero1>numero2 else numero2
    
    # Devolvemos el máximo.
    return maximo

def main():
    
    # Preguntamos los números.
    valor1 = int(input("Introduce el primer valor: "))
    valor2 = int(input("Introduce el segundo valor: "))
    
    # Llamamos a la función.
    maximo = maxNumber(valor1,valor2)
    
    # Imprimimos el máximo.
    print("El máximo es el", maximo)

# Llamamos al main.
if __name__ == "__main__":
    
    # Llamamos a la función.
    main()
    