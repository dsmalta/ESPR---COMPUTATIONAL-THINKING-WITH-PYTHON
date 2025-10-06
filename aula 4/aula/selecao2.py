num = int(input("digite um numero: "))

match num:
    case 1:
        print("Voce digitou um")
    case 2:
        print("Voce digitou dois")
    case 3:
        print("Voce digitou tres")
    case 4:
        print("Voce digitou quatro")
    case 5:
        print("Voce digitou cinco")
    case 6:
        print("Voce digitou seis")
    case _: # Opcional. caso nao entre nas opcoes anteriores, cai aqui
        print("Numero nao previsto!")

# Exercicio:
# 1. dado um numero, exiba o mes correspondente