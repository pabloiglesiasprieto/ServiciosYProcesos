# Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. 
# La clave del diccionario será el nombre del contacto y el valor, su número de teléfono.
# Crea un menú para las distintas opciones e implementa una función para cada opción.

# Creamos una función para imprimir las acciones disponibles.
def opciones():
    
    # Imprimimos las cadenas.
    print('''
=====================================
           ELIGE UNA OPCIÓN
=====================================
1. Agregar.
2. Eliminar.
3. Buscar contactos.
0. Salir
          '''       
    )
    
# Creamos una función para agregar la persona en el diccionario.
def agregarContacto(nombreContacto:str, telefono:str):
    
    # Comprobamos que el valor existe en la agenda.
    if nombreContacto in diccionario:
        
        # Si el contacto existe, imprimimos que ya existe.
        print("El contacto ya existe.")
    
    # Si no se cumple el condicional.
    else:
        
        # Añadimos el contacto a la agenda.
        diccionario[nombreContacto] = telefono
        
        # Imprimimos que el contacto se ha agregado correctamente.
        print("Contacto agregado correctamente.")
        
    
# Creamos una función para borrar una persona del diccionario.
def borrarContacto(nombreContacto:str):

    # Comprobamos que el valor se encuentre en el diccionario.
    if nombreContacto in diccionario:
        
        # Borramos el contacto de la lista.
        diccionario.pop(nombreContacto)
        
        # Imprimimos que el valor se ha borrado correctamente.
        print("El contacto se ha borrado correctamente.")
        
    # Si no es encuentra.
    else:
        
        # Imprimimos que el contacto no existe en el diccionario.
        print("El valor no existe en el diccionario.")
    
    
# Creamos una función que busca la información de un contacto.
def buscarContacto (nombreContacto:str):
    
    # Comprobamos que la llave se encuentre en el diccionario.
    if nombreContacto in diccionario:
          
        # Recogemos el telefono. 
        telefono = diccionario.get(nombreContacto)
        
        # Imprimimos el telefono del contacto
        print("El telefono de",nombreContacto, "es",telefono)
    
    # Si no se cumple el condicional.
    else:
        
        # Imprimimos que el valor no existe.
        print("El contacto no existe.")
    
        
# Creamos un diccionario vacío.
diccionario = {}

# Le preguntamos al usuario que acción quiere realizar.
opciones()

# Guardamos en una variable la elección del usuario.
eleccion = int(input("Introduce la opción: "))


# Hacemos un bucle que se repita hasta que el usuario elija 0.
while eleccion != 0:

    # Comprobamos la elección del usuario.
    if eleccion == 1:
        
            # Preguntamos el nombre y el telefono.
            nombreContacto = str(input("Introduce el nombre del contacto: "))
            telefono = str(input("Introduce el telefono del contacto: "))
            
            # Llamamos a la función que añade la persona al diccionario.
            agregarContacto(nombreContacto,telefono)

    # Si la opción es la 2.
    elif eleccion == 2:
        
        # Preguntamos el nombre del contacto.
        nombreContacto = str(input("Introduce el nombre del contacto: "))
        
        # Llamamos a la función de borrar el contacto.
        borrarContacto(nombreContacto)
        
    # Si la opción es la 3.
    elif eleccion == 3:
        
        # Preguntamos el contacto.
        nombreContacto = str(input("Introduce el nombre del contacto: "))
        
        # Llamamos a la función que busca el contacto.
        buscarContacto(nombreContacto)
        
    # Le preguntamos al usuario que acción quiere realizar.
    opciones()

    # Guardamos en una variable la elección del usuario.
    eleccion = int(input("Introduce la opción: "))
    
    
# Imprimimos la salida del programa.
print("Saliste del programa correctamente.")