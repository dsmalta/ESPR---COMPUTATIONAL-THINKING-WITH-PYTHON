# Davi de Souza Malta - 560327

num_inicio = int(input("Início: "))
num_final = int(input("Fim: "))
ordem = input("Ordem: ")

if ordem == "C":
    for volta in range(num_inicio, num_final + 1, 1):
        print(f"Multiplos: {volta}")

elif ordem == "D":
    for volta in range(num_final, num_inicio - 1, -1):
        print(f"Multiplos {volta}")