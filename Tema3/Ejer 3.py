'''Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.
'''
# Inicializamos la variable suma a 0
suma = 0

# Le preguntamos al usuario un número 
valor1 = int(input("Introduce un valor: "))

# Sumamos el valor
suma += valor1

# Creamos un bucle
while valor1 >= 0:
    
    # Le preguntamos al usuario un número 
    valor1 = int(input("Introduce un valor: "))
    
    # Sumamos el valor
    suma += valor1

# Imprimimos el resultado de la suma.
print("La cantidad de la suma es de", suma)  