conta_aluno = 0
alunos_aprovados = 0
alunos_exame = 0
alunos_reprovados = 0
media_turma = 0


# Início do loop de alunos
for conta_aluno in range(10):

    if conta_aluno == 0:
        print(f"ALUNO 1\n")

    else:
        print(f"ALUNO {conta_aluno + 1}")

    nota1 = int(input("Nota 1: "))
    
    # Erro caso digite -1 na nota 1 do primeiro aluno
    if nota1 == -1 and conta_aluno == 1:
        nota1 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))

    # Encerra as médias
    if nota1 == -1 and conta_aluno != 0:
        print("Encerrando médias...\n")
        media_turma = media_turma
        conta_aluno = conta_aluno 
        break

    # Erro caso a nota seja menor que 0 ou maior que 10
    while nota1 < 0 or nota1 > 10:
        nota1 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))

    nota2 = int(input("Nota 2: "))
    # Erro caso a nota seja menor que 0 ou maior que 10
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))

    while conta_aluno == 1 and nota1 == -1:
        nota1 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))
        
    #Calcula a média dos alunos
    media_aluno = (nota1 + nota2)/2

    if media_aluno < 4:
        # Printa que o aluno foi reprovado caso a média não atinja 6 
        print(f"REPROVADO com média {media_aluno:.1f}")
        alunos_reprovados = alunos_reprovados + 1
    elif media_aluno > 3.9 and media_aluno <= 5.9:
        # Printa que o aluno está em exame
        print(f"EXAME com média {media_aluno:.1f}")
        alunos_exame = alunos_exame + 1
    else:   
        # Printa que o aluno foi aprovado caso a média atinja 6
        print(f"APROVADO com média {media_aluno:.1f}")
        alunos_aprovados = alunos_aprovados + 1

    # Armazena os valores das notas 
    media_turma += media_aluno
    conta_aluno = conta_aluno + 1

# Calcula a porcentagem de aprovados
aprov_porcent = (alunos_aprovados / conta_aluno) * 100
# Calcula a procentagem de alunos em exame
exame_porcent = (alunos_exame / conta_aluno) * 100
# Calcula a porcentagem de reprovados
reprov_porcent = (alunos_reprovados / conta_aluno) * 100

# Calcula a média da turma
media_turma = media_turma/conta_aluno

# Exibe os resultados da turma
print(f"\nDADOS CONSOLIDADOS\n Média da turma: {media_turma:.2f}\n Aprovados: {aprov_porcent:.1f}%\n Exame: {exame_porcent:.1f}\n Reprovados: {reprov_porcent:.1f}%")   



    
