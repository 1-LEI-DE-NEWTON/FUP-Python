
contador=1
salario_menor=0

while contador<6:
    salario=int(input('Quanto é o seu salário?' '\n'))
    num_filhos=int(input('Quantos filhos voce tem?' '\n'))

    if contador == 1:
        salario1=salario
        filho1=num_filhos
        if salario<1000:
            salario_menor+=1
    if contador == 2:
        salario2=salario
        filho2=num_filhos
        if salario<1000:
            salario_menor+=1
    if contador == 3:
        salario3=salario
        filho3=num_filhos
        if salario<1000:
            salario_menor+=1
    if contador == 4:
        salario4=salario
        filho4=num_filhos
        if salario<1000:
            salario_menor+=1
    if contador == 5:
        salario5=salario
        filho5=num_filhos
        if salario<1000:
            salario_menor+=1
    contador+=1

media_salarial=(salario1+salario2+salario3+salario4+salario5)/5
media_filhos=(filho1+filho2+filho3+filho4+filho5)/5
percentual=(salario_menor*100)/5

print('a média salarial é de', media_salarial, '\n')
print('a média de filhos é de', media_filhos, '\n')
print('o percentual de pessoas com salário abaixo de mil reais é de', percentual, '%' ,'dos habitantes')