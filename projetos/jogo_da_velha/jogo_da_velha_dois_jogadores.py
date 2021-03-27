# Cores:
vermelho = '\033[1;31m'
verde = '\033[1;32m'
parar = '\033[m'


def validar_jogada(lugar, nome):
    while True:
        print('\t[ / ] Vez do {} jogador!'.format(nome))
        resposta = input('\t=> ')
        if resposta == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            if resposta in lugar:
                return resposta
            else:
                print('\t[ ! ] Ocorreu um erro, revise as informações inseridas.')
                return 1


def partida():

    vez_jogada = 1
    lugar = ['7', '8', '9', '4', '5', '6', '1', '2', '3']

    while True:
        xo = 0
        print('\t{}'.format('=-' * 4 + 'X' + '=-' * 4))
        print('''\t[ {} ] [ {} ] [ {} ]\n\t[ {} ] [ {} ] [ {} ]\n\t[ {} ] [ {} ] [ {} ]'''.format(lugar[0], lugar[1], lugar[2], lugar[3], lugar[4], lugar[5], lugar[6], lugar[7], lugar[8]))
        print('\t{}'.format('=-' * 4 + 'O' + '=-' * 4))

        for i in lugar:
            if i == '\x1b[1;32mX\x1b[m' or i == '\x1b[1;31mO\x1b[m':
                xo += 1
            if xo == 9:
                print('\t[ ! ] Deu velha!')
                exit()

        var = quem_ganha(lugar)
        if var == 1:
            print('\t[ ! ] Você ganhou!')
            exit()
        elif var == 2:
            print('\t[ ! ] Computador ganhou!')
            exit()

        if vez_jogada == 1:
            jogador = validar_jogada(lugar, 'primeiro')
            if jogador == 1:
                continue

            else:
                lugar_index = lugar.index(jogador)
                lugar.remove(jogador)
                mensagem = '{}X{}'.format(verde, parar)
                lugar.insert(lugar_index, mensagem)
                vez_jogada = 2

        elif vez_jogada == 2:
            jogador = validar_jogada(lugar, 'segundo')
            lugar_index = lugar.index(jogador)
            lugar.remove(jogador)
            mensagem = '{}O{}'.format(vermelho, parar)
            lugar.insert(lugar_index, mensagem)
            vez_jogada = 1


def quem_ganha(lista):
    contador = 1
    comparacao = 0
    while contador <= 8:
        if contador == 1:
            comparacao = lista[0] == lista[1] == lista[2]

        elif contador == 2:
            comparacao = lista[3] == lista[4] == lista[5]

        elif contador == 3:
            comparacao = lista[6] == lista[7] == lista[8]

        elif contador == 4:
            comparacao = lista[0] == lista[3] == lista[6]

        elif contador == 5:
            comparacao = lista[1] == lista[4] == lista[7]

        elif contador == 6:
            comparacao = lista[2] == lista[5] == lista[8]

        elif contador == 7:
            comparacao = lista[2] == lista[4] == lista[6]

        elif contador == 8:
            comparacao = lista[0] == lista[4] == lista[8]

        if comparacao and (contador == 1 or contador == 4 or contador == 8):
            if lista[0] == '\x1b[1;32mX\x1b[m':
                return 1
            else:
                return 2
        if comparacao and (contador == 7 or contador == 5 or contador == 2):
            if lista[4] == '\x1b[1;32mX\x1b[m':
                return 1
            else:
                return 2
        if comparacao and (contador == 6 or contador == 3):
            if lista[8] == '\x1b[1;32mX\x1b[m':
                return 1
            else:
                return 2
        contador += 1
    return 3


partida()
