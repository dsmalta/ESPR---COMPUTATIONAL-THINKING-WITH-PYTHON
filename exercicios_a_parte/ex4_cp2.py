# Davi de Souza Malta - 560327

num_inicio = int(input("Início: "))
num_final = int(input("Fim: "))
multiplo = int(input("Mult: "))

for volta in range(num_inicio, num_final):
    if volta % multiplo == 0:
        print(volta)