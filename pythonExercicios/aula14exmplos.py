preço = int(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('Opção 1 - à vista no dinheiro ou cheque , 10% de desconto')
print('Opção 2 - à vista no cartão, 5% de desconto')
print('Opção 3 - em até 2x no cartão, preço normal')
print('Opção 4 - 3x ou mais no cartão: 20% de juros')

pag = int(input('Escolha sua opção de pagamento: '))

op1 = preço - (preço * 10 / 100)
op2 = preço - (preço * 5 / 100)
op3 = preço
op4 = preço + (preço * 20 / 100)

if pag == 1:
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, op1))
elif pag == 2:
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, op2))
elif pag == 3:
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, op3))
else:
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, op4))

