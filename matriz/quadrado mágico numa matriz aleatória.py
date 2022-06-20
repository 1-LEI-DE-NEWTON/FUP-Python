
from random import randint

matriz_transposta = []
matriz = []
diagonal_p = []
diagonal_s = []
soma_linhas = False
soma_colunas = False
soma_diagonais = False

for i in range (3):
    linha = []
    for j in range (3):
        valor = randint(1,2)
        linha.append(valor)
    matriz.append(linha)

for i in range (3):
    coluna = []
    for j in range (3):
        valor_coluna = matriz[j][i]
        coluna.append(valor_coluna)
    matriz_transposta.append(coluna)

for i in range (3):
    for j in range (3):
        if i == j:
            diagonalp = matriz [i][j]
    diagonal_p.append(diagonalp)

for i in range (3):
    for j in range (3):
        if i+j == 2:
            diagonals = matriz [i][j]
    diagonal_s.append(diagonals)

for k in range (3):
    if sum(matriz[k]) == sum(matriz_transposta[k]):
        soma_linhas_colunas = True

if sum(matriz[0]) == sum(matriz[1]) == sum(matriz[2]):
    soma_linhas = True
if sum(matriz_transposta[0]) == sum(matriz_transposta[1]) == sum(matriz_transposta[2]):
    soma_colunas = True
if sum(diagonal_p) == sum(diagonal_s):
    soma_diagonais = True

if soma_colunas == True and soma_diagonais == True and soma_linhas == True and soma_linhas_colunas == True:
    print('É uma matriz quadrado mágico')
else:
    print('Não é uma matriz quadrado mágico')

for i in range (3):
    print (matriz[i])
