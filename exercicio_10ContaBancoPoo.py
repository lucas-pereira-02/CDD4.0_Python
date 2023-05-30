class Conta:
    def __init__(self,conta,nome,tipo,status=False):
        self.conta=conta
        self.saldo=0
        self.status=status
        self.nome=nome
        self.tipo=tipo
        self.limiteInicial=0
        self.limite=0

    def ativar(self):
        if self.status == False:
            self.status = True
            print("CONTA ATIVADA COM SUCESSO!")
        else:
            print("CONTA JA ATIVA")
    def desativar(self):
        if self.status == True:
            if self.saldo == 0:
                self.status = False
                print("CONTA DESATIVADA COM SUCESSO!")
            else:
                print("IMPOSSÍVEL DESATIVAR A CONTA, HÁ SALDO DISPONÍVEL!")
        else:
            print("PARA DESATIVAR A CONTA VOCÊ PRECISA TER UMA CONTA EM ABERTO!")
    def depositar(self,deposito):
        if self.status==True:
            if self.limite < self.limiteInicial:
                resto = self.limiteInicial - self.limite
                if deposito >= resto:

                    deposito = deposito - resto
                    self.limite = self.limite + resto
                    self.saldo += resto
                    self.saldo += deposito
                    print(f"DEPÓSITO REALIZADO COM SUCESSO!\n NOVO SALDO DISPONÍVEL: {self.saldo} LIMITE DISPONÍVEL: {self.limite}")
            else:
                self.saldo += deposito
                print(f"DEPÓSITO REALIZADO COM SUCESSO!\n NOVO SALDO DISPONÍVEL: {self.saldo} LIMITE DISPONÍVEL: {self.limite}")

        else:
            print("VOCÊ PRECISA TER UMA CONTA EM ABERTO PARA PODER REALIZAR DEPOSITOS")
    def sacar(self,sacar):
        if self.status==True:
            if sacar <= self.saldo:
                self.saldo=self.saldo-sacar
                print(f"SAQUE REALIZADO COM SUCESSO! NOVO SALDO DISPONÍVEL: {self.saldo}")
            else:
                if self.limite > 0:
                    saldoTotal=self.limite + self.saldo
                    if sacar <= saldoTotal:
                        self.saldo = self.saldo - sacar
                        self.limite = self.limite + self.saldo
                        print(f"SAQUE REALIZADO COM SUCESSO! NOVO SALDO DISPONÍVEL: {self.saldo} LIMITE DISPONÍVEL: {self.limite}")
                    else:
                        print("SALDO INSUFICIENTE PARA ESTE SAQUE")
                else:
                    print("SALDO INSUFICIENTE! VOCÊ NÃO POSSUI LIMITE PARA CHEQUE-ESPECIAL")
        else:
            print("PARA REALIZAR SAQUES VOCÊ PRECISA TER UMA CONTA ATIVA")



    def verificar(self):
        if self.status==True:
            print(f"SALDO DISPONÍVEL: {self.saldo}")

    def solicitarLimite(self,valorLimite):
        if valorLimite > 0:
            self.limiteInicial = valorLimite
            self.limite = valorLimite
            print(f"NOVO LIMITE ADICIONAL: {self.limite}")
        else:
            print("NÃO É POSSÍVEL ADICIONAR ESSE LIMITE")
    def verificarLimite(self):
        if self.status==True:
            print(f"SALDO DO LIMITE: {self.limite}")


c1 = Conta(123,"João","corrente")
c1.ativar()
c1.solicitarLimite(500)
c1.sacar(200)
c1.depositar(1000)
c1.verificar()