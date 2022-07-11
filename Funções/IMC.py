
peso = float(input('Informe o seu peso '))
altura = float(input('Informe a sua altura '))

def classificão_IMC(peso,altura):
    imc = peso / (altura ** 2)
    print ('Seu IMC é: ', imc)
    if imc<18.5:
        print('Magreza, obesidade grau 0')
    elif imc>=18.5 and imc<=24.9:
        print('Normal, obesidade grau 0')
    elif imc>=25 and imc<=29.9:
        print('Sobrepeso, obesidade grau 1')
    elif imc>=30 and imc<=39.9:
        print('Obesidade de grau 3')
    elif imc>=40:
        print('Obesidade grave de grau 4')
    else:
        print('Valor inválido')

classificão_IMC(peso,altura)
