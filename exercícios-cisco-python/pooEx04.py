class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, porcentagem = 0):
        self.salario += self.salario * porcentagem / 100

fun3 = Funcionario('Yuuki', 3000)
print('Nome: {} \nSalário: {}'.format(fun3.getNome(), fun3.getSalario()))
aumento = int(input('Digite o aumento do funcionário em %: '))
fun3.aumentarSalario(aumento)
print('Nome: {} \nSalário: {}'.format(fun3.getNome(), fun3.getSalario()))
