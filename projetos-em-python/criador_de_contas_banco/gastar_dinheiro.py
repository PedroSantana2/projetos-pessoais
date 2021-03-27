import random
import time


class Gastar:

    def __init__(self, saldo, limite):
        self.saldo = saldo
        self.limite = limite

    def mensagem_erro_dados(self):
        while True:
            print('\n\t[ ! ] Um erro foi encontrado, revise as informações inseridas.')
            print('\t[ 1 ] Para tentar novamente.\n\t[ 2 ] Para sair do programa.')
            resposta_erro_dados = input('\t=> ').strip()
            print()

            if resposta_erro_dados == '1':
                return True

            elif resposta_erro_dados == '2':
                exit()

            else:
                print('\t[ ! ] Resposta inválida!\n')

    def velocidade_niquel(self, giros, tempo):
        numero_1 = 0
        numero_2 = 0
        numero_3 = 0
        for i in range(1, (giros + 1)):
            numero_1 = random.randint(1, 3)
            numero_2 = random.randint(1, 3)
            numero_3 = random.randint(1, 3)
            for a in range(1, 101):
                print()
            print('\t{}'.format('=-' * 4 + '$' + '-=' * 4))
            print('\t[ {} ] [ {} ] [ {} ]'.format(numero_1, numero_2, numero_3))
            print('\t{}'.format('=-' * 4 + '$' + '-=' * 4))
            time.sleep(tempo)
        lista_numeros = [numero_1, numero_2, numero_3]
        return lista_numeros

    def comparcao(self, lista):
        if lista[0] == lista[1] == lista[2]:
            print('\n\t[ 3X ] VOCÊ GANHOU A MULTIPLICAÇÃO MÁXIMA!')
            return 1

        elif lista[0] == lista[1] or lista[1] == lista[2]:
            print('\n\t[ 2X ] VOCÊ GANHOU A SEGUNDA MAIOR MULTIPLICAÇÃO!')
            return 2

        else:
            print('\n\t[ 0X ] VOCÊ PERDEU O VALOR DA APOSTA!')
            return 3

    def niquel(self, valor_apostado):
        print('\n\t[ / ] Boa sorte!')
        time.sleep(2)
        # Modo rapido
        rodadas_rapido = random.randint(10, 20)
        self.velocidade_niquel(rodadas_rapido, 0.3)

        # Modo velocidade media
        rodadas_media = random.randint(5, 10)
        self.velocidade_niquel(rodadas_media, 0.6)

        # Modo lento
        rodadas_lento = random.randint(3, 6)
        lista_numeros = self.velocidade_niquel(rodadas_lento, 1.2)
        resultado = self.comparcao(lista_numeros)
        if resultado == 1:
            valor_final = valor_apostado * 3

        elif resultado == 2:
            valor_final = valor_apostado * 2

        else:
            valor_final = valor_apostado * 0
        return valor_final


