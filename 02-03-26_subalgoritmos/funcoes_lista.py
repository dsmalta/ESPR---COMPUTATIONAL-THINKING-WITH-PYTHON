# Fazer um procedimento que exiba na tela o índice
# e o conteúdo de uma lista

def exibe_lista(l: list) -> None:
    for i in range(0, len(l), 1):
        print(f"{i} -> {l[i]}")

def exibe_lista2(l: list) -> None:
    for ind, elem in enumerate(lista):
        print(f"{ind} -> {elem}")


# Principal

lista = [45, 23, "CP4", 56.67]
exibe_lista(lista)
exibe_lista2(lista)

# Exercícios 
# 1. FUNÇÂO: Dada uma lista somente com números, calcule a somatória dela
# 2. FUNÇÂO: Calcule a média de uma lista
# 3. FUNÇÂO: Maior valor da lista