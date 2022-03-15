s = str(input('Informe seu sexo: ')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(s))
