n1 = float(input('Digite o valor normal: R$'))
des = (n1 * 0.05)
res = n1 - des
print('O preço com 5% de desconto é de R${:.2f}'.format(res))

# Simplificado
preço = float(input('Digite o valor normal: R$'))
novo = preço - (preço * 5 / 100)
print('O preço com 5% de desconto é de R${:.2f}'.format(novo))
