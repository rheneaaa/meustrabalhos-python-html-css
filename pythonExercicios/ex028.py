from random import randint
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
des = int(input('Em que número pensei? '))
if des == pc:
    print('Parabéns, você acertou!!!')
else:
    print('GANHEI!!! Eu pensei no número {} e não no {}.'.format(pc, des))
