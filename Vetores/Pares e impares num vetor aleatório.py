
quantidade_par = 0
quantidade_impar = 0
from random import randint
vetor_10 = []
vetor_pares = []
while len(vetor_10)<10:
    vetor_10.append(randint(2,60))
print(vetor_10)

for posição,numero in enumerate(vetor_10):
    if numero % 2 == 0:
        quantidade_par+=1
    if not numero % 2 == 0:
        quantidade_impar+=1

print('existem {0} numeros impares no vetor e {1} numeros pares no vetor'.format(quantidade_impar,quantidade_par))
