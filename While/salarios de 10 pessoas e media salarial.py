

contador= 0
while contador<10:
    salario= float(input('Qual o seu salário?' + '\n'))
    if contador == 0:
        maior_salario=salario
        menor_salario=salario
    
    if salario<1500:
        imposto_de_renda=0        
    if (1500<salario<=2000):
        imposto_de_renda=(salario*0.10)    
    if salario>2000:
        imposto_de_renda=(salario*0.15)
    
    salario_liquido=salario-imposto_de_renda

    print('o valor do imposto de renda é de', imposto_de_renda, '\n' + 'e o salário líquido a receber é', salario_liquido)

    if maior_salario<salario:
        maior_salario=salario
    if menor_salario>salario:
        menor_salario=salario

    if contador== 0:
        salario1=salario
    if contador== 1:
        salario2=salario
    if contador == 2:
        salario3=salario
    if contador== 3:
        salario4=salario
    if contador == 4:
        salario5=salario
    if contador == 5:
        salario6=salario
    if contador ==6:
        salario7=salario
    if contador == 7:
        salario8=salario
    if contador == 8:
        salario9=salario
    if contador == 9:
        salario10=salario
   
    contador +=1

media_salarial=(salario1+salario2+salario3+salario4+salario5+salario6+salario7+salario8+salario9+salario10)/10

print('o maior salário é:', maior_salario, '\n' + 'o menor salário é', menor_salario)
print('a média salarial é', media_salarial)
