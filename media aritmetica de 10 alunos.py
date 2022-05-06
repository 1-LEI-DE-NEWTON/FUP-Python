
contador=0

while contador<10:
    
    nota_1= float(input('informe a nota do primeiro semestre' +'\n'))
    nota_2= float(input('informe a nota do segundo semestre' +'\n'))
    nota_3= float(input('informe a nota do terceiro semestre' +'\n'))
    media_simples=(nota_1+nota_2+nota_3)/3

    if media_simples>=7:
        print ('Aprovado')
    if (4<=media_simples<=6.9):
        print('AF')
    if media_simples<4:
        print('Reprovado')

    if contador== 0:
        aluno1=media_simples
    if contador== 1:
        aluno2=media_simples
    if contador == 2:
        aluno3=media_simples
    if contador== 3:
        aluno4=media_simples
    if contador == 4:
        aluno5=media_simples
    if contador == 5:
        aluno6=media_simples
    if contador ==6:
        aluno7=media_simples
    if contador == 7:
        aluno8=media_simples
    if contador == 8:
        aluno9=media_simples
    if contador == 9:
        aluno10=media_simples

    
    contador +=1   
media_geral= (aluno1+aluno2+aluno3+aluno4+aluno5+aluno6+aluno7+aluno8+aluno9+aluno10)/10
print('a média geral foi de', media_geral)



