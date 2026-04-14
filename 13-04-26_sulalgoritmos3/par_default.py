import os 
os.system('cls')

def saudacao(usuario: str = "Edson", hora: int = 8) -> None:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else: 
        msg = "Boa noite"
    
    print(f"{usuario}, {msg}! Seja bem-vindo!")

# Uso
saudacao() # "Edson, Bom dia! Seja bem-vindo"
saudacao("Davi") # sobrepõe os parâmetros default, "Davi, Bom dia! Seja bem-vindo!"
saudacao("João", 14) # "João, Boa tarde! Seja bem-vindo!"
saudacao(hora = 20) # Considera o nome como o padrão já definido e muda a hora(nesse caso "Edson")