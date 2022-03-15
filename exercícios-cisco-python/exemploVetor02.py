lista = []

for i in range(10):
    valor = input('Digite um caracter: ')
    lista.append(valor)
vogais = ['a', 'e', 'i', 'o', 'u']
total = 0

print(lista)
for i in lista:
    if i not in vogais:
        total += 1
print('Total de consoantes: ', total)
