# Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.

# Preguntamos el número.
valor1 = int(input("Introduce un número: "))

# Creamos un bucle desde 1 hasta el valor dado.
for valor in range(1,valor1 + 1):
    
    # Imprimimos el valor.
    print(valor)