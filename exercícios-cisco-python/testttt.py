'''class Pneu():
    def __init__(self, largura, altura, diametro):
        self.largura = largura
        self.altura = altura
        self.diametro = diametro

    def getLargura(self):
        return self.largura

    def getAltura(self):
        return self.altura

    def getDiametro(self):
        return self.diametro

pneu1 = Pneu('\nLargura do Pneu 265', '\nAltura do Pneu 50', '\nDiametro do Pneu 15')
print('Pneu:', pneu1.getLargura(), pneu1.getAltura(), pneu1.getDiametro())'''


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


livro1 = Livro("Harry Potter", 345, "NomedoAutor", "46,90")
print("Livro:", livro1.getNome(), "Preço:", livro1.getPreco())

livro2 = Livro("Narnia", 555, "NomedaAutora", "99,90")
print("Livro:", livro2.getNome(), "Preço:", livro2.getPreco())

livro1.alterarPreco("23,45")
print("Livro:", livro1.getNome(), "Preço de black friday:", livro1.getPreco())

npreco = input("Digite o novo preço do Livro2: ")
livro2.alterarPreco(npreco)
print("Livro:", livro2.getNome(), "Preço:", livro2.getPreco())
