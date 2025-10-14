# while
# num_escolhido = int(input("Digite o numero escolhido: "))
# multiplo = 1


# while multiplo <= 10:
#     tabuada = (num_escolhido * multiplo)
#     multiplo += 1
#     print(tabuada)

# while True

num_escolhido = int(input("Digite o número escolhido: "))
multiplo = 1

while True:
    tabuada = num_escolhido * multiplo
    print(tabuada)
    multiplo += 1

    if multiplo > 10:
        break