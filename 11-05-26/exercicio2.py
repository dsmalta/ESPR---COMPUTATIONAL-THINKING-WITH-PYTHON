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

        print("-----------------------")
        print("Funcionário cadastrado!")
        print("-----------------------")

    input("\nPressione alguma tecla para continuar... ")

def listar_funcionario(_tabela: list) -> None:
    print("\nListando os registros")
    
    print(f"{'CPF':<10}{'NOME':<33}{'SALARIO':>15}")
    print("=" * 70)
 
    for func in _tabela:
        print(f"{func['cpf']:>10} | {func['nome']:<30} | {func['salario']:>2.2f}")
 
    input("\nPressione alguma tecla para continuar... ")

def consultar_funcionario(_func: dict, _tabela: list, _cpf: int) -> None:

    existe = False

    func_existe = {}

    for _func in _tabela:
        if _func['cpf'] == _cpf:
            existe = True
            func_existe = _func
                
    if existe: 
        print(f"\nCPF.....: {func_existe['cpf']} ")
        print(f"Nome....: {func_existe['nome']}")
        print(f"Salário.: {func_existe['salario']}")

    else:
        print("------------------------")
        print("Funcionãrio inexistente!")
        print("------------------------")

    input("\nPressione alguma tecla para continuar... ")



while True:
    print(f"""
    M E N U
    -------
    0 - SAIR
    1 - Cadastrar Funcionário
    2 - Consultar Funcionário   
          
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

        case '2':
            print("CONSULTANDO FUNCIONÁRIO")
            print("=" * 23)
            print()
            cpf = int(input("CPF.....: "))
            
            consultar_funcionario(func, tabela, cpf)

        case '5':
            print(listar_funcionario(tabela))
