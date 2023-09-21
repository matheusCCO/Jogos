print("Jogo da Velha")

#jogador1 = input("Digite o nome do Jogador 1: ")

#jogador2 = input("Digite o nome do Jogador 2: ")

tabuleuro = [" "]* 9


def tabuleiro():
    print(tabuleuro[0]+" | "+tabuleuro[1]+" | "+ tabuleuro[2])
    print(tabuleuro[3]+" | "+tabuleuro[4]+" | "+ tabuleuro[5])
    print(tabuleuro[6]+" | "+tabuleuro[7]+" | "+ tabuleuro[8])

cont = 0
tabuleiro()


for i in range(0,10):
    
    jogada = int(input("digite a sua jogada:"))

    if jogada in range(1,10):
        if tabuleuro[jogada - 1] == " ":
            if cont % 2:
                tabuleuro[jogada - 1] = "X"
            else:
                tabuleuro[jogada - 1] = "O"
        else:
            print("invalido")
    tabuleiro()
    cont = cont +1