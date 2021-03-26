from cliente import Cliente
from conta import Conta
from banco_de_dados import Dados
from sys import exit
import re


# Status debugação:
# Escala de 1 a 10, quando mais proximo de 10, mais chances de ocorrer um bug

# Criação definitiva da conta do usuario:
# Criando e validando perfil do cliente:
# Status debugação: 5
def criar_cliente():
    while True:
        nome = validar_nome()
        idade = validar_idade()
        cpf = validar_cpf()
        senha = validar_senha()
        cliente_gerado = Cliente(nome, cpf, idade, senha)  # Passando os 4 argumentos para que a conta do cliente seja criada com sucesso pelo 'cliente.py'
        print('\n\t[ / ] Perfil do cliente criado com sucesso!\n')  # Mensagem de êxito
        return cliente_gerado


# Validações:
# Status debugação: 1
def validar_nome():
    while True:
        nome = input('\t[ ? ] Digite o nome do cliente. | ').strip().lower()
        nome = re.sub(' +', ' ', nome)  # Removendo espaçoes em brancos duplicado entre as palavras
        if nome.replace(' ', '').isalpha():  # Verificando se a contem apenas letras
            return nome.title()  # Colocando as primeiras letras das palavras em maiúsculas

        else:
            mensagem_erro_dados()


# Status debugação: 1
def validar_senha():
    while True:
        senha = input('\t[ ? ] Peça para o cliente inserir uma senha contendo apenas numeros. | ').strip().lower()
        senha = senha.replace(' ', '')  # Removendo os espaços
        if senha.isnumeric():  # Verificando se a resposta contém apenas números
            return senha

        else:
            mensagem_erro_dados()


# Status debugação: 1
def validar_idade():
    while True:
        idade = input('\t[ ? ] Digite a idade do cliente. | ').strip()
        if idade.isnumeric() and 18 <= int(idade) <= 120:  # Analisando se a resposta inserida é numerica e caso for, verifica se é maior ou igual 18 e menor igual 120
            return idade

        else:
            mensagem_erro_dados()


# Status debugação: 1
def mensagem_erro_dados():
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


# Status debugação: 1
def validar_cpf():
    while True:
        cpf = input('\t[ ? ] Digite o CPF do cliente. | ').strip()
        if validar_tamanho_cpf(cpf) and validar_cpf_no_banco_de_dados(cpf):  # Confere se as informações retornam True
            return cpf

        else:
            mensagem_erro_dados()


# Satus debugação: 1
def validar_tamanho_cpf(cpf):
    resposta = False
    if len(cpf) == 11 and cpf.isnumeric():  # Confere se o numero digitado tem ao maximo 11 digitos e confere se tem apenas numeros
        resposta = True

    return resposta


# Status debugação: 1
def validar_cpf_acesso():
    while True:
        cpf = input('\t[ ? ] Digite o CPF do cliente. | ').strip()
        if validar_tamanho_cpf(cpf) and (not validar_cpf_no_banco_de_dados(cpf)):  # Verifica se o cliente esta cadastrado no banco de dados
            return cpf

        else:
            mensagem_erro_dados()


# Status debugação: 1
def validar_cpf_no_banco_de_dados(cpf):
    banco_dados_cpf = open('banco_dados_cpf.txt', 'a')  # Banco de dados para armazenar cpfs
    banco_de_dados_cpf_leitura = open('banco_dados_cpf.txt', 'r')  # Banco de dados para leitura dos cpfs
    if cpf in banco_de_dados_cpf_leitura.read():  # Conferindo se já existe o cpf digitado
        return False

    else:  # Caso seja um cpf novo, o programa executará os seguintos codigos:
        banco_dados_cpf.write('\n{}\n'.format(cpf))  # Escrevendo novo cpf no arquivo 'banco_de_dados_cpf.txt'
        return True
# Fim das validações do perfil
# Terminando de criar o perfil do cliente


# Criação de conta:
# Status debugação: 1
def criar_conta(cliente_criado):
    while True:
        print('\t[ ! ] Finalizando cadastro do cliente: {}\n'.format(cliente_criado.nome))
        saldo = validar_saldo_limite('saldo')  # Passsando argumento 'saldo' para modificar a mensagem exibida
        limite = validar_saldo_limite('limite')
        conta_gerada = Conta(cliente_criado, saldo, limite)  # Criando conta do cliente
        print('\n\t[ / ] Conta do cliente criada com sucesso!\n')  # Mensagem de êxito
        return conta_gerada


# Validações:
# Status debugação: 1
def validar_saldo_limite(nome):
    while True:
        valor = input('\t[ ? ] Digite o {} que a conta terá. | R$'.format(nome)).strip()
        valor = valor.replace(' ', '')  # Removendo os espaços
        try:
            float(valor)

        except:
            if mensagem_erro_dados():
                continue

        if float(valor) <= 0:  # Não aceita valores negativos
            mensagem_erro_dados()
        else:
            return float(valor)


# Fim validações da conta
# Terminado criação de conta


# Status debugação: 5
def unir(cliente_criado, conta_criada):
    banco_dados_cpf = open('banco_dados_cpf.txt', 'a')  # Abrindo arquivo 'banco_dados_cpf' em modo append
    banco_de_dados = open('banco_de_dados.py', 'a')  # Abrindo arquivo 'banco_de_dados.py' em modo append
    banco_de_dados_leitura = open('banco_dados_cpf.txt', 'r')  # Abrindo arquivo 'banco_de_dados.py' em modo leitura
    banco_de_dados.write('\n{}if self.cpf == "{}" and self.senha == "{}":\n{}conta = dict(NOME="{}", CPF="{}", IDADE={}, SALDO={}, LIMITE={}, SENHA="{}")\n{}return conta\n'.format
                         (' ' * 8, cliente_criado.cpf, cliente_criado.senha, ' ' * 12,
                          cliente_criado.nome, cliente_criado.cpf,
                          cliente_criado.idade, conta_criada.saldo,
                          conta_criada.limite, cliente_criado.senha, ' ' * 12))

    # O comando acima escreve uma linha de codigo contendo os dados do cliente criado, e manda para o arquivo 'banco_de_dados.py'
    print('\t[ / ] Conta do cliente enviada ao banco de dados com sucesso!\n')
# Criação definitiva da conta do usuario concluida com sucesso


# Perguntas envolvendo a conta:
# Status debugação: 3
def perguntas_dentro_da_conta(conta_criada):
    print('\n\t[ 1 ] Para sacar dinheiro.\n\t[ 2 ] Para depositar dinheiro.\n\t[ 3 ] Para informar o saldo.')
    resposta_pergunta = input('\t=> ').strip()
    print()
    if resposta_pergunta == '1':
        quantidade_sacar = validar_deposito_saque('saque.')
        resultado_sacar = conta_criada.sacar(quantidade_sacar, conta_criada.saldo, conta_criada.limite)

    elif resposta_pergunta == '2':
        quantidade_deposito = validar_deposito_saque('deposito.')
        resultado_deposito = conta_criada.depositar(quantidade_deposito)

    elif resposta_pergunta == '3':
        conta_criada.consultar()

    else:
        mensagem_erro_dados()


# Status debugação: 5
def validar_deposito_saque(nome):
    while True:
        valor = input('\t[ ? ] Digite a quantidade do {} | R$'.format(nome)).strip()
        valor = valor.replace(' ', '')
        if valor.isnumeric() and int(valor) > 0:
            return float(valor)
        else:
            mensagem_erro_dados()
# Fim validações sobre saque e deposito


# Status debugação: 1
def perguntas_conta(conta_criada):
    while True:
        print('\t[ 1 ] Para alterar valores da conta.\n\t[ 2 ] Para sair do programa.')
        reposta = input('\t=> ').strip()
        if reposta == '1':
            perguntas_dentro_da_conta(conta_criada)

        elif reposta == '2':
            exit()

        else:
            print('\n\t[ ! ] Resposta ínvalida, tente novamente!\n')


# Status debugação: 1
def perguntas_conta_acesso(conta_criada):
    while True:
        print('\t[ 1 ] Para alterar valores da conta.\n\t[ 2 ] Para sair do programa.')
        reposta = input('\t=> ').strip()
        if reposta == '1':
            perguntas_dentro_da_conta(conta_criada)

        elif reposta == '2':
            return True

        else:
            print('\n\t[ ! ] Resposta ínvalida, tente novamente!\n')


# Status debugação: 3
def acessar_conta():
    while True:
        resposta_cpf = str(validar_cpf_acesso())
        resposta_senha = str(validar_senha())
        conta_banco_dados = Dados(resposta_cpf, resposta_senha)
        lista_informacoes = conta_banco_dados.conferir(resposta_cpf, resposta_senha)
        try:
            len(lista_informacoes)

        except:
            if mensagem_erro_dados():
                continue

        return lista_informacoes


# Status debugação: 4
def acessar_conta_editavel(conta_acesso):
    print('\n\t[ / ] Você entrou na conta do(a) cliente: {}\n'.format(conta_acesso['NOME']))
    nome_acesso = conta_acesso['NOME']
    cpf_acesso = conta_acesso['CPF']
    idade_acesso = conta_acesso['IDADE']
    senha_acesso = conta_acesso['SENHA']
    saldo_acesso = conta_acesso['SALDO']
    limite_acesso = conta_acesso['LIMITE']
    comando_dicionario = 'if self.cpf == "{}" and self.senha == "{}":'.format(cpf_acesso, senha_acesso)
    cliente_gerado_acesso = Cliente(nome_acesso, cpf_acesso, idade_acesso, senha_acesso)
    conta_gerada_acesso = Conta(cliente_gerado_acesso, saldo_acesso, limite_acesso)
    if perguntas_conta_acesso(conta_gerada_acesso):
        deletar_e_adicionar(comando_dicionario, cliente_gerado_acesso, conta_gerada_acesso)

    return comando_dicionario


# Status debugação: 7
def encontrar_comando(comando_dicionario):
    with open('banco_de_dados.py', 'r') as f:
        texto = f.readlines()
    for i in texto:
        if comando_dicionario in i:
            onde_esta = int(texto.index(i)) + 2
            return onde_esta
    print('\t[ ! ] Erro indefinido.')


# Status debugação: 8
def deletar_linha(numero_linha, cliente_gerado_acesso, conta_gerada_acesso):
    with open('banco_de_dados.py', 'r') as f:
        texto = f.readlines()
    with open('banco_de_dados.py', 'w') as f:
        contador = 0
        for i in texto:
            contador += 1
            if contador == numero_linha:
                f.write('{}conta = dict(NOME="{}", CPF="{}", IDADE={}, SALDO={}, LIMITE={}, SENHA="{}")\n'.format((' ' * 12), cliente_gerado_acesso.nome, cliente_gerado_acesso.cpf, cliente_gerado_acesso.idade, conta_gerada_acesso.saldo, conta_gerada_acesso.limite, cliente_gerado_acesso.senha))

            else:
                f.write(i)


# Status debugação: 2
def deletar_e_adicionar(comando_if, cliente_gerado_acesso, conta_gerada_acesso):
    linha_deletar = encontrar_comando(comando_if)
    deletar_linha(linha_deletar, cliente_gerado_acesso, conta_gerada_acesso)
    print('\n\t[ / ] Conta do cliente enviada ao banco de dados com sucesso!\n')


# Status debugação: 1
def iniciar_programa():
    while True:
        # Formar o cabeçalho:
        print('\t{}'.format('=-' * 9 + '$' * 3 + '=-' * 9))
        print('\t[ 1 ] Para criar uma conta no banco.\n\t[ 2 ] Para acessar uma conta já criada.\n\t[ 3 ] Para sair do programa.')
        reposta = input('\t=> ').strip()
        print()

        if reposta == '1':
            cliente_criado = criar_cliente()  # Criando perfil do cliente
            conta_criada = criar_conta(cliente_criado)  # Criando conta do cliente
            uniao_conta_perfil_cliente = unir(cliente_criado, conta_criada)  # Unindo as informações
            perguntas_conta(conta_criada)  # Perguntando se deseja alterar valores da conta ou sair

        elif reposta == '2':
            conta_acesso = acessar_conta()  # Entrando no modo acesso a conta
            comando_if = acessar_conta_editavel(conta_acesso)
            break

        elif reposta == '3':
            exit()  # Saindo do programa

        else:
            print('\t[ ! ] Resposta ínvalida, tente novamente!')  # Mensagem de erro


# Iniciando programa:
iniciar_programa()
