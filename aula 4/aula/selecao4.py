# Dado um caractere, exibir se ele é "Vogal", "Consoante", "Dígito" ou "Caractere especial"
carac = input("Digite um caractere:")
match carac.upper():
    case 'A' | 'E' | 'I' | 'O' | 'U':
        print("Vogais")
    case cons if cons > "A" and cons <= "Z":
        print("consoante")
    case dig if dig > "0" and dig <= "9":
        print("digitos")
    case _:
        print("Carateres especiais")

# Calculadora: Dados dois valores e um sinal, calcular a operacao correspondente. 
# Lembre-se que na divisão o segundo valor nao pode ser zero
# Sinais:
# - soma
# - subtracao
# - multiplicacao
# - divisao
# - módulo
# - divisao inteira
# - exponenciacao
