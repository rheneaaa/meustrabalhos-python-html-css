login = input("Insira seu nome: ")
senha = input("Insira sua senha: ")
while senha == login:
    print("A senha não pode ser igual o usuário, tente novamente.")
    login = input("Insira seu nome: ")
    senha = input("Insira sua senha: ")

print("Cadastro concluído!")
