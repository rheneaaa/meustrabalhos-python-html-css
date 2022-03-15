votos = [0, 0, 0, 0, 0, 0]
turma1 = [0, 0, 0, 0, 0, 0]
turma2 = [0, 0, 0, 0, 0, 0]
turma3 = [0, 0, 0, 0, 0, 0]
canditato = ["Ana", "Pedro", "Rita", "Alfredo", "Regina", "Ricardo"]
nulo = 0
branco = 0
total = 0
vt = 0
turma = 1

print("Eleções do Grêmio estudantil")
print("Candidatos e suas chapas:\n"
      "Chapa1-Ana\n"
      "Chapa2-Pedro\n"
      "Chapa3-Rita\n"
      "Chapa4-Alfredo\n"
      "Chapa5-Regina\n"
      "Chapa6-Ricardo\n"
      "0 - Voto nulo\n"
      "10 - Voto em branco\n")
while total != 5:
    vt = 0
    #turma = int(input("Digite o numero da sua turma para votar:\n"))
    while True:
        try:
            turma = int(input("Digite o número da sua turma para votar: 1, 2 ou 3\n"))
            if not 0 < turma < 4:
                raise ValueError("Digite um úumero válido para a turma")
        except ValueError as error:
            print("Digite um número válido para a turma")
        else:
            break
    if turma == 1:
        while vt != -1:
            #vt = int(input(f"Numero do Candidato:"))
            while True:
                try:
                    vt = int(input(f"Número do Candidato:"))
                    if not (-1 < vt < 7 or vt == 10) or vt is not int:
                        raise ValueError("Digite um número válido para o Candidato")
                except ValueError as error:
                    print("Digite um número válido para o Candidato")
                else:
                    break
            if vt == 0:
                nulo += 1
                total += 1
                vt = -1
            elif vt == 10:
                branco += 1
                total += 1
                vt = -1
            elif vt >= 1 and vt <= 6:
                votos[vt - 1] += 1
                turma1[vt - 1] += 1
                total += 1
                vt = -1
            else:
                print("Numero inválido\n"
                      "Chapa1-Ana\n"
                      "Chapa2-Pedro\n"
                      "Chapa3-Rita\n"
                      "Chapa4-Alfredo\n"
                      "Chapa5-Regina\n"
                      "Chapa6-Ricardo\n"
                      "0 - Voto nulo\n"
                      "10 - Voto em branco\n")
    elif turma == 2:
        while vt != -1:
            print("Candidatos e suas chapas:\n"
                  "Chapa1-Ana\n"
                  "Chapa2-Pedro\n"
                  "Chapa3-Rita\n"
                  "Chapa4-Alfredo\n"
                  "Chapa5-Regina\n"
                  "Chapa6-Ricardo\n"
                  "0 - Voto nulo\n"
                  "10 - Voto em branco\n")
            # vt = int(input(f"Numero do Candidato:"))
            while True:
                try:
                    vt = int(input(f"Número do Candidato:"))
                    if not -1 < vt < 7 or vt == 10 or vt is not int:
                        raise ValueError("Digite um número válido para o Candidato")
                except ValueError as error:
                    print("Digite um número válido para o Candidato")
                else:
                    break
            if vt == 0:
                nulo += 1
                total += 1
                vt = -1
            elif vt == 10:
                branco += 1
                total += 1
                vt = -1
            elif vt >= 1 and vt <= 6:
                votos[vt - 1] += 1
                turma2[vt - 1] += 1
                total += 1
                vt = -1
            else:
                print("Número inválido\n"
                      "Chapa1-Ana\n"
                      "Chapa2-Pedro\n"
                      "Chapa3-Rita\n"
                      "Chapa4-Alfredo\n"
                      "Chapa5-Regina\n"
                      "Chapa6-Ricardo\n"
                      "0 - Voto nulo\n"
                      "10 - Voto em branco\n")
    elif turma == 3:
        while vt != -1:
            print("Candidatos e suas chapas:\n"
                  "Chapa1-Ana\n"
                  "Chapa2-Pedro\n"
                  "Chapa3-Rita\n"
                  "Chapa4-Alfredo\n"
                  "Chapa5-Regina\n"
                  "Chapa6-Ricardo\n"
                  "0 - Voto nulo\n"
                  "10 - Voto em branco\n")
            # vt = int(input(f"Numero do Candidato:"))
            while True:
                try:
                    vt = int(input(f"Número do Candidato:"))
                    if not -1 < vt < 7 or vt == 10 or vt is not int:
                        raise ValueError("Digite um numero válido para o Candidato")
                except ValueError as error:
                    print("Digite um número válido para o Candidato")
                else:
                    break
            if vt == 0:
                nulo += 1
                total += 1
                vt = -1
            elif vt == 10:
                branco += 1
                total += 1
                vt = -1
            elif vt >= 1 and vt <= 6:
                votos[vt - 1] += 1
                turma3[vt - 1] += 1
                total += 1
                vt = -1
            else:
                print("Número inválido\n"
                      "Chapa1-Ana\n"
                      "Chapa2-Pedro\n"
                      "Chapa3-Rita\n"
                      "Chapa4-Alfredo\n"
                      "Chapa5-Regina\n"
                      "Chapa6-Ricardo\n"
                      "0 - Voto nulo\n"
                      "10 - Voto em branco\n")
    else:
        print("Digite o número da sua turma para iniciar a votação!!")
print()
vtval = total - nulo - branco
print(f"Resultado da Votação:\n"
      f"Foram computados {total} de votos\n"
      f"O número de votos válidos {vtval}\n"
      f"Total de votos nulos {nulo}\n"
      f"Total de votos Bracos {branco}\n"
      f"Porcentagem de votos\n"
      f"Votos Validos:{round((vtval / total) * 100, 2)}%\n"
      f"Votos Nulos:{round((nulo / total) * 100, 2)}%\n"
      f"Votos Brancos:{round((branco / total) * 100, 2)}%\n\n"
      f"Caditado   votos      %\n")

for i in range(6):
    print(f"{canditato[i]:<7}      {votos[i]}   {round((votos[i]/total) * 100, 2):>5}%")
print()
print("Porcentagens de votos por Turma\n")
for j in range(6):
    print(f"{canditato[j]:<7} {round((turma1[j] / total) * 100, 2):>11}%-turma 1"
          f" {round((turma2[j]/total) * 100, 2):>11}%-turma 2"
          f" {round((turma3[j]/total) * 100, 2):>11}%-turma 3")