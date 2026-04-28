"""
Exercício:

Dado o menu abaixo, faça um programa (usando subalgoritmos) que manipule um dicionário.
0 - SAIR
1 - Preencher
2 - Exibir
3 - Editar
4 - Adicionar Key
"""

import os
os.system('cls')
aluno = {
    'rm': '',
    'nome': '',
    'nota': 0
}

# ------ Subalgoritmos 
def preencher(_dicionario: dict, _rm: str, _nome: str, _nota: float) -> None:
    _dicionario["rm"] = _rm
    _dicionario["nome"] = _nome
    _dicionario["nota"] = _nota

def exibir(_dicionario: dict) -> None:
    if len(_dicionario) == 0:
        print("O dicionário está vazio!")
    else:
        for chave, valor in _dicionario.items():
            print(f"{chave}: {valor}")

def editar(_dicionario: dict, _chave: str, _valor: str) -> None:
    if _chave in _dicionario:
        _dicionario[_chave] = _valor
        print("Registro Editado!")
    else: 
        print("Chave não encontrada!")

def adicionar_chave(_dicionario: dict, _nova_chave: str) -> None:
    if _nova_chave not in _dicionario:
        _dicionario(_nova_chave) == ""
        print(f"A chave {_nova_chave} foi adicionada!")
    else:
        print(f"A chave {_nova_chave} já existe!")

# ------ Programa Principal
while True:
    print("""
    M E N U
    -------
    0 - SAIR
    1 - Preencher
    2 - Exibir
    3 - Editar
    4 - Adicionar Key""")
    opcao = input("Opção: ")

    match opcao:
        case '0': 
            break
        case '1':
            rm = input("RM.......: ")
            nome = input("NOME....: ")
            nota = input("NOTA....: ")
            preencher(aluno, rm, nome, nota)
        case '2':
            exibir(aluno)
        case '3':
            chave = input("Chave: ")
            valor = input("Valor: ")
            if chave == "nota":
                valor = float(valor)
            editar(aluno, chave, valor)
        case '4':
            nova_chave = input("Nova chave: ")
            adicionar_chave(aluno, nova_chave)
        case _:
            print("Opção inválida!")
            