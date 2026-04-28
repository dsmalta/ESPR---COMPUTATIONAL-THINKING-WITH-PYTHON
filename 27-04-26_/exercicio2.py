func = {
    'cpf' : 0,
    'nome' : 'Davi de Souza Malta',
    'salario' : 0,
}
    
tabela = []

def adicionar_funcionario(_tabela: list, _func: dict) -> None:
    _tabela.append(_func.copy())

def cadastrar_funcionario(_func: dict, _tabela: list, _cpf: int, _nome: str, _salario: float) -> None:

    print("\nCADASTRANDO FUNCIONÁRIO:")
    print("=" * 30)
    print(f"CPF.....: {_cpf}\n")

    existe = False

    for f in _tabela:
        if f['cpf'] == _cpf:
            existe = True

    if existe:
        print("----------------------")
        print("Funcionário já existe!")
        print("----------------------")
    else:
        _func['cpf'] = _cpf
        _func['nome'] = _nome
        _func['salario'] = _salario

        adicionar_funcionario(_tabela, _func)

        print("----------------------")
        print("Funcionário cadastrado!")
        print("----------------------")

    input("\nPressione ENTER para continuar...")

def listar_funcionario(_tabela: list, _func: dict) -> None:
    for _func in _tabela:
        print(_func)

# def listar_funcionario(_dicionario:)



while True:
    print(f"""
    M E N U
    -------
    0 - SAIR
    1 - Cadastrar Funcionário
          
          
    5 - Listar Funcionário\n""")
    escolha = input("Escolha: ")

    match escolha:

        case '0':
            break

        case '1':
            print("CADASTRANDO FUNCIONÁRIO: ")
            print("=" * 30)
            print()
            cpf = int(input("CPF.....: "))
            nome = input("Nome....: ")
            salario = int(input("Salário.: "))

            cadastrar_funcionario(func, tabela, cpf, nome, salario)
            adicionar_funcionario(tabela, func)

        case '5':
            print("CPF", '' * 10, "NOME", '' * 10, "SALARIO")
            print("=" * 30)
            print(listar_funcionario(tabela, func))
