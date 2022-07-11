
import datetime

def calculo_data_em_dias():
    dia = int(input('Informe o dia: '))
    mês = int(input('Informe o mês, em números: '))
    ano = int(input('Informe o ano: '))

    data_inicial = datetime.datetime(ano, mês, dia)
    data_atual = datetime.datetime.today()
    diff = (data_atual-data_inicial).days
    
    print(f'A diferença entre as datas é de {diff} dia(s)')
    return diff
calculo_data_em_dias()
