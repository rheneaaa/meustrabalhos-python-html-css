alunos = open('nomes.txt', 'a')
nome = 0
while nome != '':
    nome = input('Digite um nome: ')
    alunos.write(nome)
    alunos.write('\n')

alunos.close()


alunos = open("alunos.txt", "r+")
confirm = -1
while confirm !=0:
    alunos.write(input("Insira um nome : "))
    alunos.write("\n")
    confirm = int(input("Terminou de adicionar nomes?\nSe sim, pressione 0\nSe não pressione 1. : "))
if confirm == 0:
   for i in alunos:
    print("Nomes inseridos : ", i)
alunos.close()
