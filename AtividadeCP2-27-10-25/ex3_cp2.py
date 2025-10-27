# Davi de Souza Malta - 560327

num_inicio = int(input("Início: "))
num_final = int(input("Fim: "))

for volta in range(num_inicio, num_final):
    if volta % 5 == 0:
        print(volta)