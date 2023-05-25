game = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
a = game[0]
b = game[1]
c = game[2]

jogo = ['a', 'b', 'c']

print(f"\na = {game[0]}\nb = {game[1]}\nc = {game[2]}")

while True:

    jogar = input("Escolha o local que vai jogar: ")
    for x in range(3):
        if jogar in game[x]:
            for y in range(3):
                print(game[x][y])