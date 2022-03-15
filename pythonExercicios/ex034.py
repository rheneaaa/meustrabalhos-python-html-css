sal = float(input('Qual o valor do seu salário? R$'))
if sal <= 1250:
    perc = sal + (sal * 15 / 100)
else:
    perc = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal, perc))
