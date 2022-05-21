

Horas_Mensal=160
contador=1

while contador<11:
    print('funcionário', contador)
    Horas_Trabalhadas=int(input('informe quantas horas foram trabalhadas durante este mês' + '\n'))
    Salario_Hora=int(input('Informe o salário por hora trabalhada' +'\n'))
    if contador==1:
        Maior_Hora=Horas_Trabalhadas
        FuncionarioH=1

    if Horas_Trabalhadas>Horas_Mensal:
        Horas_Extras_Trabalhadas=Horas_Trabalhadas-Horas_Mensal
        Hora_extra=Salario_Hora+(Salario_Hora*0.50)
        Salario_Mensal=Salario_Hora*Horas_Trabalhadas
        Salario_Extra=Hora_extra*Horas_Extras_Trabalhadas
        Salario_Total=Salario_Extra+Salario_Mensal
        print('Salário total a receber é:', Salario_Total, 'reais')
        
    if Maior_Hora<Horas_Trabalhadas:
        Maior_Hora=Horas_Trabalhadas
        FuncionarioH=contador
    
    if Horas_Trabalhadas<=Horas_Mensal:
        Salario_Mensal=Salario_Hora*Horas_Trabalhadas
        print('Salário a receber é:', Salario_Mensal, 'reais')
    contador+=1    
print('Quem mais trabalhou foi o funcionario:', FuncionarioH)

