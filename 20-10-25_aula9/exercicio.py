# Para treino, faça uma versão com cada laço.
# Dados dois números pelo usuário (início e fim), exiba os números em ordem crescente se
# o primeiro for menor que o segundo, senão em ordem decrescente
"""
início: 4
fim:    18

4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

início: 12
fim:    7

7 8 9 10 11 12
"""

# print("Com o while")

# inicio = int(input("Digite um número: "))
# fim = int(input("Digite outro número: "))
# volta = inicio

# while volta <= fim:
#     print(volta)
#     volta = volta + 1

# print("Com o while True")

# inicio = int(input("Digite um número: "))
# fim = int(input("Digite outro número: "))
# volta = inicio

# while True:
#     print(volta)
#     volta = volta + 1
#     if volta > fim:
#         break

# print("Com o for")

# inicio = int(input("Digite um número: "))
# fim = int(input("Digite outro número: "))

# for volta in range (inicio, fim + 1, 1):
#     print(volta)


# inicio = int(input("Digite um número: "))
# fim = int(input("Digite outro número: "))
# volta = inicio

# if inicio < fim:
#         for volta in range (inicio, fim + 1, 1):
#             print(volta)
# else:
#         for volta in range (fim, inicio + 1, 1):
#             print(volta)

# # Exemplo do Professor

# inicio = int(input("Digite um número: "))
# fim = int(input("Digite outro número: "))

# if inicio > fim: 
#      aux = inicio # aux 10
#      inicio = fim # inicio 4
#      fim = aux # 10

# Para treino, faça uma versão com cada laço.
# Dados dois números pelo usuário (início e fim), exiba os números em ordem crescente se
# o primeiro for menor que o segundo, senão em ordem decrescente

inicio = int(input("Digite um número: "))
fim = int(input("Digite outro número: "))

if inicio > fim:
    # Exibe em ordem crescente
    for volta in range (inicio, fim + 1, 1):
        print(volta)

else:
    # Exibe em ordem decresnte
    for volta in range (fim, inicio - 1, -1):
        print(volta)