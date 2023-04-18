import random
from pprint import pprint

# Desafio 1
# Usando list compreheension, crie a seguinte lista:
# [2, 4, 6, 8, 10]
pprint([i*2 for i in range(1, 6)])

# Desafio 2
# Use a list compreheension usando a seguinte lista como base:
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
# para criar a lista a seguir:
# ['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rosa','6 - preto']
pprint([str(cores.index(cor)+1) + ' - ' + cor for cor in cores])

# Desafio 3
# Usando a lista seguir como base:
participantes = ['joel', 'jessica', 'maria',
                 'cris', 'larissa', 'rafael', 'marcus', 'john']
pagamento_realizado = ['joel', 'jessica', 'maria', 'cris']
"""Concatene (adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais,
somente nos casos onde seu nome esteja na lista 'pagamento_realizado', o resultado final  deve ser 
como  a lista a seguir:  """
pprint([i + ' PAGO' if i in pagamento_realizado else i +
        ' DEVENDO' for i in participantes])
