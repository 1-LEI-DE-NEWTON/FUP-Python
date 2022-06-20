
from random import randint
vetor_10 = []
vetor_pares = []
while len(vetor_10)<10:
    vetor_10.append(randint(2,60))
print(vetor_10)

for posição,numero in enumerate(vetor_10):
    if numero % 2 == 0:
        vetor_pares.append(numero) 

print(vetor_pares)
print(sorted(vetor_pares, reverse= True))
