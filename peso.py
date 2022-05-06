
contador=0
while contador<10:
    peso= int(input('informe o peso'))
    altura= int(input('informe a altura'))
    novidade= peso/altura

    if novidade<18.5:
        print('abaixo do peso ideal')
    elif 18.5>novidade<24.9:
        print('peso ideal')
    elif 25<novidade<29.9:
        print('sobrepeso')
    elif 30<novidade<34.9:
        print ('obesidade grau I')
    elif 35<novidade<39.9:
        print ('obesidade grau II')
    elif novidade>=40:
        print('obesidade grau III')
contador+=1
