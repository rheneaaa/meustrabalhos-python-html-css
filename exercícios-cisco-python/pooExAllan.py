class Android:
    def _init_(self):
        self.modelo = "RK800"
        self.cor_pele = "Branca"
        self.Masc_ou_femi = "Masculino"
        self.altura = 1.70
        self.funcao = "Acompanhate"
        self.nome = "Android"

    def getModelo(self):
        return self.modelo

    def getCor_pele(self):
        return self.cor_pele

    def getMasc_ou_femi(self):
        return self.Masc_ou_femi

    def getAltura(self):
        return self.altura

    def getFuncao(self):
        return self.funcao

    def getNome(self):
        return self.nome

    def setCor_pele(self, cp):
        self.cor_pele = cp

    def setMasc_ou_femi(self, mf):
        self.Masc_ou_femi = mf

    def setFuncao(self, f):
        self.funcao = f

    def setNome(self, n):
        self.nome = n

an1 = Android()
print("Patrão de Facrica")
print(f"Modelo:{an1.getModelo()}\nNome:{an1.getNome()}\nSexo:{an1.getMasc_ou_femi()}\nCor Da pele:{an1.getCor_pele()}\n"
      f"Altura:{an1.getAltura()}\nFunção:{an1.getFuncao()}")
print()
v = int(input(f"Bem vindo a Cyber Life\nEsse é o Android Pessol {an1.getModelo()}\nAgora vc pode configurar seu Android:\n"
        f"opção 1 Altera o nome:\nopção 2 Cor da pele:\nopção 3 Genero sexual:\nopção 4 Funçao:\n"
        f"opção 5 mudar todas configurações:\nopção 0 manter configurações de frabrica:\nopção:"))
if v == 1:
    n = input(f"Novo nome do {an1.getModelo()}:")
    an1.setNome(n)
elif v == 2:
    cp = input(f"Nova Cor de pele do {an1.getModelo()}:")
    an1.setCor_pele(cp)
elif v == 3:
    mf = input(f"Novo genero sexual do {an1.getModelo()}:")
    an1.setMasc_ou_femi(mf)
elif v == 4:
    f = input(f"Qual será a Função do {an1.getModelo()}:")
    an1.setFuncao(f)
elif v == 5:
    n = input(f"Novo nome do {an1.getModelo()}:")
    an1.setNome(n)
    cp = input(f"Nova Cor de pele do {an1.getModelo()}:")
    an1.setCor_pele(cp)
    mf = input(f"Novo genero sexual do {an1.getModelo()}:")
    an1.setMasc_ou_femi(mf)
    f = input(f"Qual será a Função do {an1.getModelo()}:")
    an1.setFuncao(f)
print()
print(f"Modelo:{an1.getModelo()}\nNome:{an1.getNome()}\nSexo:{an1.getMasc_ou_femi()}\nCor Da pele:{an1.getCor_pele()}\n"
      f"Altura:{an1.getAltura()}\nFunção:{an1.getFuncao()}")
print()
print("A CYBER LIFE AGRADECE A SUA PREFERENCIA")