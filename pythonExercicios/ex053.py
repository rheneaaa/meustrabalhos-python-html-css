frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inver de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não é!')

    # Outro exemplo sem for
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não é!')