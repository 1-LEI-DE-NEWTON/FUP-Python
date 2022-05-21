
texto=f'informe um numero aleatoriamente'

n1=int(input(f'{texto}' + '\n'))
n2=int(input(f'{texto}' + '\n'))
n3=int(input(f'{texto}' + '\n'))
n4=int(input(f'{texto}' + '\n'))
n5=int(input(f'{texto}' + '\n'))
n6=int(input(f'{texto}' + '\n'))
n7=int(input(f'{texto}' + '\n'))
n8=int(input(f'{texto}' + '\n'))
n9=int(input(f'{texto}' + '\n'))
n10=int(input(f'{texto}' + '\n'))

numeros=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
print('numeros agrupados em ordem crescente:', sorted(numeros))
numeros.sort()
numeros.reverse()
print('numero agrupados em ordem decrescente:', numeros)