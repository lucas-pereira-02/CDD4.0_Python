#exercicio para imprimir números repetindo a quantidade do mesmo
#1
#22
#333
def exercicio_3(num):
    for x in range(num):
#srt() converte para string
        print(str(x)*x)
exercicio_3(7)
#aqui ele vai imprimir um "none" no final porque a função não tem retorno
print(exercicio_3(5))