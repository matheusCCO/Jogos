print("Jogo da Velha")

tabuleuro = [" "]* 9


def tabuleiro():
    print(tabuleuro[0]+" | "+tabuleuro[1]+" | "+ tabuleuro[2])
    print(tabuleuro[3]+" | "+tabuleuro[4]+" | "+ tabuleuro[5])
    print(tabuleuro[6]+" | "+tabuleuro[7]+" | "+ tabuleuro[8])

def verificaJogoX(tabuleuro):
    if(tabuleuro[0] =="X" and tabuleuro[1] =="X" and tabuleuro[2] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[3] =="X" and tabuleuro[4] =="X" and tabuleuro[5] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[6] =="X" and tabuleuro[7] =="X" and tabuleuro[8] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[0] =="X" and tabuleuro[4] =="X" and tabuleuro[8] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[2] =="X" and tabuleuro[4] =="X" and tabuleuro[6] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[0] =="X" and tabuleuro[3] =="X" and tabuleuro[6] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[1] =="X" and tabuleuro[4] =="X" and tabuleuro[7] =="X"):
        print("Jogador X Ganhou!!")
        return True
    elif(tabuleuro[2] =="X" and tabuleuro[5] =="X" and tabuleuro[8] =="X"):
        print("Jogador X Ganhou!!")
        return True

def verificaJogoO(tabuleuro):
    if(tabuleuro[0] =="O" and tabuleuro[1] =="O" and tabuleuro[2] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[3] =="O" and tabuleuro[4] =="O" and tabuleuro[5] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[6] =="O" and tabuleuro[7] =="O" and tabuleuro[8] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[0] =="O" and tabuleuro[4] =="O" and tabuleuro[8] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[2] =="O" and tabuleuro[4] =="O" and tabuleuro[6] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[0] =="O" and tabuleuro[3] =="O" and tabuleuro[6] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[1] =="O" and tabuleuro[4] =="O" and tabuleuro[7] =="O"):
        print("Jogador O Ganhou!!")
        return True
    elif(tabuleuro[2] =="O" and tabuleuro[5] =="O" and tabuleuro[8] =="O"):
        print("Jogador O Ganhou!!")
        return True

def jogada(jogador, jogada):
    for jogada in range(0,10):
        if(jogador == 1):
            if(tabuleiro[jogada - 1] == " "):
                tabuleiro[jogada - 1] = "O"
            else:
                print("Invalido. Repita a Jogada.")
                tabuleiro()

        if(jogador == 2):
            if(tabuleiro[jogada - 1] == " "):
                tabuleiro[jogada - 1] = "X"
        

def jogo(jogador1,jogador2):
    cont = 0
    for i in range(0,10):
        if(cont%2 == 0):
            print("Vez do jogador "+ jogador1)
            jogador = 1
        else:
            print("Vez do jogador "+ jogador2)
            jogador = 2
        jogada = int(input("digite a sua jogada:"))

        if jogada in range(1,10):
            if tabuleuro[jogada - 1] == " ":
                if cont % 2:
                    tabuleuro[jogada - 1] = "X"
                else:
                    tabuleuro[jogada - 1] = "O"
            else:
                print("invalido")
                jogada = int(input("digite a sua jogada:"))
                
        tabuleiro()
        fimDeJogo = verificaJogoX(tabuleuro)
        if(fimDeJogo == True):
            break
        fimDeJogo = verificaJogoO(tabuleuro)
        if(fimDeJogo == True):
            break
        cont = cont +1


tabuleiro()

jogado1 = "Matheus" #input("Digite o nome do Jogador 1: ")
jogado2 = "Lele" #input("Digite o nome do Jogador 2: ")
print("")
print("Ola Jogadores "+jogado1+" e "+jogado2+" bem vindos")
print("Por padrão o jogador "+jogado1+" ficara com a peças O")
print("E o jogador "+jogado2+"ficara com a peças X")
print("")

print("Para as jogados acontecem, cada jogador deve digitar o numero da casa que deseja marcar.")
print(" 1 | 2 | 3 ")
print(" 4 | 5 | 6 ")
print(" 7 | 8 | 9 ")

jogo(jogado1,jogado2)