meses = ['Janeiro', 'Fevereiro', 'Março']
temp = []
valor = 0
soma = 0
media = 0

for i in range(3):
    valor = float(input('Digite a temperatura do mês de ' + meses[i] + ':'))
    temp.append(valor)

for i in range (3):
    soma += temp[i]

media = soma / 3
print('A média da temperatura do ano é: ', media)

print('\nOs meses que tiveram temperatura acima da média são: ')
for i in range(3):
    if temp[i] > media:
        print(meses[i], 'com', temp[i], 'graus')
