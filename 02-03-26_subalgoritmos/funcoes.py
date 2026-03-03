# Definição de função - sem parâmetros
# def valor_de_pi():
#     return 3.14159

# # Uso 
# raio = float(input("Digite o raio: "))
# area_circulo = valor_de_pi() * raio * 2
# print(f"Área do círculo com {raio} é {area_circulo}")

# Dado um número por parâmetro, faça uma função que retorne o próximo 
# número

def proximo_numero(n):
    return n + 1

# Uso 
# numero = int(input("Número: "))
# prox = proximo_numero(numero)
# print(f"{numero}, próximo {prox}")

# Exercícios 
# 1. Dado um número por parâmetro, retorne o dobro
# resp = dobro(5) # resp valerá 10

# 2. Fazer uma função que calcule o valor de delta. (pense quantos e quais parâmtetros são
# necessários)
# resp = delta(1, 2, 3) # resp valerá -8

# 3. Fazer uma função que calcule a média de 4 números (pense quantos e quais parâmtetros são
# necessários)
# resp = media4n(8, 9, 10, 7) # resp valerá 7.5

# Dados por parâmetro um número e um múltiplo, exiba o próximo múltiplo do primeiro número
# resp = prox_mult(7, 22) # resp valerá 28

# 1.
def dobro(num: float) -> float:  # definindo o tipo do parâmetro e definindo o tipo que ele vai retornar
    return num * 2
print(dobro(5))

# 2.
def calcula_delta(a: float, b: float, c: float) -> float:
    delta = a ** 2 - 4 * b * c
    return delta
print(calcula_delta(1, 2, 3))

# 3.
def calcula_media(n1: float, n2: float, n3: float, n4: float) -> float:
    media = (n1 + n2 + n3 + n4)/4
    return media
print(calcula_media(8, 9, 10, 7))

# 4.
def prox_mult(num: int, mult: int) -> int:
    novo_mult = mult + 1
    while novo_mult % num != 0:
        novo_mult = novo_mult + 1
    return novo_mult
print(prox_mult(7, 22))