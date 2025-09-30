'''Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10
.Luego pedirá un valor N y mostrará cuántas veces aparece N. '''
# Importamos el Random
import random

# Declaramos la lista vacía.
lista = []

# Creamos un bucle que itere 100 veces y que genere números aleatorios.
for valor in range(100):
    
    # Generamos el valor aleatorio y lo metemos a la lista.
    lista.append(random.randint(1,11))
    
# Preguntamos el valor al usuario.
numero = int(input("Escribe un número: "))

# Comprobamos la cantidad de números en la lista.
print(lista.count(numero))    


