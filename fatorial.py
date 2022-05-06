
def fatorial(x):
    return 1 if (x==1 or x==0) else x * fatorial(x-1)
numero= int(input('informe o número para cálculo do seu fatorial' + '\n'))
print('o fatorial de ', numero, 'é:', fatorial(numero))    

