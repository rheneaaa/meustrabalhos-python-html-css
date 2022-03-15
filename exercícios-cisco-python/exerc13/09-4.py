largura = int(input('Digite a largura: '))
altura = int(input('DIgite a altura: '))
print('#' * largura)

for i in range(altura - 2):
    print('#' + ' ' * (largura - 2) + '#')

print('#' * largura)