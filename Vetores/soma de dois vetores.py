x = 2
y = 20
z = 10
lista_pares = [] 
lista_numeros = []
for i in range(x,y+1): 
    if i % 2 == 0: 
        w=i**2
        lista_pares.append(w) 
print(lista_pares)

while z<=19:
    lista_numeros.append(z)
    z+=1
print(lista_numeros)
soma_vetores = []
for k,o in zip (lista_numeros, lista_pares):
    soma_vetores.append (k+o)
print (soma_vetores)
