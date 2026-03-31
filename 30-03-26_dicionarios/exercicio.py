nome = []
n1 = []
n2 = []
media = []

def calcula_media(vm1: float, vm2: float) -> float:
    media_calculo = (vm1 + vm2)/ 2
    media.append(media_calculo)
    return media
        
while True:
    print(f'''
          1- Preencher as notas
          2- Exibir o registro do aluno
          3- Exibir os registros
          4- Contar aprovados e reprovados
        ''')
    
    opcao_user = int(input("Escolha: "))
    if opcao_user <= 0 or opcao_user > 4:
        ('Opção inválida. Digite um número de 1 a 4')

    match opcao_user:

        case 1:
            nome_aluno = input("Nome: ")
            conta_nome = len(nome_aluno.split())
            while conta_nome < 2:
                print("Digite pelo menos dois nomes.")
                nome_aluno = input("Nome: ")
                conta_nome = len(nome_aluno.split())
            else:
                nome.append(nome_aluno)


            v_n1 = float(input("Nota 1: "))
            n1.append(v_n1)

            if v_n1 > 10 or v_n1 < 0:
                print('Digite uma nota válida entre 0 e 10.')
                v_n1 = float(input("Nota 1: "))
            n1.append(v_n1)
            
            v_n2 = float(input("Nota 2: "))

            if v_n2 > 10 or v_n2 < 0:
                print('Digite uma nota válida entre 0 e 10.')
                v_n2 = float(input("Nota 2: "))
            n2.append(v_n2)

            calcula_media(v_n1, v_n2)

        case 2:
            escolha_aluno = int(input("Digite um número para acessar os registros de um aluno (De 0 ao número de alunos registrados): "))
            print(f"Nome: {nome[escolha_aluno]}, Nota 1: {n1[escolha_aluno]}, Nota 2: {n2[escolha_aluno]}, Média: {media[escolha_aluno]}")

        case 3:
            print(f"")

        