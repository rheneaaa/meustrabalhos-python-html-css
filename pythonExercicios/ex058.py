from random import randint
pc = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 10.')
print('Será que consegue adivinhar? ')
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas.'.format(palpites))
