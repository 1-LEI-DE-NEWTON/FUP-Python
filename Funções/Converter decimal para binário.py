
def converter(n, base):
    result = expoente = 0
    while n > 0:
        n, digito = divmod(n, base)
        result += (10 ** expoente) * digito
        expoente += 1
    return result

decimal = int(input('Digite um numero: '))
print(converter(decimal, 2))
