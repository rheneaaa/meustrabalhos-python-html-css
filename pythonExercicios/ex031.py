n1 = float(input('Digite o preço da passagem: '))
if n1 <= 200:
    preço = n1 * 0.50
else:
    preço = n1 * 0.45
print('A passagem custará R${:.2f}'.format(preço))
