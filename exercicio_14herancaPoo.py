class Atleta():
    def __init__(self):
        self.aposentado=False
        self.peso=None
    def aposentar(self):
        self.aposentado=True
        print("O atleta foi aposentado")
    def aquecer(self):
        if self.aposentado==False:
            print("O atleta está aquecendo")
        else:
            print("O atleta não pode aquecer, pois está aposentado")

class Corredor(Atleta):
    def __init__(self):
        super().__init__()
        self.peso=75
    def correr(self):
        if self.aposentado==False:
            print("O atleta está correndo")
        else:
            print("O atleta não pode correr, pois está aposentado")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()
        self.peso=86
    def nadar(self):
        if self.aposentado==False:
            print("O atleta está nadando")
        else:
            print("O atleta não pode nadar, pois está aposentado")


class Ciclista(Atleta):
    def __init__(self):
        super().__init__()
        self.peso=80
    def pedalar(self):
        if self.aposentado==False:
            print("O atleta está pedalando")
        else:
            print("O atleta não pode pedalar, pois está aposentado")


class TriAtleta(Corredor,Nadador,Ciclista):
    def __init__(self):
        super().__init__()

atletaCorredor=Corredor()
atletaNadador=Nadador()
atletaCiclista=Ciclista()
triAtleta1 = TriAtleta()
triAtleta1.aposentar()
atletaCorredor.aquecer()
atletaCorredor.correr()
atletaNadador.nadar()
atletaCiclista.pedalar()

triAtleta1.pedalar()
triAtleta1.correr()