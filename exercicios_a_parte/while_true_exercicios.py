# Menu Simples
while True:
    escolha = input(f"1 - Dizer Ola \n2 - Dizer Tchau \n0 - Sair")
    
    if escolha == "1":
        print('\nOla! ')
        
        
    elif escolha == "2":
        print("\nTchau! ")
    
    elif escolha == "0":
        break
    
# Validacao de entrada 

while True:
    num_escolhido = 8
    
    num_adivinha = int(input("Tente adivinhar o numero de um a dez "))
    
    if num_adivinha != num_escolhido:
        num_adivinha = int(input("Tente novamente! "))
        
    elif num_adivinha == num_escolhido:
        print("Voce acertou o numero!")
        break
    
