
matriz = []
v_notas = []
v_cursos = []
v_situacao = []
numero_comp, numero_inf, numero_red, aprovados, reprovados = 0, 0, 0, 0, 0

for i in range (4):
    linha = []
    if i == 0:
        for j in range (7):
            linha.append(input('informe o seu nome' + '\n'))
        matriz.append(linha)
    if i == 1:
        for j in range (7):
            nota = (int(input('informe a sua nota' + '\n')))
            while (1>nota or nota>11):
                print('Nota invalida, digite um numero entre 1 e 10')
                nota = (int(input('informe a sua nota' + '\n')))
            linha.append(nota)
            v_notas.append(nota)
        matriz.append(linha)
    if i == 2:
        for j in range (7):
            curso = (input('informe o seu curso' + '\n'))
            linha.append(curso)
            v_cursos.append(curso)
        matriz.append(linha)
    if i == 3:
        for j in range (7):
            situação = (input('informe a sua situação' + '\n'))
            linha.append(situação)
            v_situacao.append(situação)
        matriz.append(linha)

for i in range (4):
    print (matriz[i])
media_geral = sum(v_notas)/len(v_notas)
print('A média geral é: ', media_geral)

for posicao, str in enumerate(v_cursos):
    if str == 'Computação':
        numero_comp = numero_comp + 1
    if str == 'Informática':
        numero_inf = numero_inf + 1
    if str == 'Redes':
        numero_red = numero_red + 1

for posicao, str in enumerate(v_situacao):
    if str == 'Aprovado':
        aprovados = aprovados + 1
    if str == 'Reprovado':
        reprovados = reprovados + 1

print('O número de alunos do curso de Computação é: ', numero_comp)
print('O número de alunos do curso de Informática é: ', numero_inf)
print('O número de alunos do curso de Redes é: ', numero_red)

print('O número de alunos aprovados é: ', aprovados)
print('O número de alunos reprovados é: ', reprovados)

percentual_arprovados = (aprovados/(len(v_situacao)))*100
percentual_reprovados = (reprovados/(len(v_situacao)))*100

print('O percentual de alunos aprovados é: ', "%.2f" % percentual_arprovados, '%')
print('O percentual de alunos reprovados é: ', "%.2f" % percentual_reprovados, '%')

maior_nota = max(v_notas)
print ('A maior nota é: ', maior_nota)

for posicao, numero in enumerate(v_notas):
    if numero == maior_nota:
        print('O aluno com maior nota é: ', matriz[0][posicao])
        print('O curso do aluno com maior nota é: ', matriz[2][posicao])
        print('A situação do aluno com maior nota é: ', matriz[3][posicao])
