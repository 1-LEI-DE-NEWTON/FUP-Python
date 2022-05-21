
Quantidade_Maça=int(input('informe o numero de maças a ser comprado' + '\n'))

if Quantidade_Maça<12:
    Preço_Maça=1.30
else:
    Preço_Maça=1.0
ValorTotal=Preço_Maça*Quantidade_Maça
print('Custo total da compra=', ValorTotal, 'reais')
