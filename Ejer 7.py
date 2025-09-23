# Realiza un programa que pida un número entero positivo y nos diga si es primo o no.

# Preguntamos el número.
valor1 = int(input("Introduce un número: "))

if valor1 < 2:
    print("No es primo")
else:
    es_primo = True
    for i in range(2, int(valor1 ** 0.5) + 1):
        if valor1 % i == 0:
            es_primo = False
    if es_primo:
        print("Es primo")
    else:
        print("No es primo")


