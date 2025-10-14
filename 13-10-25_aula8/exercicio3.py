# Exemplo
# nota = float(input("Digite uma nota: "))
# while nota < 0 or nota > 10:
#     nota = float(input(("Nota inválida! Tente novamente!\nDigite uma nota: ")))

# print(f"Nota {nota}")
    

# usando o continue
while True:
    nota = float(input("Nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida! Tente novamente!")
        continue # volta para linha 11
    else:
        break # acaba o programa

print(f"Nota: {nota}")
    
    