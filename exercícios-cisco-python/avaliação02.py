notas = []
atleta = input('Digite o nome da atleta: ')
x = float(input('Digite uma nota: '))
maior = 0
menor = 0
soma = 0
media = 0
for i in range(7):
    i = float(input('Digite uma nota: '))
    notas.append(i)
    maior = max(notas)
    menor = min(notas)
    for j in notas:
        soma += j
media = (soma-maior-menor)/5
print()
print('Atleta: {}'.format(atleta))
for x in notas:
    print('Nota: {}'.format(x))
print()
print('Resultado final:')
print('Atleta:{}'.format(atleta))
print('Maior valor {}'.format(maior))
print('Menor valor {}'.format(menor))
print('Média:{:.1f}'.format(media))
