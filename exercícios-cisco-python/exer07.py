ncarros = int(input('Digite o total de carros: '))
totv = int(input('Digite o total de vendas: '))
salf = int(input('Digite o salário fixo: '))
com = int(input('Digite sua comissão: '))
salfi = (ncarros*com)+(totv*0.05)+salf
print('O salário final é: ', salfi)
