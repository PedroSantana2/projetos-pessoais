import random
import time
import sys


# Cores:
roxo = '\033[35m'
parar = '\033[m'
vermelho = '\033[31m'
azul = '\033[34m'
amarelo = '\033[33m'


def pensamento_maquina():
    print('\t{}[ / ] Estou pensando em um numero entre 1 e 3, tente adivinhar...{}'.format(amarelo, parar))
    print('\t{}'.format('=-' * 33))             
    numero_aleatorio = random.randint(1, 3)
    return numero_aleatorio
     

def jogada_jogador():
    while True:
        jogada_jogador = input('\tSua jogada | => ').strip()
        if jogada_jogador.isnumeric() and (int(jogada_jogador) <= 3 and int(jogada_jogador) > 0):
            return int(jogada_jogador)
        else:
            mensagem_erro()


def mensagem_erro():
    while True:
        print('\n\t[ ! ] Ocorreu um erro!')
        print('\t[ 1 ] Para tentar novamente.\n\t[ 2 ] Para sair do programa.')
        resposta_jogador = input('\t=> ').strip()
        print()
        if resposta_jogador == '1':
            return True
        
        elif resposta_jogador == '2':
            exit()

        else:
            print('\t[ ! ] Resposta inválida.')


def comparar(jogada_computador, jogada_player):
    if jogada_player == jogada_computador:
        return 1  # Significa que o jogador ganhou
    else:
        return 2  # Significa que o computador ganhou


def iniciar_partida():
    print()
    while True:
        print('\t[ ? ] Quantas partidas você deseja jogar?')
        partidas = input('\t=> ').strip()
        if partidas.isnumeric() and int(partidas) > 0:
            partidas = int(partidas)
            break
        else:
            if mensagem_erro():
                continue

    print('\n\t[ ! ] Iniciando jogo!\n')
    vitorias = 0
    derrotas = 0
    while partidas > 0:
        # Iniciando:
        print('\t{}'.format('=-' * 33))
        jogada_computador = pensamento_maquina()  # Computador escolhendo jogada
        jogada_player = jogada_jogador()  # Jogador escolhendo jogada
        if comparar(jogada_computador, jogada_player) == 1:
            print('\n\t[ ! ] Você ganhou!')
            vitorias += 1
        else:
            print('\n\t[ ! ] Você perdeu!')
            print('\t[ ! ] O número que pensei foi: {}'.format(jogada_computador))
            derrotas += 1
        partidas -= 1
        print('\n\t[ / ]{} Vitórias: {} | Derrotas: {}{}\n'.format(roxo, vitorias, derrotas, parar))


iniciar_partida()
