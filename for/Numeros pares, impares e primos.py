
numero = 50
Par = 0
Impar = 0
quantidade_primo=0
for numero in range(50,100):
    primo = True
    for resto in range(2,numero-1):
        if (numero % resto == 0):    
            primo = False
        elif (primo == True):
            quantidade_primo +=1
        if numero % 2 == 0:
            Par = Par + 1
        else:
            Impar = Impar + 1
print('A quantidade de números primos é: ', quantidade_primo)
print('A quantidade de números pares é: ', Par)
print('A quantidade de números ímpares é: ', Impar) 
