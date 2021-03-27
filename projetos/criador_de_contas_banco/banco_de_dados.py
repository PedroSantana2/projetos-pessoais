class Dados:
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha

    def conferir(self, cpf, senha):
        conta = 0
        