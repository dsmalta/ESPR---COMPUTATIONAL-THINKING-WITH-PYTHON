num_alunos = int(input("Quantos anos há na turma? "))
# media_aluno = nota1 + nota2/ 2
conta_aluno = 1
alunos_aprovados = 0
alunos_reprovados = 0
media_turma = 0

while conta_aluno <= num_alunos:
    print(f"\nALUNO {conta_aluno}/{num_alunos}")
    nota1 = int(input("Nota 1: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))
        continue
    
    nota2 = int(input("Nota 2: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input("Digite uma nota válida entre 0 e 10. Nota: "))
        continue

    media_aluno = (nota1 + nota2)/2

    if media_aluno < 6: 
        print(f"Reprovado com média {media_aluno:.1f}")
        alunos_reprovados = alunos_reprovados + 1
    else:
        print(f"Aprovado com média {media_aluno:.1f}")
        alunos_aprovados = alunos_aprovados + 1

    media_turma += media_aluno
    conta_aluno = conta_aluno + 1

aprov_porcent = (alunos_aprovados / num_alunos) * 100
reprov_porcent = (alunos_reprovados / num_alunos) * 100

media_turma = media_turma/num_alunos
print(f"\nDADOS CONSOLIDADOS\n Média da turma: {media_turma:.1f}\n Aprovados: {aprov_porcent:.1f}%\n Reprovados: {reprov_porcent:.1f}%")   



    
