import os
os.system("cls")

# v = [54, 87, 12, 88, 90]
# print(v)
# # v[0] = int(input("Digite um valor: "))
# # print(v)

# for ind in range (0, 5, 1):
#     print(f"v[{ind}] = {v[ind]}")

v = [45, -89, 32, -12, 33]

# Exercício 1
# print(f"{v[0]}\n")

# # Exercício 2
# for ind in range (1, 5, 1):
#     if v[ind] % 2 != 0:
#         print(v[ind], end = " ")

# # Exercício 3
# for ind in range (1, 5, 1):
#     if v[ind] < 0: 
#         print(v[ind])

# Exercício 4
# soma = 0
# for ind in range (5):
#     soma += v[ind]
#     print(soma)

# Exercício 5
# tamanho_lista = len(v)

# soma_lista = 0 
# for ind in range (5):
#     soma_lista += v[ind]
#     media_lista = soma_lista / tamanho_lista
# print(media_lista)

# Exercício 6
# soma_elementos_pares = 0
# for ind in range (5):
#     if v[ind] % 2 == 0:
#         soma_elementos_pares += v[ind]
# print(soma_elementos_pares)

# Exercício 7
# for ind in range (5):
#     v[ind] = int(input("Digite um valor para o índice: "))

# print(v)

# Exercício 8
# ind = int(input("Digite o índice que você quer alterar: "))

# if 0 <= ind < len(v):
#     valor_ind = int(input(f"Digite um valor para o índice {ind}: "))
#     v[ind] = valor_ind
# else: 
#     print("Índice inválido")

# print(v)

# Exercício 9 
# invertido = [0, 0, 0, 0, 0]
# for ind in range(5):
#     invertido[4-ind] = v[ind]
# print(v)
# print(invertido)

#Exercício 10 
menor = v[0]
for ind in range(1, 5, 1):
    if v[ind] < menor:
        menor = v[ind]
print(f"Menor valor = {menor}")