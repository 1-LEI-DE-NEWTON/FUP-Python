
matriz = []
diagonal_p = []
diagonal_s = []

def soma_diagonal_matriz():
    
    for i in range (3):
        linha = []
        for j in range(3):
            linha.append(int(input('Informe o valor da posição [' + str(i) + ',' + str(j) + ']:')))
        matriz.append(linha)

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
    
    soma_diagonal_p = sum(diagonal_p)
    soma_diagonal_s = sum(diagonal_s)
    soma_diagonais = soma_diagonal_p+soma_diagonal_s
    
    print('a matriz obtida foi: ')
    
    for i in range (3):
        print(matriz[i])

    print('\n')
    print('a soma da diagonal principal é: ', soma_diagonal_p)
    print('a soma da diagonal secundária é: ', soma_diagonal_s)
    print('a soma da diagonal principal + a diagonal secundária é: ', soma_diagonais)

soma_diagonal_matriz()
