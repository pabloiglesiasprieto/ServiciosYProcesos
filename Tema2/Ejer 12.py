
# Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. 
# Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. 
# La función devolverá el resultado de la operación mediante un número real.


# Función para sumar dos números
def sumar(number1, number2):
    return number1 + number2


# Función para restar dos números
def restar(number1, number2):
    return number1 - number2


# Función para multiplicar dos números
def multiplicar(number1, number2):
    return number1 * number2


# Función para dividir dos números
def dividir(number1, number2):
    return number1 / number2
    

# Función calculadora que elige la operación según el número introducido
def calculadora(number1, number2, operation):
    if operation == 1: 
        return sumar(number1, number2)         # Suma
    elif operation == 2:
        return restar(number1, number2)        # Resta
    elif operation == 3:
        return multiplicar(number1, number2)   # Multiplicación
    elif operation == 4:
        return dividir(number1, number2)       # División


# Función principal que pide los datos al usuario y muestra el resultado
def main():
    number1 = int(input("Introduce el primer número: "))      # Pide el primer número
    number2 = int(input("Introduce el segundo número: "))     # Pide el segundo número
    operation = int(input("Introduce la operación: "))        # Pide la operación (1, 2, 3 o 4)
    resultado = calculadora(number1, number2, operation)        # Llama a la calculadora
    print("El resultado es", resultado)                        # Muestra el resultado


# Hace que el programa se ejecute solo si es el archivo principal
if __name__ == "__main__":
    main()

    
    
