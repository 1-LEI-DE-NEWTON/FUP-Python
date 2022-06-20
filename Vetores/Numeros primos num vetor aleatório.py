
from random import randint
vetor_10 = []
while len(vetor_10)<10:
    vetor_10.append(randint(2,60))
print(vetor_10)

def numeros_primos(numero):
    for resto in range(2,numero):
        if (numero % resto == 0):    
            return False
    return True
            
for posição,numero in enumerate(vetor_10):
    if numeros_primos(numero):
        print(f'O numero {numero} é primo e esta na posição {posição} do vetor.')
