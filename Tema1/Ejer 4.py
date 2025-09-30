'''Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor o menor con respecto al número secreto. 
El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).'''

# Importamos el random.
import random as rnd

# Generamos el número aleatorio.
valorAleatorio = rnd.randrange(1,101)

# Preguntamos el valor.
valorUsuario = int(input("Introduce un valor: "))

# Creamos un bucle hasta que el usuario acierte el número.
while valorUsuario != valorAleatorio and valorUsuario != -1:
    
    # Si el número del usuario es mayor, imprimimos mayor.
    if valorUsuario > valorAleatorio:
        print("Menor")
        
    # Si el número del usuario es menor, imprimimos menor.
    elif valorUsuario < valorAleatorio:
        print("Mayor") 
        
    # Preguntamos el valor.
    valorUsuario = int(input("Introduce un valor: "))

# Comprobamos que el usuario ha escrito -1.
if valorUsuario == -1:
    
    # Imprimimos que falló.
    print("Fallaste")
    
# Si no se cumple la condición.
else:
    
# Imprimimos que acertó el usuario.
    print("Acertaste.")

