lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
total = 0
print(lista)
print()
for i in lista:
    if i not in vogais:
        total += 1
    print(i)
print()
print('Total de consoantes: ', total)
