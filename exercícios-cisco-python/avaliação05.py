list = []
n = int(input("Digite um número:"))
x = 0
a = 0
while a < n:
    i = int(input("Informe um número:"))
    list.append(i)
    a += 1
for j in list:
    print()
    print('Tabuada: {}'.format(j))
    for x in range(21):
        print('\n{} x {} = {}'.format(x, j, x*j))
        print()
