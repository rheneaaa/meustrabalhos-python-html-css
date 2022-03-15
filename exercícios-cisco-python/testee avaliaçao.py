# variaveis
media = 0 # inteiro
menor_maior = [] # lista

# repete 10x
for num in range(10):
    num = input('Digite um numero: ') # pega inteiro do teclado
    menor_maior.append(num)           # adiciona num a lista
    media += num                      # soma a media mais o numero

menor_maior.sort()                    # organiza a lista em ordem crescente

print('\nO menor numero {}:\nE o maior nmero:{}'.format(menor_maior[0], menor_maior[-1]))
# menor_maior[0] = pega o primeiro elemento da lista
# e menor_maior[-1] = pega o ultimo elemento da lista

print('A media \x82: %s\n' % (float(media) / 10)) # calcula a media

raw_input()# espera Enter pra encerrar