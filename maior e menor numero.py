
def questao1():
    contador= 1
    while contador<11:
        numero= int(input('informe 10 numeros inteiros aleatoriamente' + '\n'))
        if contador == 1:
            maior_numero=numero
            menor_numero=numero
        if maior_numero<numero:
            maior_numero=numero
        if menor_numero>numero:
            menor_numero=numero
        contador= contador+1
    print('o maior número é', maior_numero, 'e o menor número é', menor_numero)
questao1()   
