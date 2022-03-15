repo = open('repositorios.txt', 'r')
links = open('links.txt', 'w+')

for linha in repo:
    a = linha.split(':')
    print(f'{a[-2]}')
    links.write(f'{a[1]}\n')

repo.close()
links.close()

