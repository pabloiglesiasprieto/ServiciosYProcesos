# Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
#    *
#   * *
#  * * *
# * * * *

# Preguntamos la altura.
n = int(input("Introduce la altura de la pirámide: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

