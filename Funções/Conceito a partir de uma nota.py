
media_final = float(input('informe a média final: '))

def conceito_por_media_final(media_final):
    if (0<=media_final<=4.9):
        print('Conceito D')
    elif (5<=media_final<=6.9):
        print ('Conceito C')
    elif (7<=media_final<=8.9):
        print ('Conceito B')
    elif (9<=media_final<=10):
        print ('Conceito A')
conceito_por_media_final(media_final)
