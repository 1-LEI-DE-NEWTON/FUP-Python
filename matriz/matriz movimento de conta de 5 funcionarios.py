
from random import randint

v_saldo = []
v_valores_random = []
matriz = []
v_novo_saldo = []
v_op_bancarias = []

while len (v_valores_random)<5:
    v_valores_random.append(randint(1,100))

for i in range (5):
    linha = []
    if i == 0:
        for j in range (5):
            linha.append(input('informe o seu nome [' + str(i) + ',' + str(j) + ']:' + '\n'))
        matriz.append(linha)
    if i == 1:
        for j in range (5):
            linha.append(input('informe o número da sua conta [' + str(i) + ',' + str(j) + ']:' + '\n'))
        matriz.append(linha)
    if i == 2:
        for j in range (5):
            saldo = int(input('informe o seu saldo' +' \n'))
            v_saldo.append(saldo)
            linha.append(saldo)
        matriz.append(linha)
    if i == 3:
        for j in range (5):
            OP = input('informe a Operação Bancária, C para crédito e D para débito' + '\n')
            linha.append(OP)
            v_op_bancarias.append(OP)
        matriz.append(linha)            
    if i ==4:
        for posicao,valor in enumerate(v_op_bancarias):
            if valor == 'C':
                v_novo_saldo.append(v_saldo[posicao]+v_valores_random[posicao])
            if valor == 'D':
                v_novo_saldo.append(v_saldo[posicao]-v_valores_random[posicao])
        matriz.append(v_novo_saldo)

for i in range (5):
    print (matriz[i])
