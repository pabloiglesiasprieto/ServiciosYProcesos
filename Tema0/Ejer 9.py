# Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos.
# Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.

# Creamos una función que muestre los números entre los números.
def numerosEnMedio(num1, num2):
    
    # Creamos un bucle que imprima los números.
    for valor in range(num1+1,num2):
        print(valor)

# Creamos el método main().
def main():
    
    # Pedimos los valores al usuario.
    valor1 = int(input("Introduce el primer valor: "))
    valor2 = int(input("Introduce el segundo valor: "))
    
    # Pasamos los valores a la función e imprimimos.
    numerosEnMedio(valor1,valor2)

# Llamamos al main.
if __name__ == "__main__":
    main()
