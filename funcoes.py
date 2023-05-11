#Biblioteca de funcoes criada por Lucas Nascimento no curso CDD4.0
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

def imprimir_nome(nome):
#f - print formatado
    print(f"Nome: {nome}")

#conta quantas vogais tem em um texto
def vogais(t):
    qtVogais = 0
    for j in t:
        if j in "AaEeIiOoUu":
            qtVogais=qtVogais+1
    print(qtVogais)

#conta quantas letras tem em um texto
def letras(t):
    qtLetras = 0
    for j in t:
        if j != " ":
            qtLetras=qtLetras+1
    print(qtLetras)

def valorEstoque(produto,quantidade,valor):
    nomeProduto = produto
    valorTotal = valor * quantidade
    return nomeProduto,valorTotal

def tipoArgumento(num):
    if num > 0:
        return "P"
    elif num < 0:
        return "N"
    else:
        return "Z"

# * na frente dos argumentos serve para argumentos ilimitados
def somarIlimitado(*numeros):
    soma = 0
    for x in numeros:
        soma+=x
    return soma