valor_inicial = int(input("Valor Inicial: "))
valor_final = int(input("Valor Final: "))

if valor_inicial > valor_final:
    print("Impossível exibir o intervalo")

while valor_inicial <= valor_final:
    print(valor_inicial)
    valor_inicial = valor_inicial + 1
