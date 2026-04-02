nomes = []
n1 = []
n2 = []
media = []


# Essa funcao recebe dois valores e faz media deles
def calcula_media(vm1: float, vm2: float) -> float:
    media_calculo = (vm1 + vm2)/ 2
    media.append(media_calculo)
    return media_calculo

# Essa funcao recebe um valor de input e retorna True ou False dependendo da condicao
def confere_nota(v_input: float) -> bool:
    while (0 <= v_input <= 10):
       return True 
    else:
        return False
    
# Essa funcao recebe e percorre uma lista dizendo a quantidade de alunos aprovados e reprovados
def aprova_reprova(lista_media: list) -> float:
    alunos_aprovados = 0
    alunos_reprovados = 0
    
    for v_media in lista_media:
        if v_media >= 6:
            alunos_aprovados += 1
        else:
            alunos_reprovados += 1
    return alunos_aprovados, alunos_reprovados
        
def isfloat(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-', '', 1)
    if v[0] == '+':
        v = v.replace('+', '', 1)
    v = v.replace('.','',1)
    return v.isdigit()    

def isint(v: str) -> bool:
    if v[0] == '-':
        v = v.replace('-', '', 1)
    if v[0] == '+':
        v = v.replace('+', '', 1)
    return v.isdigit()

while True:
    print(f'''
          1- Preencher as notas
          2- Exibir o registro do aluno
          3- Exibir os registros
          4- Contar aprovados e reprovados
        ''')
    
    opcao_user = (input("Escolha: "))
    
    # Verifica se o numero escolhido e inteiro
    while not isint(opcao_user):
            print("Digite um número válido.")
            opcao_user = input("Escolha: ")
    opcao_user = int(opcao_user)
    
    # Verifica se o numero escolhido esta entre 1 e 4
    while not (1 <= opcao_user <= 4):
        print("Digite um número válido entre 1 e 4.")
        opcao_user = int(input("Escolha: "))
        
    match opcao_user:

        case 1:
            nome_aluno = input("Nome: ")
            conta_nome = len(nome_aluno.split())
            while not nome_aluno.strip():
                print("O nome nao pode estar vazio") 
                nome_aluno = input("Nome: ")
            while conta_nome < 2:
                print("Digite pelo menos dois nomes.")
                nome_aluno = input("Nome: ")
                conta_nome = len(nome_aluno.split())
            else:
                nomes.append(nome_aluno)

            v_n1 = input("Nota 1: ")

            while not isfloat(v_n1):
                print('Digite uma nota válida.')
                v_n1 = (input("Nota 1: "))
            v_n1 = float(v_n1)
            
            while not confere_nota(v_n1):
                print('Digite uma nota válida entre 0 e 10.')
                v_n1 = (float(input("Nota 1: ")))
            
            n1.append(v_n1)
            
            v_n2 = input("Nota 2: ")

            while not isfloat(v_n2):
                print('Digite uma nota válida.')
                v_n2 = (input("Nota 2: "))
            v_n2 = float(v_n2)
            
            while not confere_nota(v_n2):
                print('Digite uma nota válida entre 0 e 10.')
                v_n2 = (float(input("Nota 2: ")))
            
            n2.append(v_n2)

            calcula_media(v_n1, v_n2)

        case 2:
            escolha_aluno = (input("Digite um número para acessar os registros de um aluno (De 0 ao número de alunos registrados): "))
            
            while not isint(escolha_aluno):
                print("Digite um número válido.")
                escolha_aluno = (input("Digite um número para acessar os registros de um aluno (De 0 ao número de alunos registrados): "))
            escolha_aluno = int(escolha_aluno)
    
            if media[escolha_aluno] >= 6:
                print("-----------------------------------------------------------------")
                print(f"\nNome.........: {nomes[escolha_aluno]}\nNota 1.......: {n1[escolha_aluno]}\nNota 2.......: {n2[escolha_aluno]}\nMédia........: {media[escolha_aluno]}\nAluno Aprovado!\n")
                print("-----------------------------------------------------------------")
            else:
                print("-----------------------------------------------------------------")
                print(f"\nNome.........: {nomes[escolha_aluno]}\nNota 1.......: {n1[escolha_aluno]}\nNota 2.......: {n2[escolha_aluno]}\nMédia........: {media[escolha_aluno]}\nAluno Reprovado!\n")
                print("-----------------------------------------------------------------")

        case 3:
            for nome in range(len(nomes)):
                if media[nome] >= 6:
                    print("-----------------------------------------------------------------")
                    print(f"\nNome.........: {nomes[nome]}\nNota 1.......: {n1[nome]}\nNota 2.......: {n2[nome]}\nMédia........: {media[nome]}\nAluno Aprovado!\n")
                    print("-----------------------------------------------------------------")
                else:
                    print("-----------------------------------------------------------------")
                    print(f"\nNome.........: {nomes[nome]}\nNota 1.......: {n1[nome]}\nNota 2.......: {n2[nome]}\nMédia........: {media[nome]}\nAluno Reprovado!\n")
                    print("-----------------------------------------------------------------")
        
        case 4:
            qtd_aprovados_reprovados = aprova_reprova(media)
            print(f"\nQuantidade de Aprovados: {qtd_aprovados_reprovados[0]}\nQuantidade de Reprovados: {qtd_aprovados_reprovados[1]}")   

        