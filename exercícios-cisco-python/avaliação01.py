def calc(n):
    n = ((n / total) * 100)
    return n


jogadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total = 0

print('Enquete: Quem foi o melhor jogador?')
voto = int(input('Número do jogador (0=fim): '))

while voto != 0:
    if 1 <= voto <= 23:
        jogadores[voto - 1] += 1
        total += 1
    else:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    voto = int(input('Número do jogador (0=fim): '))

melhor = 0
# maior = jogadores.max()
for v in jogadores:
    if v > melhor:
        melhor = v
posi = jogadores.index(melhor) + 1

print('Resultado da votação:')
print('Foram computados', total, 'votos.')
print('\nJogador votos % ')
for i in range(23):
    if jogadores[i] > 0:
        print(i + 1, '     ', jogadores[i], '     ', round(calc(jogadores[i]), 2), '%')

print('O melhor jogador foi o número {} com {} votos, correspondendo a {}% do total de votos'.format(posi, melhor, round(calc(melhor), 2)))
