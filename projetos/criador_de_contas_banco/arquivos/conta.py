class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, dinheiro_sacar, saldo, limite):
        if self.saldo - dinheiro_sacar < (limite * -1):
            print('\n\t[ ! ] Ação ínvalida, limite atingido!')
            print('\t[ ! ] O saldo é de: R${:.2f}'.format(self.saldo))
            print('\t[ ! ] O limite da conta é de: R${:.2f}\n'.format(self.limite))

        else:
            antigo = self.saldo
            self.saldo = saldo - dinheiro_sacar
            print('\n\t[ ! ] O saldo da conta era R${:.2f} e agora passou a ser de R${:.2f}\n'.format(antigo, self.saldo))

    def depositar(self, valor_deposito):
        antigo_saldo = self.saldo
        self.saldo = float(self.saldo) + valor_deposito
        print('\n\t[ ! ] O saldo da conta era R${:.2f} e agora passou a ser de R${:.2f}\n'.format(antigo_saldo, self.saldo))

    def consultar(self):
        print('\t[ ! ] O saldo é de: R${:.2f}\n'.format(self.saldo))
