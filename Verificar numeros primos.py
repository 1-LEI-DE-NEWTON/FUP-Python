
def numeros_primos():
    quantidade=0
    contador= 0
    while contador<10:
        numero= int(input('digite o numero' + '\n'))
        primo = True
        for resto in range(2,numero-1):
            if (numero % resto == 0):    
             primo = False
        if (primo == True):
            print('é primo')
            quantidade +=1
        else:
            print ('não é primo')
        contador +=1
    print('você digitou', quantidade, 'numero primos')
numeros_primos()
