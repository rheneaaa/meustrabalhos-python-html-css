nome = input('Insira o seu nome: ')
idade = int(input('Insira sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('Informe seu sexo: ')
ec = input('Informe seu estado civil: ')
while len(nome) < 4:
    if idade > 150:
       # while salario < 0:
            #    while sexo != 'f' or sexo != 'm':
            #  while ec != 'solteiro' or 'casado':
            print("Cadastro incorreto, digite novamente: ")
            nome = input('Insira o seu nome: ')
            idade = int(input('Insira sua idade: '))
            salario = float(input('Digite seu salário: '))
            sexo = input('Informe seu sexo: ')
            ec = input('Informe seu estado civil: ')
print('ok')
