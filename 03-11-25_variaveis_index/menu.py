import os
os.system("cls")

v = [45, -89, 32, -12, 33]

while True:
    os.system("cls")
    print(f"""
          0 - SAIR
          1 - Fazer uma rotina que exiba o primeiro elemento do vetor.
          2 - Fazer uma rotina que exiba apenas os números ímpares.
          3 - Fazer uma rotina que somente os elementos negativos.
          4 - Fazer uma rotina que some os elementos do vetor.
          5 - Fazer uma rotina que calcule a média do vetor.
          6 - Fazer uma rotina que exiba na tela a soma dos elementos pares.
          7 - Fazer uma rotina que peça para o usuário preencher todos os elementos do vetor.
          8 - Fazer uma rotina que peça para o usuário preencher um índice específico do vetor.
          """)
    opcao = input("Escolha: ")
    match opcao:
        case '0':
            break
        case '1':
            print(v[0])
        case '2':
            for ind in range (1, 5, 1):
                if v[ind] % 2 != 0:
                    print(v[ind], end = " ")
        case '3':
            for ind in range (1, 5, 1):
                if v[ind] < 0: 
                    print(v[ind])
        case '4':
            soma = 0
            for ind in range (5):
                soma += v[ind]
                print(soma)
        case '5':
            tamanho_lista = len(v)

            soma_lista = 0 
            for ind in range (5):
                soma_lista += v[ind]
                media_lista = soma_lista / tamanho_lista
            print(media_lista)
        case '6': 
            soma_elementos_pares = 0
            for ind in range (5):
                if v[ind] % 2 == 0:
                    soma_elementos_pares += v[ind]
            print(soma_elementos_pares)
        case '7':
            for ind in range (5):
                v[ind] = int(input("Digite um valor para o índice: "))

            print(v)
        case '8':
            for ind in range(5):
                ind = int(input("Digite um índice para mudar seu valor: "))
                escolha_usuario = ind
                
                if ind == escolha_usuario:
                    v[ind] = int(input("Digite um valor para o índice escolhido: "))
                    break

            print(v)


    input("\nPressione algo para continuar . . . ")