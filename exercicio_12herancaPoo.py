class Ingresso():
    def __init__(self,valor):
        self.valor=valor
    def imprimirValor(self):
        print(f"O valor do ingresso fica: R${self.valor}")
class IngressoVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)

#
    def imprimirValor(self):
        adicional =(self.valor * 50) / 100
        self.valor+=adicional
        print(f"O valor do ingresso VIP fica: R${self.valor}")

ingressoNormal = Ingresso(120)
ingressoVip = IngressoVip(120)

ingressoNormal.imprimirValor()
ingressoVip.imprimirValor()