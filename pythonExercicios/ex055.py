maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso {}: '.format(i)))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))