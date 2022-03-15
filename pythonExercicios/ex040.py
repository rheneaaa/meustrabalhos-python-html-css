from datetime import date
atual = date.today().year
nasc = int(input('Qual sua data de nascimento? '))
data = atual - nasc

if data <= 9:
    print('Você tem {} anos e é MIRIM'.format(data))
elif 9 < data <= 14:
    print('Você tem {} anos e é INFANTIL'.format(data))
elif 14 < data <= 19:
    print('Você tem {} anos e é JUNIOR'.format(data))
elif 19 < data <= 20:
    print('Você tem {} anos e é SÊNIOR'.format(data))
else:
    print('Você tem {} anos e é MASTER'.format(data))