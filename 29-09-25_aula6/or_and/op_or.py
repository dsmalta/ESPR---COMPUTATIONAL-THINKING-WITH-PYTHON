import os
os.system("cls")
sorteado = 5
print("Duas tentativas")
tentativa1 = int(input("Adivinhe um numero entre 1 e 5:"))
if tentativa1 == 5:
    print("Acertou")
else:
    tentativa2 = int(input("ERROU! Adivinhe um numero entre 1 e 5:"))
    if tentativa2 == 5:
        print("Acertou")
    else:
        print("Errou, duas tentativas esgotadas")




if tentativa1 == 5 or tentativa2 == 5:
    print("Acertou")
else: 
    print("Errou, duas tentativas esgotadas")