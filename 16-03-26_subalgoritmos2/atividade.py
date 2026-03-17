# Funções

def quadrado(numero: float) -> float:
    return numero ** 2
print(quadrado(2))

def maior_3n(a: float, b: float, c: float) -> float:
    
    maior = a # maior é uma variável local
    
    if b > maior:
        maior = b
    
    if c > maior:
        maior = c
    
    return maior
print(maior_3n(5, 8, 33))
 

# def converter_dolar(valor_reais: float, cotacao_dolar: float) -> float:
#     return valor_reais / cotacao_dolar

# valor_reais = float(input('Digite um valor em reais: '))
# cotacao_dolar = float(input('Digite a cotação atual do dólar: '))

# print(f'{converter_dolar(valor_reais, cotacao_dolar):.2f}')

# 

# Assinatura - int quadrado (int n)
#              {
#                  return n * n
#              }
# Em Python - def quadrado (numero : int) -> int
#                 return n * n

# Procedimentos

# def saudacao(nome: str, hora:int) -> None:
#     if hora < 12:
#         msg = "Bom dia"
    
#     elif hora < 18:
#         msg = "Boa tarde"
#     else:
#         msg = "Boa noite"
#     print(f"{msg}, {nome}, seja bem-vindo a FIAP!")

# saudacao("Davi", 8)

lista = []

def preencher_lista(lista: list) -> None:
    valor = input('Digite um valor para a sua lista: ')
    lista.append(valor)

    while valor != '.':
        valor = input('Digite um valor para a sua lista: ')
        

        if valor == '.':
            break

        lista.append(valor)

preencher_lista(lista)
print(lista)

lista_maior_numero = [5, 20, 37, -42, 60]

def maior_numero(lista: list) -> float:
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

print(lista_maior_numero)
print(maior_numero(lista_maior_numero))

def media_lista(lista: list) -> float:
    # media = sum(lista) / len(lista)
    soma = 0
    total = 0
    for i in lista:
        soma += i
        total += 1
    media = soma / total
    return media

print(media_lista(lista_maior_numero))

def contar_pares(lista: list) -> float:
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += 1
    return pares
   
print(contar_pares(lista_maior_numero))

def numeros_acima_media(lista: list) -> list:
    media = media_lista(lista)
    nova_lista = []
    for i in lista:
        if i > media:
            nova_lista.append(i)
    return nova_lista

print(numeros_acima_media(lista_maior_numero))

def remover_negativos(lista: list) -> list:
    lista_negativos = []
    for i in lista:
        if i < 0:
            lista_negativos.append(i)
    for i in lista_negativos:
        lista_maior_numero.remove(i)
    return lista_maior_numero

print(remover_negativos(lista_maior_numero))

def retorna_mais_proximo(lista: list, valor: float) -> float:
    valor = float(input('Digite um valor: '))
    
    for i in lista:
        if valor == i:
            return valor
        
        if valor != i:
            valor_proximo = (i - valor) + valor   
        return valor

valor = 7
print(retorna_mais_proximo(lista_maior_numero, valor))