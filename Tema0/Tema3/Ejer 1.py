class CuentaCorriente:
    def __init__(self, dni, saldo, nombre = ""):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo
        
    def sacarDinero(self,cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            
    def ingresarDinero(self,cantidad):
        self.saldo += cantidad
            
    def __str__(self):
        return "Nombre: " + self.nombre + " DNI: " + str(self.dni) + " Saldo: " + str(self.saldo)
    
    def __eq__(self, other):
        return self.dni == other.dni   
    
    def __lt__(self, other):
        return self.saldo > other.saldo


class Prueba: 
    
    def main():
        obj = CuentaCorriente("11223344",1000, "Pedro Sanchez")
        obj2 = CuentaCorriente("11223344",1000, "Juan Sanchez")
        print(obj)
        obj.ingresarDinero(1000)
        print(obj)
        obj.sacarDinero(200)
        print(obj)
        print("--------------------------------------------")
        print(obj.__eq__(obj2))


    if __name__ == "__main__" :
        main()
    
    