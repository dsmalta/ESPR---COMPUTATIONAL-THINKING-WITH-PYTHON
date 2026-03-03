# ------ Criação dos módulos
# --- Procedimentos

# Sem parâmetros
def saudacao():
    nome = input('Qual seu nome? ')
    print(f'Boa noite, {nome}, seja bem-vindo!')

# Com parâmetros (argumentos)
def saudacao2(nome):
    print(f'Boa noite, seja bem-vindo, {nome}!')

def saudacao3(nome, hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else: 
        msg = "Boa noite"

    print(f'{msg}, seja bem-vindo, {nome}!')
    
# ------ Programa Principal
import os
os.system('cls')
saudacao()
x = 'Edson'
saudacao2(x)
saudacao3("Davi", 17)