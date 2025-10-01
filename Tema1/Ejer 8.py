# Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son los nombres de los productos y los valores son las cantidades vendidas. 
# El programa debe permitir al usuario agregar nuevas ventas y calcular el total de ventas para un producto específico. Implementa un menú con ambas opciones. 

# Creamos una función que imprima las opciones disponibles.
def opciones():
    
    # Imprimimos las opciones.
    print('''=====================================
           ELIGE UNA OPCIÓN
=====================================
1. Agregar.
2. Calcular total.
0. Salir''')

# Creamos una función para agregar una nueva venta.
def agregarProducto (nombre,ventas):
    
     # Comprobamos que el producto no exista en el diccionario.
     if nombre in diccionario:
         
         # Imprimimos que el producto ya existe.
         print("El producto ya existe.")
         
     # Si no se cumple.
     else:
         
         # Añadimos el producto al diccionario.
         diccionario[nombre] = ventas
         
         # Imprimimos que se ha añadido.
         print("El producto se ha añadido correctamente.")

# Creamos una función que calcule todas las ventas.
def sumarVentas():
    
    # Inicializamos la suma a 0.
    suma = 0
            
    # Recorremos la lista y sumamos todas las ventas.
    for valor in diccionario:
            
            # Sumamos todos los valores.
            suma += diccionario[valor]
    
    # Devolvemos la suma.
    return suma        


# Creamos un diccionario vacío.
diccionario = {}

# Imprimimos las opciones.
opciones()

# Preguntamos que acción quiere realizar.
eleccion = int(input("Que acción quieres realizar: "))

# Creamos un bucle que se repita hasta que el usuario escriba 0.
while eleccion != 0:
    
    # Si la eleccion es la primera.
    if eleccion == 1:
        
        # Preguntamos el nombre y las ventas.
        nombre = str(input("Introduce el nombre del producto: "))
        ventas = int(input("Introduce las ventas del producto: "))
        
        # Llamamos a la función.
        agregarProducto(nombre,ventas)
        
    # Si la eleccion es la segunda.
    if eleccion == 2:
        
        # Calculamos las ventas.
        suma = sumarVentas()
        
        # Imprimimos las ventas totales.
        print("El total de ventas es de", suma)
        
    # Imprimimos las opciones.
    opciones()

    # Preguntamos que acción quiere realizar.
    eleccion = int(input("Que acción quieres realizar: "))

    
# Imprimimos que salió del programa.
print("Saliste del programa.")
        


