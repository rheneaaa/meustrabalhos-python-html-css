from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input('Digite a data {}: '.format(i)))
    idade = atual - ano

    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores'.format(maior))
print('Ao todo tivemos {} pessoas menores'.format(menor))

