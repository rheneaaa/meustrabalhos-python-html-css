hat_list = [1, 2, 3, 4, 5]
print(hat_list)
n1 = int(input('Digite um número: '))
hat_list[2] = n1
print('Nova lista: ', hat_list)
del hat_list[-1]
print('Novo conteúdo da lista: {}.\nComprimento da nova lista é {}'.format(hat_list, len(hat_list)))
