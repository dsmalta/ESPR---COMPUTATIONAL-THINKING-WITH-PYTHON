import random
# num_sorteado = random.randint(1,10)
# num_tentativas = 1
# print(num_sorteado)

# while num_tentativas != 3:
#     tentativa = int(input("Digite um número para adivinhar: ")) 

#     if tentativa == num_sorteado:
#         print(f"Parabéns! Você acertou em {num_tentativas} tentativa(s)")
#         break
        
#     elif tentativa == 0:
#         break
        
#     elif tentativa != num_sorteado:
#         print("Errou! Tente novamente!")
#         num_tentativas += 1

# if num_tentativas == 3:
#     print(f"Suas tentativas acabaram! O número sorteado era {num_sorteado}")


# Exemplo do Professor
num_secreto = random.randint(1,10)
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    tentativa = int(input(f"Tentativa {tentativas +1}:"))
    tentativas += 1

    if tentativas == 0:
        print("Você desistiu do jogo")
        break

    if tentativas == num_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
        break

    print("Errou! Tente novamente!\n")

else:
    print("Suas tentativas acabaram!")
    print(f"O número secreto era {num_secreto}.")

print("\nFim de jogo!")