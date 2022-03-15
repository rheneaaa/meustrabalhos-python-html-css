frase = "http://www.sc.senai.br"
print(frase)
print(frase.replace('.', '-',1))



em = open('emails.txt', 'r')
nv = open('novos_emails.txt', 'w+')

for linha in em:
  a = linha.split('@')
  print(f"{a[0].replace('.','_')}@estudante.blumenau.senai")

em.close()
nv.close()