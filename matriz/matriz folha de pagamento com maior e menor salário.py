
maior_salario=0
menor_salario=0
matriz = []
v_salarios = []

for i in range (4):
    linha = []
    if i == 0:
        for j in range (3):
            linha.append(int(input('informe a sua matrícula' + '\n')))
        matriz.append(linha)
    if i == 1:
        for j in range (3):
            linha.append(input('informe o seu nome' + '\n'))
        matriz.append(linha)
    if i == 2:
        for j in range (3):
            linha.append(input('informe a sua função' + '\n'))
        matriz.append(linha)
    if i == 3:
        for j in range (3):
            salario = input('informe o seu salário' + '\n')
            linha.append(salario)
            v_salarios.append(salario)
        matriz.append(linha)

for i in range (4):
    print (matriz[i])
tamanho = len(v_salarios)
v_salarios.sort()
maior_salario=v_salarios[tamanho-1]
menor_salario=v_salarios[0]
print('o maior salário é: ', maior_salario, ' e o menor salário é :', menor_salario)
