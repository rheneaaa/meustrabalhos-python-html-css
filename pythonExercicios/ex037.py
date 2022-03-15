num = int(input('Digite um número inteiro: '))
opçao = int(input('Escolha uma das bases para conversão:\n[ 1 ] - binário\n[ 2 ] - octal\n[ 3 ] - hexadecimal\nSua opção:  '))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEZADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA!')