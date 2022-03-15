class Televisão: # Início da classe, nome Televisão
    def __init__(self): # Construtor init, método self
        self.ligada = False # Atributo ligada
        self.canal = 2 # Atributo canal
        self.tamanho = 20 # Atributo tamanho
        self.marca = "Ching-Ling" # Atributo marca

tv = Televisão() # Criação do objeto
tv.tamanho = 32 # Alterando o valor do atributo tamanho do objeto tv

tv_sala = Televisão()
tv_sala.marca = 'Samsung' # Alterando o valor do atributo marca do objeto tv

print("tv - tamanho:", tv.tamanho) # Exibindo as informações do objeto tv
print("tv da sala - tamanho:", tv_sala.tamanho, '\nMarca:', tv_sala.marca)

tv2 = Televisão()
tv2.tamanho = input("Digite o tamanho para a nova TV: ") # Alterando o valor do atributo tamanho do objeto tv2
tv2.marca = input("Digite a marca da nova TV: ") # Alterando o valor do atributo marca do objeto tv2
print("tv2 - tamanho:", tv2.tamanho, "marca:", tv2.marca, "canal:", tv2.canal) # Exibindo as informações do objeto tv2