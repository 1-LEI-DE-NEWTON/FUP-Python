def serie_fibonacci():
    termo = 12
    ultimo_numero = 1
    penultimo_numero = 1
    contador = 3

    while contador <= termo:
        fibonacci = ultimo_numero + penultimo_numero
        penultimo_numero = ultimo_numero
        ultimo_numero = fibonacci
        contador = contador+1
    print(fibonacci)

serie_fibonacci()