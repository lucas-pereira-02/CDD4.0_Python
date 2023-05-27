class Atleta():
    def __init__(self):
        self.aposentado=None
        self.peso=None
    def aposentar(self):
        self.aposentado=True
    def aquecer(self):
        print("O atleta está aquecendo")

class Corredor(Atleta):
    def __init__(self):
        super().__init__()
        self.peso=75
    def correr(self):
        print("O Corredor está correndo")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()
        self.peso=86
    def nadar(self):
        print("O nadador está nadando")

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()
        self.peso=80
    def pedalar(self):
        print("O Ciclista está pedalando")

class TriAtleta(Corredor,Nadador,Ciclista):
    def __init__(self):
        super().__init__()

atletaCorredor=Corredor()
atletaNadador=Nadador()
atletaCiclista=Ciclista()
triAtleta1 = TriAtleta()

atletaCorredor.aquecer()
atletaCorredor.correr()
atletaNadador.nadar()
atletaCiclista.pedalar()

triAtleta1.pedalar()
triAtleta1.correr()
