

def busca(lista, item):
    for n in lista:
        if n == item:
            return True
    return False
    
lista = []
while True:
    n = int(input('Informe um número inteiro: '))
    if n == 0:
        break
    lista.append(n)
print(lista)

item = int(input('Informe um número para buscar na lista: '))
if busca(lista, item):
    print('O número está contido na lista')
else:
    print(f'O número {item} não está contido na lista')