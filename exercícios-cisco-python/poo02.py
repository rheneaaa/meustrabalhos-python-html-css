class Funcionario:
    def __init__(self):
        self.nome = 'Rhene'
        self.salario = float(1000.00)

    def getNome(self): # Método para exportar um atributo da classe
        return self.nome # Atributo a ser exportado

    def getSalario(self): # Método para exportar um atributo da classe
        return self.salario # Atributo a ser exportado


fun1 = Funcionario()
fun2 = Funcionario()
fun3 = Funcionario()

print('Nome: {} \nSalário: {:.2f}'.format(fun1.getNome(), fun1.getSalario()))
print()


"""                     Exemplo
class FolhaPagamento: # Nova classe
    fun1.nome # Isso não fuinciona
    fun1.getNome() # Isso funciona"""