'''
Percorrer uma lista de números inteiros e contar a quantidade de números pares.
'''

# preenche uma lista
lista = []
for i in range(10):     # preenche uma lista com 10 numeros
    numero = int(input('Numero: '))
    lista.append(numero)
print(lista)

# percorrer os itens da lista
cont = 0
for item in lista:
    if item % 2 == 0:   # verifica se o numero é par
        cont += 1       # incrementa o contador
print(f'Quantidade de numeros pares: {cont}')
