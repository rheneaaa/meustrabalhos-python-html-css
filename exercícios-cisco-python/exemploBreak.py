# break - example

print("Instrução de pausa:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do loop.", i)
print("Fora do loop.")


# continue - example

print("\nA instrução continua:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do loop.", i)
print("Fora do loop.")
