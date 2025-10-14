class Libro:

    def __init__(self, titulo, autor, ejemplares, ejemplaresPrestados):

        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.ejemplaresPrestados = ejemplaresPrestados

    def prestamo(self):

        if self.ejemplares <= 0:
            prestado = False
        else:
            self.ejemplaresPrestados += 1
            self.ejemplares -= 1
            prestado = True
        return prestado

    def devolucion(self):

        if self.ejemplaresPrestados <= 0:
            devolvido = False
        else:
            self.ejemplares += 1
            self.ejemplaresPrestados -= 1
            devolvido = True
        return devolvido

    def __str__(self):
        return (
            self.titulo + 
            " - " + 
            self.autor + 
            " - Unidades Prestadas:" +
            str(self.ejemplaresPrestados) +
            " - Existencias:" + 
            str(self.ejemplares)
        )

    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor

    def __lt__(self, other):
        return self.autor > other.autor


class main:
    obj = Libro("Como ser un femboy", "Julian Lorente Marroco", 20, 2)
    obj2 = Libro("Como cazar a un femboy", "Julian Lorente Marroco", 20, 2)
    obj3 = Libro("Como cazar a un femboy", "Julian Lorente Marroco", 1, 9)
    
    print(obj)

    print(obj.__eq__(obj2))
    print(obj2.__eq__(obj3))

    print(obj3.prestamo())
    print(obj3.prestamo())


if __name__ == "__main__":
    main()
