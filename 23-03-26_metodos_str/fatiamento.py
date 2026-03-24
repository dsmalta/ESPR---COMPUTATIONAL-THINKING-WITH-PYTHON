import os
os.system("cls")

# Fatiamento
# Sintaxe lista[inicio : fim : passo]
#          0   1   2   3   4   5   6   7   8   9
#         -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numeros)
numeros_parte = numeros[3:7]
print(numeros)
print(numeros_parte)
print(numeros[-4:-1])
print(numeros[1:8])
print(numeros[1:8:3])
print(numeros[8:1:-2])
print(numeros[-3::]) # printa a partir do -3 para trás
print(numeros[::-1]) # printa a lista toda a partir do 9