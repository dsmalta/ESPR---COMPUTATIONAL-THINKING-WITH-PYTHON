import os
os.system("cls")

dia_semana = input("Digite o dia da semana: ")

match dia_semana:
    case "segunda-feira":
        print("dia da semana")
    case "terça-feira":
        print("dia da semana")
    case "quarta-feira":
        print("dia da semana")
    case "quinta-feira":
        print("dia da semana")
    case "sexta-feira":
        print("dia da semana")
    case "sábado":
        print("final de semana")
    case "domingo":
        print("final de semana")
    case _:
        print("digitou algo errado mano!")



match dia_semana:
    case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
        print("Dia da semana")
    case "sábado" | "domingo":
        print("final de semana")
    case _:
        print("digitou algo errado mano!")

# Dado um caractere, exibir se ele é "Vogal", "Consoante", "Dígito" ou "Caractere especial"