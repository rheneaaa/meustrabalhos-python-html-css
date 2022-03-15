n = int(input('Digite um número para saber se é primo: '))
mult = 0

for count in range(2, n):
    if (n % count == 0):
        print('Múltiplo de', count)
        mult += 1

if mult == 0:
    print('É primo')
else:
    print('Não é primo')