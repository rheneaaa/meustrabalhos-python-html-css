'''Crie uma classe Livro que possui os
atributos nome, qtdPaginas, autor e preço.
– Crie os métodos getPreco para obter o valor do preco e o método setPreco para setar um novo valor do preco.'''

class Livro():
    def __init__(self, nome, qtdPaginas, autor, preço):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preço = preço

    def getNome(self):
        return self.nome
    def getqtsPaginas(self):
        return self.qtdPaginas
    def getAutor(self):
        return self.autor
    def getPreço(self, valor):
        self.preço.append(valor)
    def setPreço(self):
        self.preço.pop(0)

l1 = Livro('Harry Potter', 345, 'Nome do autor', '46,90')



