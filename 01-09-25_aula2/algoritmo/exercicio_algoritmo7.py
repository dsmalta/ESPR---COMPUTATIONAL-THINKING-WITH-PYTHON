"""
Sétimo exercício
"""

valor = int(input("Digite um valor:"))
multiplo_cinco = ((valor // 5) + 1) * 5
# print("O multiplo de 5 mais proximo de", valor, "é", multiplo_cinco)
print(f"{valor:05d} próximo multiplo {multiplo_cinco:05d}") #d de decimal, 5 número de caracteres, 0 completar o espaço