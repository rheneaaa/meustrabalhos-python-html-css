valor = float(input('Qual o valor do produto? R$ '))
print('''Escolha a opção de pagamento:
[ 1 ] à vista no dinheiro e cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opçao = int(input('Opção: '))
n1 = valor - (valor * 10 / 100)
n2 = valor - (valor * 5 / 100)
n3 = valor
n4 = valor + (valor * 20 / 100)
if opçao == 1:
    print('O valor a ser pago é R${:.2f}'.format(n1))
elif opçao == 2:
    print('O valor a ser pago é R${:.2f}'.format(n2))
elif opçao == 3:
    parcela = valor / 2
    print('O valor parcelado será de 2x de R${:.2f}'.format(parcela))
    print('O valor a ser pago é R${:.2f}'.format(n3))
elif opçao == 4:
    parce = int(input(('Quantas parcelas? ')))
    parc = n4 / parce
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(parce, parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, (parc * parce)))
