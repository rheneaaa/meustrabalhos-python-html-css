
casa = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe seu salário: R$'))
anos = int(input('Informe quantos anos deseja pagar: R$'))
res = casa / (anos * 12)
minimo = sal * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, aprestação será R${:.2f}'.format(casa, anos, res))
if res <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')
