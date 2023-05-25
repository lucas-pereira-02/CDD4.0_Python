class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea(self,base,altura):
        self.area = base * altura
        print(f"Area do retângulo {self.area}")
    def calcularPerimetro(self,base,altura):
        self.perimetro = (base+altura) * 2
        print(f"Perimetro do retângulo {self.perimetro}")


class Triangulo(Forma):
    def __init__(self):
        super().__init__()
        self.altura=0
    def calcularArea(self,base,altura):
        self.altura=altura
        self.area = (self.altura * base)/2
        print(f"Area do triangulo {self.area}")
    def calcularPerimetro(self,l1,l2,l3):
        self.perimetro = l1+l2+l3
        print(f"Perimetro do triangulo {self.perimetro}")

retangulo = Retangulo()
retangulo.calcularArea(30,15)
retangulo.calcularPerimetro(30,15)

triangulo = Triangulo()
triangulo.calcularPerimetro(20,40,40)
triangulo.calcularArea(20,40)