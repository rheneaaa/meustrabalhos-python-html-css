nome = str(input("Funcionário: "))
hort = int(input("Horas trabalhadas: "))
horv = float(input("Valor da hora em R$: "))
fgts = float(input("Desconto do FGTS em %: "))
inss = int(input("Desconto do INSS em %: "))
val = float(input("Desconto do vale alimentação em R$: "))
vatr = float(input("Desconto do vale transporte em R$: "))
plsa = int(input("Desconto do plano de saúde em R$: "))
salat = (hort * horv)
fgts = (salat / 100) * fgts
inss = (horv / 100) * inss
salario = salat - (fgts + inss + val + vatr + plsa)
print('Funcionário:{}\nSalário(hora):R${:.2f}\nHoras trabalhadas:{:.2f}hs\nDesconto do FGTS:{:.1f}%\nDesconto do '
      'INSS:{:.1f}%\nVale alimentação:R${:.2f}\nVale transporte:R${:.2f}\nPlano de saúde:R${:.2f}\nTotal:R${'
      ':.2f}'.format(nome, hort, horv, fgts, inss, val, vatr, plsa, salario))
