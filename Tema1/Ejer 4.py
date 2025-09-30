# Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.

# Declaramos la lista vacia.
miLista = []

# Creamos un bucle for que se repita 10 veces y por cada vez que itere pregunte un nombre.
for valor in range(10):
    
    # Preguntamos el valor.
    numero = float(input("Introduce un valor: "))
    
    # Añadimos el valor a la lista.
    miLista.append(numero)

# Ordenamos la lista.
miLista.sort()

# Imprimimos la lista.
for valor in miLista:
    print(valor)