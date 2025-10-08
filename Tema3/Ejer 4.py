class Articulo:
    
    IVA = 21.00
    
    def __init__(self,nombre,precio,cuantosQuedan):
        
        self.nombre = nombre
        self.precio = float(precio)
        self.cuantosQuedan = cuantosQuedan
    
    def getPVP(self):
        return self.precio + (self.precio * Articulo.IVA)
    
    def getPVPDescuento(self, descuento):
        pvp = self.getPVP()
        return pvp - (pvp * descuento)
    
    def vender(self, cantidad):
        if self.cuantosQuedan - cantidad <= 0:
            return False
        else:
            self.cuantosQuedan -= cantidad
            return True
        
    def almacenar(self, cantidad):
        self.cuantosQuedan += cantidad
        
    def __str__(self):
        return f'{self.nombre}, {self.precio}, {self.cuantosQuedan}'
    
    def __eq__(self, other):
        return self.nombre == other.nombre
    
    def __lt__(self, other):
        return self.nombre > other.nombre
    
def main():
    # Crear un artículo
    articulo1 = Articulo("Teclado", 50.0, 10)
    
    # Mostrar artículo
    print("Artículo:", articulo1)

    # Mostrar PVP
    print("PVP:", articulo1.getPVP())

    # Mostrar PVP con descuento del 10%
    print("PVP con 10% de descuento:", articulo1.getPVPDescuento(10))

    # Intentar vender 5 unidades
    if articulo1.vender(5):
        print("Venta realizada con éxito.")
    else:
        print("No hay suficientes unidades para la venta.")

    print("Stock tras venta:", articulo1.cuantosQuedan)

    # Intentar vender más de lo disponible
    if articulo1.vender(6):
        print("Venta realizada con éxito.")
    else:
        print("No hay suficientes unidades para la venta.")

    # Almacenar unidades
    articulo1.almacenar(20)
    print("Stock tras almacenamiento:", articulo1.cuantosQuedan)

    # Comparación con otro artículo
    articulo2 = Articulo("Auriculares", 30.0, 5)
    print("Artículo 1 == Artículo 2?", articulo1 == articulo2)

    # Ordenar lista de artículos
    articulos = [articulo1, articulo2]
    articulos.sort()
    print("Artículos ordenados por nombre:")
    for art in articulos:
        print(art)

if __name__ == "__main__":
    main()

        