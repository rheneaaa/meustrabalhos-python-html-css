class Macaco():
    def __init__ (self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print('Bucho', self.bucho)

    def digerir(self):
        if (len(self.bucho) > 0):
            self.bucho.pop(0)

m1 = Macaco('Macaco 1')
m1.comer('Maça')
m1.verBucho()
m1.comer('Banana')
m1.verBucho()
m1.comer('Abacaxi')
m1.verBucho()
m1.digerir()
m1.verBucho()
m2 = Macaco('Macaco 2')
m2.comer('Feijão')
m2.verBucho()
