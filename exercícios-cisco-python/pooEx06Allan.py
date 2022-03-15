class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivel = 0

    def abastecer(self, gaso):  # encher o tanque
        self.nivel += gaso

    def getNivel(self):  # litros que tem no tanque
        return self.nivel

    def andar(self, km):
        temp = km / self.consumo
        self.nivel -= temp

    # def getDirigir(self): #distancia em km
    #     return self.dirigir


meuFusca = Carro(15)
print("Nivel de Combustivel:", meuFusca.getNivel())
gaso = int(input("Quanto de gasoliga vc quer abastecer:"))
meuFusca.abastecer(gaso)
print("Nivel de Combustivel:", meuFusca.getNivel(), "Litros")
km = int(input("Quantos km vc vai rodar:"))
meuFusca.andar(km)
# meuFusca.nivelCombus(km, gaso)
print("Vc rodou {meuFusca.getDirigir()}km e Nivel do tanque", round(meuFusca.getNivel(), 2), "Litros")