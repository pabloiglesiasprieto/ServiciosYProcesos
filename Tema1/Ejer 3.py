''' Realiza un programa que pida 8 números enteros y los almacene en una lista.
 A continuación, recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda.'''
 
# Declaramos la lista vacia.
miLista = []

# Creamos un bucle que se recorra 8 veces.
for valor in range(10):
   
     # Preguntamos el valor.
     valor = float(input("Introduce el valor: "))
     
     # Añadimos el valor a la lista.
     miLista.append(valor)

# Recorremos el bucle y comprobamos que sea impar o par el valor.
for valor in miLista:
    
    # Comprobamos que el valor sea par.
    if valor % 2 == 0:
        
        # Imprimimos que es par.
        print(valor, "es par.")
    
    # Si no se cumple la condición.
    else:
        
        # Imprimimos que el valor es impar.
        print(valor, "es impar.")
        
     
