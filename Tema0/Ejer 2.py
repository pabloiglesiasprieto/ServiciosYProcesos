# Pedir dos números y mostrarlos ordenados de menor a mayor.

# Le preguntamos al usuario los 2 números.
valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))

# Comprobamos cual valor es más grande.
if valor1 > valor2:
    print(valor1, valor2)
elif valor2 > valor1:
    print(valor2,valor1)
else:
    print("Son iguales.")