
numero = int(input('Informe o valor para sacar acima de R$ 4,00: '))

def contagem_de_notas(numero):
    while numero<4:
        print('Valor abaixo do permitido')
        numero = int(input('Informe o valor para sacar acima de R$ 4,00: '))

    cédulas = [2, 5, 10, 20, 50, 100, 200]
    cédulas.reverse()

    for posição,valor in enumerate(cédulas):
        if numero>=valor:  
            if numero == 6:
                quantidade = numero//2
                print(f'{quantidade} nota(s) de R$ 2')
                numero -= quantidade*valor
            elif numero == 8:
                quantidade = numero//2
                print(f'{quantidade} nota(s) de R$ 2')
                numero -= quantidade*valor      
            elif numero == 11:
                quantidade = (numero-5)//5
                numero = numero-5
                print(f'{quantidade} nota(s) de R$ 5')
                quantidade = numero//2
                print(f'{quantidade} nota(s) de R$ 2')
                numero -= quantidade*valor
            elif numero == 13:
                quantidade = (numero-5)//5
                numero = numero-5
                print(f'{quantidade} nota(s) de R$ 5')
                quantidade = numero//2
                print(f'{quantidade} nota(s) de R$ 2')
                numero -= quantidade*valor                        
            else:
                quantidade = numero//valor
                numero = numero % valor
                print('{0} cédulas de R${1}'.format(quantidade,valor))
contagem_de_notas(numero)
