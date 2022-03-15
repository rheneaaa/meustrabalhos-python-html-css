n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
print('Tirando {:.1f}, {:.1f}, {:.1f}, {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, n3, n4, media))
if media >= 9:
    print('A - APROVADO')
elif 9 > media >=7.5:
    print('B - APROVADO')
elif 7.5 > media >= 6:
    print('C - APROVADO')
elif 6 > media >= 4:
    print('D - REPROVADO')
elif 4 > media:
    print('E - REPROVADO')