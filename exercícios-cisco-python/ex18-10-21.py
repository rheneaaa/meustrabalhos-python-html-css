# exemplo 1
arq = open("senai.txt","r+")
arq.write("oi")
linha = arq.readline()
print(linha)
arq.close()

# exemplo 2
a2 = open("tecnico.txt", "a")
a2.write("Tecnico em Des. Sistemas\n")
a2.close()

# exemplo 3
a3 = open("nomes.txt", "r")
for i in a3:
    print(i)
a3.close()

# exemplo 4
arq = open('nomes.txt', 'r')
linha = arq.read()
a = linha.split()
print(a[0])
arq.close()

# exemplo 5 - Printa o primeiro nome
a3 = open("nomes.txt", "r")
for i in a3:
    a = i.split()
    print(a[0])
a3.close()

# exemplo 5 - Printa o primeiro nome
a3 = open("nomes.txt", "r")
for i in a3:
    a = i.split()
    print(f'{a[0]}.{a[-1]}') # Tira o espaço entre os nomes e o ponto
a3.close()

# exemplo 6
nome = open("nomes.txt", "r")
for i in nome:
    a = i.split()
    print(f'{a[0]}.{a[-1]}@email.com.br'.lower())
nome.close()

# exemplo
nome = open('nomes.txt', 'r')
emails = open('emails.txt', 'w+')

for i in nome:
    a = i.split()

    emails.write(f'{a[0]}.{a[-1]}@email.com.br\n'.lower())
    print(f'{a[0]}.{a[-1]}@email.com.br'.lower())


emails.close()
nome.close()








a3 = open("nomes.txt", "r")
for i in a3:
    a = i.split()
    print(f'{a[0]}.{a[-1]}') # Tira o espaço entre os nomes e o ponto
a3.close()






alunos = open("teste.txt", "a")
confirm = -1
while confirm != 0:
    alunos.write(input("Insira um nome : "))
    confirm = int(input("Terminou de adicionar nomes?\nSe sim pressione 0\nSe não pressione 1: "))
if confirm == 1:
    alunos.close()
print('Fim')
