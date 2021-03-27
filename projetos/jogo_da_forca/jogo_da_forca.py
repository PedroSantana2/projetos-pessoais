palavra_secreta = input("Digite a palavra secreta:").lower().strip()  

for x in range(100):  # Espaçoes para inciar o jogo
    print()

digitadas = []
acertos = []
erros = 0

while True:
    formar_palavra = ""
    for letra in palavra_secreta:  # Percorre todas as letras da palavra escrita e confere se o player já acertou alguma letra, caso 
        if letra in acertos:                                                                            # contrario ele escreve um ponto.
            formar_palavra += letra
        else:
            formar_palavra += '.'
        
    print(formar_palavra)

    if formar_palavra == palavra_secreta:
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
        break

    letra_tentativa = input("\nDigite uma letra:").lower().strip()

    if letra_tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue

    else:
        digitadas += letra_tentativa
        if letra_tentativa in palavra_secreta:
            acertos += letra_tentativa
    
        else:
            print("Você errou!")
            erros += 1
        
    
    print("X==:==\nX  :   ")
    if erros >= 1:
        print('X  O   ')

    else:
        print('X')
    
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    
    elif erros == 3:
        linha2 = " \|   "
    
    elif erros >= 4:
        linha2 = " \|/ "
    
    print("X{}".format(linha2))
    linha3 = ""

    if erros == 5:
        linha3 += " /     "
    
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")

    if erros == 6:
        print("Você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
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
        break