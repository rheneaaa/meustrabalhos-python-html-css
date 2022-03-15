class Carro():
    def __init__ (self, consumo):
        self.consumo = consumo # Recebe o valor a partir do objeto
        self.nivelCombustivel = 0 # Nível de combustível inicia com 0



    def adicionarGasolina(self, qtde):
        self.nivelCombustivel += qtde # Adicionando gasolina no tanque

    def obterGasolina(self):
        return self.nivelCombustivel

    def andar(self, distancia): # Distância em km
        litros = distancia / self.consumo
        self.nivelCombustivel -= litros

meuFusca = Carro(15)
print('Nível de combustível', meuFusca.obterGasolina())
meuFusca.adicionarGasolina(40)
print('Nível de combustível após abastecimento:', meuFusca.obterGasolina())
gaso = int(input('Quanto de gasolina você quer abastecer? '))
meuFusca.adicionarGasolina(gaso)
print('Nível de combustível após abastecimento: ', meuFusca.obterGasolina())

meuFusca.andar(90)
print('Nível de combustível após percorrer um trajeto:', meuFusca.obterGasolina())
