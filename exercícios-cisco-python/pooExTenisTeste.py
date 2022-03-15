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
    def altPeso(self, peso):
        self.peso = peso
    def altModelo(self, modelo):
        self.modelo = modelo

Tenis1 = Tenis('Azul', 40, 'Nike', '500g', 'Masculino')
print('Exemplo - Cor:', Tenis1.getcor(), '- Tamanho:', Tenis1.gettamanho(), '- Marca:', Tenis1.getmarca(), '- Peso:', Tenis1.getpeso(), '- Modelo:', Tenis1.getmodelo())

print('Olá!. Digite o modelo que deseja!')

t = int(input('Escolha: Opção 1 - Opção 2 - Opção 3 - Opção 4 - Opção 5: '))
op1 = ('Amarelo', 35, 'Adidas', '400g', 'Feminino')
op2 = ('Branco', 36, 'Olimpikus', '400g', 'Feminino')
op3 = ('Vermelho', 37, 'NB', '400g', 'Feminino')
op4 = ('Azul', 38, 'Okley', '500g', 'Masculino')
op5 = ('Cinza', 39, 'Adidas', '500g', 'Masculino')

if t == 1:
    print('Opção 1 - Cor: Amarelo -', 'Tamanho: 35 -', 'Marca: Adidas -', 'Peso: 400g -', 'Modelo: Feminino'.format(op1))
elif t == 2:
    print('Opção 2 - Cor: Branco -', 'Tamanho: 36 -', 'Marca: Olimpikus -', 'Peso: 400g -', 'Modelo: Feminino'.format(op2))
elif t == 3:
    print('Opção 3 - Cor: Vermelho -', 'Tamanho: 37 -', 'Marca: NB -', 'Peso: 400g -', 'Modelo: Feminino'.format(op3))
elif t == 4:
    print('Opção 4 - Cor: Azul -', 'Tamanho 38 -', 'Marca: Okley -', 'Peso: 500g -', 'Modelo: Masculino'.format(op4))
elif t == 5:
    print('Opção 5 - Cor: Cinza -', 'Tamanho: 39 -', 'Marca: Adidas -', 'Peso: 500g -', 'Modelo: Masculino'.format(op5))


