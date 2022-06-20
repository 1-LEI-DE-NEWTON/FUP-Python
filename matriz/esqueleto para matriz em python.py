
matriz = []
for i in range (3):
    linha = []
    for j in range (3):
        linha.append(int(input('digite o valor do termo [' + str(i) + ',' + str(j) + ']:' + '\n')))
    matriz.append(linha)
for i in range (3):
    print (matriz[i])
