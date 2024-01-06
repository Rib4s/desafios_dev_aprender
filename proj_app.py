import os
import random

status = True

while status:
    # Criar listas.
    nomes = ['Nome-1', 'Nome-2', 'Nome-3', 'Nome-4', 'Nome-5']
    emails = ['email-1@gmail.com', 'email-2@gmail.com', 'email-3@gmail.com', 'email-4@gmail.com', 'email-5@gmail.com']
    telefones = ['1111-1111', '2222-2222', '3333-3333', '4444-4444','5555-5555']
    cidades = ['Cidade-1', 'Cidade-2', 'Cidade-3', 'Cidade-4', 'Cidade-5']
    estados = ['Estado-1', 'Estado-2', 'Estado-3', 'Estado-4', 'Estado-5']

    # Criar apresentação, menu de opções e escolha.
    print('Olá, bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa digite "parar"')
    print('-'*90)
    print('Escolha uma ou mais opções abaixo a serem geradas aleatóriamente:\n'
        '[1] - Nome\n'
        '[2] - E-mail\n'
        '[3] - Telefone\n'
        '[4] - Cidade\n'
        '[5] - Estado')
    entrada = input('Digite uma(as) opções: ')
    lista = entrada.split(",")

    # Condição para encerrar o programa
    if entrada == 'parar':
        break
    print('-'*90)

    # Gerar os dados aleatórios, conforme multipla escolha do usuário.
    save = input('Gostaria de salvar os dados em um arquivo de texto?(s/n) ')
    nome = random.choice(nomes)
    email = random.choice(emails)
    telefone = random.choice(telefones)
    cidade = random.choice(cidades)
    estado = random.choice(estados)
    valores = []

    # Criar condicionais
    if '1' in lista:
        valores.append(nome)
    if '2' in lista:
        valores.append(email)
    if '3' in lista:
        valores.append(telefone)
    if '4' in lista:
        valores.append(cidade)
    if '5' in lista:
        valores.append(estado)

    # Imprimir valores em coluna
    for valor in valores:
        print(valor)

    # Salvar os dados
    if save == 's':
        with open('Valores.txt', 'a') as arquivo:
            for valor in valores:
                arquivo.write(valor + os.linesep)

    # Limpar a lista de valores
    valores.clear()
    print('-'*90)

# Mensagem de encerramento
print('Encerrando o programa')
