
contador=0
while contador<10:
    peso= float(input('informe o peso'))
    altura= float(input('informe a altura'))
    IMC= peso/altura

    if IMC<18.5:
        print('abaixo do peso ideal')
    elif 18.5>IMC<24.9:
        print('peso ideal')
    elif 25<IMC<29.9:
        print('sobrepeso')
    elif 30<IMC<34.9:
        print ('obesidade grau I')
    elif 35<IMC<39.9:
        print ('obesidade grau II')
    elif IMC>=40:
        print('obesidade grau III')
contador+=1
