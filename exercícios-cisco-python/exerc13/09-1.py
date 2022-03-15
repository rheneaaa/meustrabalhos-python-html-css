lista = []
soma = 0
media = 0
cont = 0
cmedia = 0
c7 = 0
nota = int(input("Digite uma nota: "))

while nota != -1:
    lista.append(nota)
    soma += nota
    cont += 1

    nota = int(input("Digite uma nota: "))

media = soma / cont

print("\n###Resultados###")
print("Quantidade de valores lidos: ", cont)
print("Ordem dos valores: ")
for i in lista:
    if i > media:
        cmedia += 1
    if i < 7:
        c7 += 1
    print(i, end=" ")

print("\nOrdem inversa dos valores: ")
for i in reversed(lista):
    print(i)

print("Soma das notas: ", soma)
print("Média das notas: ", media)
print("Quantidade de notas acima da média: ", cmedia)
print("Quantidade de notas abaixo de 7: ", c7)
print("Obrigado pela atenção")

#print(lista)
