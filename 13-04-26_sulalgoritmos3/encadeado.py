import os 
os.system('cls')

# Definição da função primária
def media2notas(n1: float, n2: float) -> float:
    # Definição da função primária
    if nota_valida(n1) and nota_valida(n2):
        return (n1 + n2) / 2
    else:
        return -1

# Definição.....: Retorna a nota se la for válida ou False se for inválida
# PAR1..........: Nota a ser verificada 
# Type Par1.....: float
# Return........: float / bool (false se não for uma nota)

def nota_valida(nota: float) -> float:
    resp = nota >= 0 and nota <= 10
    if resp == True:
        return nota
    else:
        return False
    
# Uso
nota1 = 9
nota2 = 9.6
retorno = media2notas(nota1, nota2)
if retorno == -1:
    print(f"{nota1} ou {nota2} uma das duas é inválida!")
else:
    print(f"Média = {retorno}")