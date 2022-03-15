from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Menu
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua posição? '))
    if opcao == 1:
        soma = v1 + v2
        print('{} + {} é igual a {}'.format(v1, v2, soma))
    elif opcao == 2:
        mult = v1 * v2
        print('{} x {} é igual a {}'.format(v1, v2, mult))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(3)
print('Fim')
