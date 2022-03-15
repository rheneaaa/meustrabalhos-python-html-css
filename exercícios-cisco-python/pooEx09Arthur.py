class Telefone: # Cria uma classe
  def __init__(self, numero, modelo, cor): # Inicia as classes
    self.numero = numero # Definição de classes
    self.modelo = modelo # Definição de classes
    self.cor = cor # Definição de classes

  def getnumero(self): # getnumero armazena o objeto da classe Telefone
    return self.numero # getnumero vai retornar a função self.numero quando for chamada

  def getmodelo(self): # getmodelo armazena o objeto da classe Telefone
    return self.modelo # getmodelo vai retornar a função self.modelo quando for chamada

  def getcor(self): # getcor armazena o objeto da classe Telefone
    return self.cor # getcor vai retornar a função self.cor quando for chamada

  def altNumero(self, numero): # Altera o número da classe número
    self.numero = numero

  def altModelo(self, modelo): # Altera o modelo da classe modelo
    self.modelo = modelo

  def altCor(self, cor): # Altera a cor da classe cor
    self.cor = cor

Telefone1 = Telefone("(52) 8374-5920",  "S30", "Vermelho") # Informa o número modelo e cor
print("Telefone1:", Telefone1.getnumero(), "numero", Telefone1.getmodelo(), "modelo", Telefone1.getcor(), "cor") # Aparece na tela do usuário o número modelo e cor

num1 = input('Digite o novo número: ') # Pergunta para o usuário
Telefone1.altNumero(num1) # Chama a função altNumero e coloca o novo numero digitado na pergunta
print('Novo número é:', Telefone1.getnumero()) # Aparece na tela do usuário o novo número

model1 = input('Digite o novo modelo: ') # Pergunta para o usuário
Telefone1.altModelo(model1) # Chama a função altModelo e coloca o novo modelo digitado na pergunta
print('Novo modelo é', Telefone1.getmodelo()) # Aparece na tela do usuário o novo modelo

cor1 = input('Digite a nova cor: ') # Pergunta para o usuário
Telefone1.altCor(cor1) # Chama a função altCor e coloca a nova cor digitado na pergunta
print('A nova cor é: ', Telefone1.getcor()) # Aparece na tela do usuário a nova cor
