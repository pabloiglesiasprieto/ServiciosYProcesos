# Crea un programa que pida diez números reales por teclado, los almacene en una lista, y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

# Declaramos la lista.
listaNumerosReales = []

# Creamos un bucle que es recorra 10 veces.
for valor in range(10):
    
    # Preguntamos el valor.
    valor = float(input("Introduce un valor: "))
    
    # Añadimos el valor a la lista.
    listaNumerosReales.append(valor)
    
# Declaramos 2 variables para almacenar el máximo y el mínimo.
minimo = min(listaNumerosReales)
maximo = max(listaNumerosReales)

# Imprimimos el máximo y el mínimo.
print("El mínimo es de",minimo," el máximo es de",maximo)
    
    

    
    
    

