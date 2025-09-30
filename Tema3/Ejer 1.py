# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.

# Le preguntamos al usuario cual es el número.
valor = int(input("Introduce un número: "))

# Comprobamos que el número sea primo.
if valor % 2 == 0:
    
    # Imprimimos que el valor es par.
    print("El valor es par.")
else:
    # Imprimimos que el valor es impar.
    print("El valor es impar.")