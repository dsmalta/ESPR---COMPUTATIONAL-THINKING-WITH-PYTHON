import os
os.system("cls")

aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}

# estrutura do dicionario
print(aluno)

# Exemplos de manuseio
usuario = "Carlos"
if aluno["nome"] == usuario:
    print("Nome correto")
else:
    print(f"Não! O nome é {aluno["nome"]}")

print(aluno["idade"])
# print(aluno["nota"])
print(aluno.get("nota", "Key nome inexistente"))
print(aluno.get("curso", "Key curso inexistente"))


aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}

# modificando valores (values) no dicionario
os.system("cls")
print(aluno)
aluno["idade"] = 50
print(aluno)

# aluno["nome"] = input("Nome: ")
print(aluno)

# adicionando novas keys
aluno = {
    #   item
    # key : value
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}
os.system("cls")
print(aluno)
aluno["nota"] = 7.5
print(aluno)

# remover um item
aluno = {
    #   items
    #   item
    # key : value
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}
os.system("cls")
print(aluno)
aluno.pop("curso")
print(aluno)
del aluno["idade"]
print(aluno)

aluno.clear()
print(aluno)

aluno = {
    #   item
    # key : value
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}
print(aluno)
# del aluno
print(aluno)

# outros métodos
os.system("cls")

aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}
print(aluno)

print(aluno.keys()) # retorna uma lista somete com as keys

print(aluno.values()) # retorna uma lista somete com os values

print(aluno.items()) # retorna todas as linhas
os.system("cls")
print(aluno)
aluno.update({"nome":"Ana"}) # pode alterar tanto a key quanto o value
print(aluno)

# aplicação dos métodos
os.system("cls")

aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "ES",
}

print(aluno.keys())

for posicao, chave in enumerate(aluno.keys()):
    print(f"{posicao+1}.o - {chave.capitalize()}: ")

print()

for posicao, valor in enumerate(aluno.values()):
    print(f"{posicao+1}.o - {valor} ")

print()

for chave, valor in aluno.items():
    print(f"{chave}: {valor} ")

# Dicionario de dicionários
os.system("cls")

turma = {
    "aluno1" : {"nome":"Edson", "nota":10},
    "aluno2" : {"nome":"Maria", "nota":6},
}
print(turma)

# como imprimir a nota da maria?
print(f"Nota da Maria: {turma['aluno2']['nota']}")

# Exibindo o relatório com todas as informações
os.system("cls")

turma = {
    "aluno1" : {"nome":"Edson", "nota":10},
    "aluno2" : {"nome":"Maria", "nota":6},
}
print("RELATÓRIO COMPLETO:")
for chave, dados in turma.items():
    print(f"ID.....: {chave}")
    print(f"Nome...: {dados['nome']}")
    print(f"Nota...: {dados['nota']}")
    print("-" * 20)

# utilizando subalgoritmos


def exibe_registro_aluno(id_aluno: str, dados: dict) -> None:
    print(f"ID.....: {id_aluno}")    
    for campo, valor in dados.items():
        print(f"{campo.capitalize()}: {valor}")
    print("-" * 20)
   

def exibe_turma(turma: dict) -> None:
    print("Registros :")
    for id_aluno, dados in turma.items():
        exibe_registro_aluno(id_aluno, dados)

# uso
os.system("cls")

turma = {
    "aluno1" : {"nome":"Edson", "nota":10},
    "aluno2" : {"nome":"Maria", "nota":6},
}

exibe_turma(turma)


"""
Crie um dicionario vazio "mortal" (apenas um)

Crie o menu:
0 - Zerar dicionario
1 - Inserir Key
2 - Preencher dicionario
3 - Listar dicionario
4 - Remover Key
6 - Sair

"""