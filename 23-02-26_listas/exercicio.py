lista_valores = []
valor = input("Digite um valor a ser inserido na lista. Digite '.' para que a lista seja encerrada ")
 
while valor != ".":
    lista_valores.append(valor)
    valor = input("Digite um valor a ser inserido na lista. Digite '.' para que a lista seja encerrada ")
    if valor == ".":
        break
 
lista_num = []
lista_outros_valores = []
 
for valor in lista_valores:
    if valor.isnumeric():
        valor_int = int(valor)
        lista_num.append(valor_int)
    else:
        lista_outros_valores.append(valor)
 
print(lista_valores)
print(lista_num)
print(lista_outros_valores)

soma_lista = sum(lista_num)
qtd_elementos_lista = len(lista_num)
    
print(f"A soma dos valores da lista é {sum(lista_num)}")
print(f"A lista tem {len(lista_num)} elemento(s)!")
lista_crescente = lista_num.copy()
lista_crescente.sort()
print(f"A lista em ordem crescente fica:{lista_crescente}")
lista_decrescente = lista_num.copy()
lista_decrescente.sort(reverse=True)
print(f"A lista em ordem decrescente fica:{lista_decrescente}")
 
lista_crescente.extend(lista_outros_valores)
 
print(f"Essa é a lista com os dados numéricos em ordem crescente e os demais no final: {lista_crescente}")