x = 0
x = int(input("Digite um valor: "))
while x != 0:
    if (x % 2 == 0):
        print(x, "é par")
    else:
        print(x, "é impar")
    x = int(input("Digite um valor: "))

print("Você digitou ZERO para sair do programa")