# Ejercicio 6
# Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.

# Preguntamos el número.
valor1 = int(input("Introduce un número: "))

# Inicializamos el factorial a 1.
factorial = 1

# Creamos un bucle.
for valor in range(valor1, 1,-1):
    
    # Calculamos el factorial.
    factorial*=valor
    
#Imprimimos el factorial
print("El factorial es de",factorial)
    