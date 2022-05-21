
d_percurso1=int(input('informe a distancia de um lugar para o outro no percurso 1, em km' + '\n'))
d_percurso2=int(input('informe a distancia de um lugar para o outro no percurso 2, em km' + '\n'))

if d_percurso1<d_percurso2:
    print('o percurso 1 é o menor percurso')
    print('o consumo de gasolina neste percurso é de', (d_percurso1/12), 'litros de gasolina, para um consumo de 12km/L')
else:
    print ('o percurso 2 é o menor percurso')
    print('o consumo de gasolina neste percurso é de', (d_percurso2/12), 'litros de gasolina, para um consumo de 12km/L')