# Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.

def limpiar_palabra(palabra):
	"""Elimina signos de puntuación básicos de los extremos y pasa a minúsculas."""
	signos = ".,;:!?\"'()[]{}"
	return palabra.strip(signos).lower()

def main():
	texto = input("Introduce un texto: ")
	palabras = texto.split()
	frecuencias = {}
	for palabra in palabras:
		limpia = limpiar_palabra(palabra)
		if limpia:
			if limpia in frecuencias:
				frecuencias[limpia] += 1
			else:
				frecuencias[limpia] = 1
	print("Diccionario de frecuencias:")
	print(frecuencias)

if __name__ == "__main__":
	main()

