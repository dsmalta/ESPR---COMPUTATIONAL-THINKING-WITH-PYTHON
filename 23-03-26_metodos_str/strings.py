import os
os.system("cls")

frase = "Agora veremos como funciona o fatiamento com strings"
print(frase)
print(frase[4])
for carac in frase:
    print(carac, end = " ")
print()

print(frase[7:15])
print(frase[2:30:2])
print(frase[::-1])

# Exercício:
# 1. Crie uma função que passe uma frase por parâmetro e substitua
# todas as vogais por ponto de interrogação (?), retornando a frase
# modificada

def troca_vogais(frase: str) -> str:
    new_frase = list()
    vogais = "AEIOU"
    for i in range(len(frase)):
        if frase[i].upper() in vogais:
            new_frase.append("?")
        else:
            new_frase.append(frase[i])
    return new_frase
        

frase = "Edson de Oliveira"
print(frase)
new_frase = troca_vogais(frase)
print(new_frase)
print("".join(new_frase))
# >> ?ds?n de ?l?v??r?