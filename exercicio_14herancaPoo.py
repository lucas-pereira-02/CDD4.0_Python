class Atleta():
    def __init__(self,peso):
        self.aposentado=False
        self.aquecendo=False
        self.peso=peso
        self.correndo=False
        self.nadando=False
        self.pedalando=False
    def aposentar(self):
        self.aposentado=True
        print("O atleta foi aposentado")
    def aquecer(self):
        if self.aposentado==False:
            if self.aquecendo==False:
                self.aquecendo=True
                print("O atleta está aquecendo")
            else:
                print("O atleta ja estava aquecendo")
        else:
            print("O atleta não pode aquecer, pois está aposentado")

class Corredor(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
    def correr(self):
        if self.aposentado==False:
            if self.aquecendo==True:
                if self.correndo==False:
                    self.correndo=True
                    print("O atleta começou a correr")
                else:
                    print("O atleta ja estava correndo")
            else:
                print("O atleta precisa aquecer antes correr")
        else:
            print("O atleta não pode correr, pois está aposentado")
    def pararDeCorrer(self):
        if self.correndo==True:
            self.correndo=False
            print("O atleta parou de correr")
        else:
            print("O atleta precisa correr para poder parar de correr")

class Nadador(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.peso=peso
    def nadar(self):
        if self.aposentado==False:
            if self.aquecendo==True:
                if self.nadando==False:
                    self.dadando=True
                    print("O atleta começou a nadar")
                else:
                    print("O atleta ja estava nadando")
            else:
                print("O atleta precisa aquecer antes nadar")
        else:
            print("O atleta não pode nadar, pois está aposentado")
    def pararDeNadar(self):
        if self.nadando==True:
            self.nadando=False
            print("O atleta parou de nadar")
        else:
            print("O atleta precisa nadar para poder parar de nadar")

class Ciclista(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.peso=peso
    def pedalar(self):
        if self.aposentado==False:
            if self.aquecendo==True:
                if self.pedalando==False:
                    self.pedalando=True
                    print("O atleta começou a pedalar")
                else:
                    print("O atleta ja estava pedalando")
            else:
                print("O atleta precisa aquecer antes pedalar")
        else:
            print("O atleta não pode pedalar, pois está aposentado")
    def pararDePedalar(self):
        if self.pedalando==True:
            self.pedalando=False
            print("O atleta parou de pedalar")
        else:
            print("O atleta precisa pedalar para poder parar de pedalar")
class TriAtleta(Corredor,Nadador,Ciclista):
    def __init__(self,peso):
        super().__init__(peso)

    def correr(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                if self.nadando == False:
                    if self.pedalando == False:
                        if self.correndo == False:
                            self.correndo=True
                            print("O atleta está correndo")
                        else:
                            print("O atleta ja estava correndo")
                    else:
                        print("O atleta precisa parar de pedalar para correr")
                else:
                    print("O atleta precisa parar de nadar para correr")
            else:
                print("O atleta precisa aquecer antes de correr")
        else:
            print("O atleta não pode correr, pois está aposentado")
    def nadar(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                if self.correndo == False:
                    if self.pedalando == False:
                        if self.nadando == False:
                            self.nadando=True
                            print("O atleta está nadando")
                        else:
                            print("O atleta ja estava nadando")
                    else:
                        print("O atleta precisa parar de pedalar para nadar")
                else:
                    print("O atleta precisa parar de correr para nadar")
            else:
                print("O atleta precisa aquecer antes de nadar")
        else:
            print("O atleta não pode nadar, pois está aposentado")
    def pedalar(self):
        if self.aposentado == False:
            if self.aquecendo == True:
                if self.correndo == False:
                    if self.nadando == False:
                        if self.pedalando == False:
                            self.pedalando=True
                            print("O atleta está pedalando")
                        else:
                            print("O atleta ja estava pedalando")
                    else:
                        print("O atleta precisa parar de nadar para padelar")
                else:
                    print("O atleta precisa parar de correr para pedalar")
            else:
                print("O atleta precisa aquecer antes de pedalar")
        else:
            print("O atleta não pode pedalar, pois está aposentado")

atletaCorredor=Corredor(78)
atletaNadador=Nadador(85)
atletaCiclista=Ciclista(80)
triAtleta1=TriAtleta(75)
atletaCorredor.aquecer()
atletaCorredor.correr()
atletaNadador.nadar()
atletaCiclista.pedalar()
triAtleta1.aquecer()
triAtleta1.pedalar()
triAtleta1.correr()
triAtleta1.pararDePedalar()
triAtleta1.correr()