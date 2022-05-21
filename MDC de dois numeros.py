

numero1 = int(input('informe o primeiro numero' + '\n'))
numero2 = int(input('informe o segundo numero ' + '\n'))
while numero2!=0:
    resto = numero1 % numero2
    numero1 = numero2
    numero2 = resto
mdc=numero1
print('o mdc é igual a:', mdc)
