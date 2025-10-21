num_alunos = int(input("Quantos alunos há na turma? "))
conta_aluno = 1
alunos_aprovados = 0
alunos_reprovados = 0
media_turma = 0

# Início do loop de alunos
while conta_aluno <= num_alunos:
    print(f"\nALUNO {conta_aluno}/{num_alunos}")
    nota1 = int(input("Nota 1: "))
    # Erro caso a nota seja menor que 0 ou maior que 10
    while nota1 < 0 or nota1 > 10:
        nota1 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))
        
    nota2 = int(input("Nota 2: "))
    # Erro caso a nota seja menor que 0 ou maior que 10
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))
        
    #Calcula a média dos alunos
    media_aluno = (nota1 + nota2)/2

    if media_aluno < 6:
        # Printa que o aluno foi reprovado caso a média não atinja 6 
        print(f"Reprovado com média {media_aluno:.1f}")
        alunos_reprovados = alunos_reprovados + 1
    else:
        # Printa que o aluno foi aprovado caso a média atinja 6
        print(f"Aprovado com média {media_aluno:.1f}")
        alunos_aprovados = alunos_aprovados + 1

    # Armazena os valores das notas 
    media_turma += media_aluno
    conta_aluno = conta_aluno + 1

# Calcula a porcentagem de aprovados
aprov_porcent = (alunos_aprovados / num_alunos) * 100
# Calcula a porcentagem de reprovados
reprov_porcent = (alunos_reprovados / num_alunos) * 100

# Calcula a média da turma
media_turma = media_turma/num_alunos

# Exibe os resultados da turma
print(f"\nDADOS CONSOLIDADOS\n Média da turma: {media_turma:.1f}\n Aprovados: {aprov_porcent:.1f}%\n Reprovados: {reprov_porcent:.1f}%")   



    
