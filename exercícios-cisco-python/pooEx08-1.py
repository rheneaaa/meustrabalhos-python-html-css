class Livro:
    def __init__(self, nome, qtdpg, autor, preco):
        self.nome = nome
        self.qtdpg = qtdpg
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        return self.preco

    def getNome(self):
        return self.nome

    def alterarPreco(self, preco):
        self.preco = preco



livro2 = Livro("Narnia", 555, "NomedaAutora", "99,90")
print("Livro:", livro2.getNome(), "Preço:", livro2.getPreco())

npreco = input("Digite o novo preço do Livro2: ")
livro2.alterarPreco(npreco)
print("Livro:", livro2.getNome(), "Preço:", livro2.getPreco())

