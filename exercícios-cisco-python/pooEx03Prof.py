class Funcionario:
    def __init__(self, nome, salario):  # recebe 2 parâmetros para criação do objeto
        self.nome = nome
        self.salario = salario

    def getNome(self):  # método para exportar um atributo da classe
        return self.nome  # atributo a ser exportado

    def getSalario(self):  # método para exportar um atributo da classe
        return self.salario  # atributo a ser exportado


fun1 = Funcionario("Daniel", 1234)  # criação de objeto, passando 2 parâmetros para a classe
fun2 = Funcionario("Fernando", 2345)  # criação de objeto, passando 2 parâmetros para a classe
fun3 = Funcionario("Miguel", 3456)  # criação de objeto, passando 2 parâmetros para a classe

print("Nome:", fun1.getNome(), "- Salário:", fun1.getSalario())  # observar aqui a forma como está sendo instanciado os atributos
print("Nome:", fun2.getNome(), "- Salário:", fun2.getSalario())  # observar aqui a forma como está sendo instanciado os atributos
print("Nome:", fun3.getNome(), "- Salário:", fun3.getSalario())  # observar aqui a forma como está sendo instanciado os atributos
