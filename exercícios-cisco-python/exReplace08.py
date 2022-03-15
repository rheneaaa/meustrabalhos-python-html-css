repo = open("repositorios.txt", "r", encoding="utf8")

for i in repo:
    a = i.split(':')
    pais = f"{a[0].lower()}.txt"

    links = open(pais, "a")
    if a[0].lower() in pais:
        links.write(f"{a[1]}\n")
    links.close()
repo.close()
