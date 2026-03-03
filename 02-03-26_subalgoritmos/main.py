# Criação da função

def retorna_maior(n1, n2, n3):
    maior = n1 
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    return maior

# Dados 3 números, retornar o de maior valor

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

print(retorna_maior(n1, n2, n3))
