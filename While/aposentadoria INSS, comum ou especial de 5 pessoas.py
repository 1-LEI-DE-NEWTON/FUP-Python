
contador=0

while contador<6:

    nome=input('informe seu nome' + '\n')
    ano_nasc=int(input('informe o seu ano de nascimento' + '\n'))
    idade=2022-ano_nasc
    sexo=input('Qual o seu sexo? (masculino ou feminino)' + '\n')
    tempo_trabalho=int(input('informe o seu numero de anos de contribuição'+ '\n'))
    status=input('informe o seu status (comum ou especial)' + '\n')

    if (sexo== 'masculino') and (idade>=65) and (tempo_trabalho>=35) and (status== 'comum'):
        print(' nome:', nome, '\n', sexo, idade, 'anos', '\n' ' Apto para aposentadoria')
    elif (sexo== 'feminino') and (idade>=60) and (tempo_trabalho>=30) and (status== 'comum'):
        print(' nome:', nome, '\n', sexo, idade, 'anos', '\n' ' Apta para aposentadoria')
    elif (sexo== 'masculino') and (idade>=60) and (tempo_trabalho>=30) and (status== 'especial'):
        print(' nome:', nome, '\n', sexo, idade, 'anos', '\n' ' Apto para aposentadoria')
    elif (sexo== 'feminino') and (idade>=55) and (tempo_trabalho>=25) and (status== 'especial'):
        print(' nome:', nome, '\n', sexo, idade, 'anos', '\n' ' Apta para aposentadoria')
    else:
        if sexo== 'masculino':
            print('Não apto para aposentadoria')
        if sexo== 'feminino':
            print('Não apta para aposentadoria')
    contador+=1