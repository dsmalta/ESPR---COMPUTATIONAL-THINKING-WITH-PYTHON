
"""
6. Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma
“Nota válida”, senão “Nota inválida”.

7. Dadas duas notas, calcular e exibir a média simples das mesmas. Caso a média seja inferior a 5
exibir “Você está reprovado”, senão exibir “Você está aprovado”.
"""
import os
os.system("cls")
nota1 = float(input("Nota 1: "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        if media < 5:
            print(f"Reprovado com media {media}")
        else:
            print(f"Aprovado com media {media}")
    else:
        print(f"A nota 2 {nota2} é inválida")
else:
    print(f"A nota 1 {nota1} é inválida")
