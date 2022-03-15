"""from datetime import date
data = input('Digite sua data de nascimento: ')

dia = data[:2]
mes = data[3:5]
ano = data[6:]

if mes == '05':
    print('Você nasceu em {} de maio de {}'.format(dia, ano))
elif mes == '06':
    print('Você nasceu em {} de junho de {}'.format(dia, ano))"""

lista = ['mes', 'Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data = input('Digite sua data de nascimento: ')
dia = data[:2]
mes = int(data[3:5])
ano = data[6:]
print('Você nasceu em {} de {} de {}'.format(dia, lista[mes], ano))