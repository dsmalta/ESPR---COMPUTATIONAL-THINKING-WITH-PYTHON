import os 
os.system('cls')

def montar_frase(*args) -> str:
    frase = ""
    for palavra in args:
        frase = frase + palavra + " "
    return frase.strip()

# Uso
print(montar_frase("Hoje", "não é", "CP", "Surpresa"))