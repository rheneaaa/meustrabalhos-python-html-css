class Conta():
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, saque):
        self.saldo -= saque

x = Conta(123, 'Rhene', 500)

print(vars(x)) # Para fins de testes pode utilizar este formato
x.alterarNome('Mikio')
x.deposito(200)
print(vars(x))
x.saque(400)
print(vars(x))
