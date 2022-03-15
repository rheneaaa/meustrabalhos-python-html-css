class Tenis:
    def __init__(self, cor, tamanho, marca, peso, modelo):
       self.cor = cor
       self.tamanho = tamanho
       self.marca = marca
       self.peso = peso
       self.modelo = modelo

    def getcor(self):
        return self.cor
    def gettamanho(self):
        return self.tamanho
    def getmarca(self):
        return self.marca
    def getpeso(self):
        return self.peso
    def getmodelo(self):
        return self.modelo

    def altCor(self, cor):
        self.cor = cor
    def altTamanho(self, tamanho):
        self.tamanho = tamanho
    def altMarca(self, marca):
        self.marca = marca
    def altPeso(self, marca):
        self.marca = marca
    def altModelo(self, modelo):
        self.modelo = modelo

Tenis1 = Tenis('Azul', 40, 'Nike', '500g', 'Masculino')
print('Cor:', Tenis1.getcor(), '\nTamanho:', Tenis1.gettamanho(), '\nMarca:', Tenis1.getmarca(), '\nPeso:', Tenis1.getpeso(), '\nModelo:', Tenis1.getmodelo())

Tenis2 = input('Digite a cor: ')
Tenis1.altCor(Tenis2)
print('Cor:', Tenis1.getcor())
