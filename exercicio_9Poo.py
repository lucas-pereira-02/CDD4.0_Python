class Pessoas:
#comendo sempre vai ser False, a menos que passe algum parametro para ele na hora de chamar a função
    def __init__(self,nome,peso,idade,comendo=False,correndo=False,falando=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.correndo=correndo
        self.falando=falando
    def comer(self,comida):
        self.comida=comida
        if self.falando==False:
            if self.comendo==False:
                self.comendo = True
                print(f"{self.nome} está comendo {self.comida} ")
            else:
                print(f"{self.nome}Não pode comer porque ja está comendo")
        else:
            print("Você precisa parar de falar para comer")

    def pararDeComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} só pode parar de comer se estiver comendo")

    def correr(self):
        self.correndo=True
        print(f"{self.nome} está correndo")

    def pararDeCorrer(self):
        if self.correndo==True:
            self.correndo=False
            print(f"{self.nome} parou de correr")
        else:
            print(f"{p} só pode parar de correr se estiver correndo")

    def falar(self):
        if self.comendo==False:
            self.falando=True
            print(f"{self.nome} está falando")
        else:
            print(f"Você precisa terminar de comer para depois falar")
#é possível chamar apenas 3 parametros porque o parametro comendo ja está definido
p1 = Pessoas("Lucas",72,23)
p2 = Pessoas("Maria",56,23)

print(f"{p1.nome} pesa {p1.peso} e tem {p1.idade} anos")
print(f"{p2.nome} pesa {p2.peso} e tem {p2.idade} anos")

#se quisermos imprimir todos os atributos de uma vez usamos o vars(), que vai mostrar tudo em forma de dicionário
print(vars(p1))

p1.comer("feijão")
p1.correr()
p1.falar()