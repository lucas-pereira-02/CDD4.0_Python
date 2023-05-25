#classe Iguana(Animal) vai herdar os atributos de sua classe pai Animal()

class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"O {self.nome} foi comer")
class Iguana(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def movimentar(self):
        print(f"o {self.nome} subiu na árvore")
class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def comer(self):
        print(f"O {self.nome} foi comer galinha")

iguana = Iguana("banguela","verde")
cachorro = Cachorro("Logan","capa-preta")

iguana.comer()
iguana.movimentar()
cachorro.comer()