resposta = "s"
qtdMedia= 0

while resposta == "s":
    valor1 = int(input("Me dê o primeiro valor "))
    valor2 = int(input("Me dê o segundo valor "))

    media = (valor1 + valor2)/2

    print(f"A média dos dois valores é {media:.2f}\n")
    qtdMedia = qtdMedia + 1
    resposta = input("Deseja continuar? <s>im ou <n>ão? ")
    resposta = resposta.lower()

if resposta == "n":
    print(f"Você executou o programa {qtdMedia} vezes.")
    
    