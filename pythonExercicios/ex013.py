sal = float(input('Digite o salário do funcionário: '))
no = (sal * 0.15) + sal
print('Seu novo salário é de R${:.2f}'.format(no))

# Simplificado
sal = float(input('Digite o salário do funcionário: '))
no = sal + (sal * 15 / 100)
print('Seu novo salário é de R${:.2f}'.format(no))