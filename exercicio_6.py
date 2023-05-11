#calcular valor total de produtos no estoque e retornar o nome e o valor total a partir da biblioteca funcoes
from funcoes import valorEstoque
nomeProduto = input("Digite o nome do produto: ")
qtProduto =  int(input("Digite a quantidade de produtos: "))
valorUni =  float(input("Digite o valor unitário: "))
valor = valorEstoque(nomeProduto,qtProduto,valorUni)
print(valor)