

contador=0

while contador<10:
    data_de_nascimento= int(input('informe o ano de nascimento' + '\n'))
    idade= 2022-data_de_nascimento
    if contador == 0:
        mais_velho= idade
        jovem= idade
    if mais_velho<idade:
        mais_velho=idade
    if jovem>idade:
        jovem=idade
    print('voce tem', idade, 'anos')
    contador += 1
print('o mais velho tem', mais_velho, 'anos')
print('o mais novo tem', jovem, 'anos')

