# Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

# Importamos Random.
import random

# Declaramos la variable que almacenará la lista.
miLista = []

# Creamos un bucle for que se repita 10 veces y por cada vez que itere se genere un número aleatorio.
for valor in range(10):
    miLista.append(random.randint(1,101))

# Imprimimos la lista.
for valor in miLista:
    print(valor)
    