# Davi de Souza Malta - 560327

num_escolhido = int(input("Número: "))
fatorial = 1

for volta in range(num_escolhido, 0, -1):
    fatorial = fatorial * volta 
    
print(f"Fatorial: {fatorial}")