class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def getNome(self):
        return self.nome

    def getDucho(self):
        return self.bucho

    def comer(self, comida):
        self.bucho.append(comida)

    def direrir(self):
        self.bucho.pop(0)


m1 = Macaco("Allan")
print('O macaco', m1.getNome())
for i in range(3):
    comida = input(f"O que vc quer que {m1.getNome()} coma:")
    m1.comer(comida)
    print(f"Bucho do Macaco {m1.getNome()} {m1.getDucho()}")

