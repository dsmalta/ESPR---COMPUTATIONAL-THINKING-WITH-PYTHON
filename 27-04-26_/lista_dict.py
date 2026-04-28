import os 
os.system('cls')

tabela = list() # Lista
pessoa = dict() # Dicionário

pessoa["nome"] = input("Nome: ")
pessoa["idade"] = int(input("Idade: "))
tabela.append(pessoa.copy())

pessoa["nome"] = input("Nome: ")
pessoa["idade"] = int(input("Idade: "))
tabela.append(pessoa)

'''
print(pessoa)
print(tabela)


for i in range(2):
    print(f"Nome: {tabela[i]["nome"]}")
    print(f"idade: {tabela[i]["idade"]}")
'''

for registro in tabela:
    for x, y in registro.items():
        print(x)
        print(y)