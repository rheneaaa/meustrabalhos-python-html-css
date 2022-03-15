alunos = open("teste.txt", "a")
confirm = -1
while confirm != 0:
    alunos.write(input("Insira um nome : "))
    confirm = int(input("Terminou de adicionar nomes?\nSe sim pressione 0\nSe não pressione 1: "))
if confirm == 1:
    alunos.close()
print('Fim')
