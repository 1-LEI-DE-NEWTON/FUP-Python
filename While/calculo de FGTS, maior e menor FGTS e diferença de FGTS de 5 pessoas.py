
reais='reais'
contador = 0
dif='A diferença de valores do FGTS do maior pelo menor após 1 ano é de:'

while contador<6:
    salario=int(input('informe seu salario' + '\n'))
    fgts=(salario*0.085)
    print('Voce possui', fgts, 'de fgts' +'\n')

    if contador == 0:
        maior_fgts=fgts
        menor_fgts=fgts

    if maior_fgts<fgts:
        maior_fgts=fgts
    if menor_fgts>fgts:
        menor_fgts=fgts
    dif_1ano=(maior_fgts*12)-(menor_fgts*12)
    contador+=1
print('o maior FGTS é:', maior_fgts, f'{reais}' '\n' + 'e o menor FGTS é:', menor_fgts, f'{reais}')
print(f'{dif}', dif_1ano)
