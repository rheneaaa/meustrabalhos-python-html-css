class carro:
    def __init__(self):
        self.valorGasolina = 7.15
        self.tanque = 50

    def getValorGasolina(self):
        return self.valorGasolina

    def gatTanque(self):
        return self.tanque

car = carro()
gas = float(input('Digite quantos litros deseja colocar: '))
print('Colondo ', gas, 'litros, você vai pagar R$', (gas*car.getValorGasolina()))
