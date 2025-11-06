import os
os.system ("cls")

# Lista de vagas (começa com todas liberadas)
vagas = [0,0,0,0,0,0,0,0,0,0]

while True:
    print(f"""
          1 - Mostrar estado das vagas
          2 - Ocupar uma vaga
          3 - Liberar uma vaga
          4 - Encerrar o programa
          """)
    
    # Escolha do usuário sobre o que deseja fazer
    opcao = int(input(f"Escolha: "))
    
    # Enquanto o usuário não digitar uma opção válida, vai exibir uma mensagem de erro
    while opcao < 1 or opcao > 4:
        opcao = int(input(f"Opção inválida, digite um valor entre 1 e 4. "))
        
    
    match opcao:
        
        # Primeira opção: mostrar o estado das vagas
        case 1:
            for ind in range (10):
                num_vaga = ind + 1
                if vagas[ind] == 0:
                    print(f"Vaga {num_vaga}: Livre ") 
                else:
                    print(f"Vaga {num_vaga}: Ocupada")
                    
        # Segunda opção: ocupar uma vaga
        case 2:
            opcao_ocupa_vaga = int(input(f"Qual vaga você deseja ocupar? "))
            
            # Mensagem de erro caso o número inserido seja inválido 
            while opcao_ocupa_vaga < 1 or opcao_ocupa_vaga > 10:
                opcao_ocupa_vaga = int(input((f"Insira uma vaga válida entre 1 e 10. Vaga: ")))
                
            ind = opcao_ocupa_vaga - 1 
            
            if vagas[ind] == 0:
                vagas[ind] = 1
                print(f"Vaga ocupada com sucesso!")
               
            else:
                print(f"Essa vaga já está ocupada.")
                
        # Terceira opção: liberar uma vaga
        case 3:
            opcao_libera_vaga = int(input(f"Qual vaga você deseja liberar? "))
            
            # Mensagem de erro caso o número inserido seja inválido
            while opcao_libera_vaga < 1 or opcao_libera_vaga > 10:
                opcao_libera_vaga = int(input((f"Insira uma vaga válida entre 1 e 10. Vaga: ")))
            
            ind = opcao_libera_vaga - 1
            if vagas[ind] == 1:
                vagas[ind] = 0
                print(f"Vaga liberada com sucesso!")
            else: 
                print(f"Essa vaga já está liberada.")
                
        # Última opção de encerrar o programa
        case 4:
            break
    