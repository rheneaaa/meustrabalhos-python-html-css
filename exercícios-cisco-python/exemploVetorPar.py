lista = []
par = []
impar = []

numero = int(input('Digite um numero: '))
resto = numero % 2

for i in range(20):
    valor = int(input('Digite um número: '))
    lista.append(valor)
par = ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20']
impar = ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19']
total = 0

print(lista)
for i in lista:
    if i not in par:
        total += 1
print('')