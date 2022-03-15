n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('O aluno está em EXAME.')
elif media < 7:
    print('O aluno está REPROVADO.')
elif 10 > media >= 7:
    print('O aluno está APROVADO.')
elif media == 10:
    print('APROVADO COM DISTINÇÃO.')