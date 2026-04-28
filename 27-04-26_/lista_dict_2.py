def preenche_registro(p: dict) -> None:
    # Cria o dicionário e preenche as Keys
    p["nome"] = input("Nome: ")
    p["idade"] = int(input("Idade: "))

def add_registro(t: list, p: dict) -> None:
    # Grava o registro (item na lista)
    t.append(p.copy())

def exibe_tabela(t: list) -> None:
    for registro in t:
        for k, v in registro.items():
            print(f"{k} -> {v}")
        print(30*'-')

# Uso
tabela = []   # lista
pessoa = {}   # dicionario

# Adiciona dois registros na tabela
print(f"\nPreenchendo 2 registros:\n" + ("="*len("Preenchendo 2 registros")) + "\n")
preenche_registro(pessoa)
add_registro(tabela, pessoa)
preenche_registro(pessoa)
add_registro(tabela, pessoa)

# Exibe a tabela
print(f"\nExibindo Registros\n" + ("="*len("Exibindo Registros")) + "\n")
exibe_tabela(tabela)    
