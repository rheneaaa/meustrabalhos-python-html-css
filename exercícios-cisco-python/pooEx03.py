class Funcionario:
    def __init__(self, nome, salario): # Recebe 2 parâmetros para a criação de objeto
        self.nome = nome
        self.salario = salario

    def getNome(self): # Método para exportar um atributo da classe
        return self.nome # Atributo a ser exportado

    def getSalario(self): # Método para exportar um atributo da classe
        return self.salario # Atributo a ser exportado

n1 = input('Digite o nome do funcionário: ')
s1 = input('Digite o salário do funcionário: ')

fun1 = Funcionario('Rhene', 1000.00) # Criação de objeto, passando 2 parâmetros para a classe
fun2 = Funcionario('Mikio', 2000.00) # Criação de objeto, passando 2 parâmetros para a classe
fun3 = Funcionario('Yuuki', 3000.00) # Criação de objeto, passando 2 parâmetros para a classe

print('Nome: {} \nSalário: {:.2f}'.format(fun1.getNome(), fun1.getSalario()))
print('Nome: {} \nSalário: {:.2f}'.format(fun2.getNome(), fun2.getSalario()))
print('Nome: {} \nSalário: {:.2f}'.format(fun3.getNome(), fun3.getSalario()))

