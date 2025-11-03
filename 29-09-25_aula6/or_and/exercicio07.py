
"""
6. Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 0 e 10 (inclusive) ela é uma
“Nota válida”, senão “Nota inválida”.
"""
import os
os.system("cls")
nota = float(input("Nota: "))

if nota >= 0:
    if nota <= 10:
        print(f"{nota} é uma nota valida!")
    else:
        print(f"{nota} é uma nota INvalida!")
else:
    print(f"{nota} é uma nota INvalida!")

"""
OPERADORES LÓGICOS:
not     - Negação
and     - consjunção
or      - disjuncao
"""

if nota >= 0 and nota <= 10:
    print(f"{nota} é uma nota valida!")
else:
    print(f"{nota} é uma nota INvalida!")    