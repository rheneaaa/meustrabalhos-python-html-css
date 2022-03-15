class Ct_Corrente():
  def __init__(self, num_conta, nome, saldo=0):
    self.num_conta = num_conta
    self.nome = nome
    self.saldo = saldo
  def getNumConta(self):
    return self.num_conta
  def getNome(self):
    return self.nome
  def getSaldo(self):
    return self.saldo
  def auterarNome(self, nvnome):
    self.nome = nvnome
  def Deposito(self, valdeposito):
    self.saldo += valdeposito
  def Saque(self, valsaque):
    self.saldo -= valsaque

cliente1 = Ct_Corrente(123456-0, "Bezalel")

print("Número da conta:", cliente1.getNumConta(),"\nNome:", cliente1.getNome(),"\nSaldo: R$", cliente1.getSaldo())

nvnome = input("Digite o nome do cliente: ")
cliente1.auterarNome(nvnome)
valdeposito = float(input("O valor do depósito? "))
cliente1.Deposito(valdeposito)
valsaque = float(input("Digite o valor do saque: R$ "))
cliente1.Saque(valsaque)

print("Número da conta:", cliente1.getNumConta(),"\nNome:", cliente1.getNome(),"\nSaldo: R$", cliente1.getSaldo())
