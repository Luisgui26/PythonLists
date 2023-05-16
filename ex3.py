lista1 = []
lista2 =[]
for i in range(10):
    num = int(input('Número: '))
    if num % 2 == 0:
        lista1.append(num)
    else:
        lista2.append(num)

print(lista1)
print(lista2)