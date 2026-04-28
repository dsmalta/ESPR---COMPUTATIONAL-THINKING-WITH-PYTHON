func = {
    'cpf' : 0,
    'nome' : '',
    'salario' : 0,
}
    
tabela = []

def adicionar_funcionario(_tabela: list, _func: dict) -> None:
    _tabela.append(_func.copy())

def funcionario_existente(_tabela: list, _cpf: int) -> bool:
    for funcionario in _tabela:
        if funcionario['cpf'] == _cpf:
            return True
    return False

def cadastrar_funcionario(_func: dict, _tabela: list, _cpf: int, _nome: str, _salario: float) -> None: 
    _func['cpf'] = _cpf
    _func['nome'] = _nome
    _func['salario'] = _salario

    adicionar_funcionario(_tabela, _func)
    resposta = 'Cadastrado com sucesso!'
    print(f"\n{'!' * (len(resposta) + 1)}")
    print(resposta)
    print('!' * (len(resposta) + 1))
    input('\nPressione uma tecla para continuar...')    
    
     
def listar_funcionario(_tabela: list, _func: dict) -> None:
    for _func in _tabela:
        print(_func)

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
            mensagem = "\nCADASTRANDO FUNCIONÁRIO:"
            print(mensagem)
            print("=" * len(mensagem))
            print()
            cpf = int(input("CPF.....: "))
            
            if funcionario_existente(tabela, cpf):
                resposta = "Funcionario ja existente"
                print(f"\n{'-' * (len(resposta) + 1)}")
                print(resposta)
                print('-' * (len(resposta) + 1))
                input('\nPressione uma tecla para continuar...')
            else:
                nome = input("Nome....: ")
                salario = int(input("Salário.: "))
                cadastrar_funcionario(func, tabela, cpf, nome, salario)

        case '5':
            print("CPF", '' * 10, "NOME", '' * 10, "SALARIO")
            print("=" * 30)
            listar_funcionario(tabela, func)
