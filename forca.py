import random


def mensagemDeAbertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregaArquivo():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
     
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta
    
def inicializaLetrasAcertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista

def pedeChute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if(chute.upper() == letra.upper()):
            letrasAcertadas[index] = letra
        index += 1

def mensagemVitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagemDerrota(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprimeMensagemDeFimDeJogo(acertou,enforcou,palavraSecreta):
    if(acertou):
        mensagemVitoria()
    elif(enforcou):
        mensagemDerrota(palavraSecreta)


def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    mensagemDeAbertura()

    palavraSecreta = carregaArquivo()

    letrasAcertadas = inicializaLetrasAcertadas(palavraSecreta)

    enforcou =False
    acertou = False
    erros= 0

    print(letrasAcertadas)
    while(not enforcou and not acertou):
        
        chute = pedeChute()
        
        if(chute in palavraSecreta):
            marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta)
        else:
            erros += 1
            desenhaForca(erros)

            
        enforcou = erros == 7
        acertou = "_" not in letrasAcertadas
        print(letrasAcertadas)

        imprimeMensagemDeFimDeJogo(acertou, enforcou, palavraSecreta)



        

if(__name__ == "__main__"):
    jogar()


