def somar(a,b):
    soma=0
    soma=a+b
    return soma
def multiplicar(a,b):
    multiplicacao=0
    multiplicacao=a*b
    return multiplicacao
def subtrair(a,b):
    subtracao=0
    subtracao=a-b
    return subtracao
def dividir(a,b):
    divisao=0
    divisao=a/b
    return divisao
resp = "s"
while True:
    operacao = int(input("Selecione a operação: \n 1.SOMAR \n 2.MULTIPLICAR \n 3.SUBTRAIR \n 4.DIVIDIR \n 5.SAIR \n"))
    if operacao == 5:
        break
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    match operacao:
        case 1:
            print(somar(n1,n2))
        case 2:
            print(multiplicar(n1,n2))
        case 3:
            print(subtrair(n1,n2))
        case 4:
            print(dividir(n1,n2))
        case 5:
            break
        case _:
            print("Opção inválida!")
