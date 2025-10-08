class Punto:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def setXY(self,x,y):
        self.x = x
        self.y = y
    
    def desplaza(self,dx,dy):
        self.x += dx
        self.y = dy
        
    def distancia(self,other):
        return f'({self.x-other.x},{self.y-other.y})'
    
    def __str__(self):
        return f'({self.x},{self.y})'
    
def main():
    
    punto1 = Punto(1,3)
    punto2 = Punto(2,4)
    
    print(punto1.distancia(punto2))
    
    punto2.desplaza(2,2)
    print(punto1.distancia(punto2))
    
if __name__ == "__main__":
    
    main()

    
    
    
    
        