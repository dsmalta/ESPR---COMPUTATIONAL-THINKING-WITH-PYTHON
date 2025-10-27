# Tabuada
num_escolhido = int(input("Escolha um numero: "))
multiplo = 1
for multiplo in range (multiplo, 11, 1):
    tabuada = num_escolhido * multiplo
    print(tabuada)
    tabuada += 1
    
# Contagem 
for numeros in range (1, 51, 1):
    print(numeros)
    
# Fatorial
num_escolhido = int(input("Numero escolhido: "))
resultado = 1

for numeros in range(num_escolhido, 0, -1):
    resultado = resultado * numeros
    print(resultado)