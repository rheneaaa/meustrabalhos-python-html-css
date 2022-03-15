opcao = 0
while opcao != 3:
    print('''Menu de opções:
    [ 1 ] Imposto
    [ 2 ] Novo salário
    [ 3 ] Classificação''')
    opcao = float(input('Digite a posição desejada? '))
    v1 = float(input('Digite o salário: '))
    if opcao == 1:
        if v1 < 500:
            menor = v1 - (v1 * 5 / 100)
            print('O imposto com salário de R${} vai ter 5% de imposto e vai ficar R${}'.format(v1, menor))
        if 500 <= v1 <= 850:
            medio = v1 - (v1 * 10 / 100)
            print('O imposto com salário de R${} vai ter 10% de imposto e vai ficar R${}'.format(v1, medio))
        if v1 > 850:
            acima = v1 - (v1 * 15 / 100)
            print('O imposto com salário acima de R$850,00 tem 15% de imposto e vai ficar R${}'.format(acima))
    if opcao == 2:
        if v1 > 1500:
            m = v1 + 25
            print('O seu novo salário com aumento de R$25,00 será R${},00'.format(m))
        if 750 <= v1 <= 1500:
            m1 = v1 + 50
            print('O seu novo salário com aumento de R$50,00 será R${},00'.format(m1))
        if 450 <= v1 < 750:
            m2 = v1 + 75
            print('O seu novo salário com aumento de R$75,00 será R${},00'.format(m2))
        if v1 < 450:
            m3 = v1 + 100
            print('O seu novo salário com aumento de R$100,00 será R${},00'.format(m3))




