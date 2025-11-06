import os
os.system ("cls")

vagas = [0,0,0,0,0,0,0,0,0,0]

while True:
    print(f"""
          1 - Mostrar estado das vagas
          2 - Ocupar uma vaga
          3 - Liberar uma vaga
          4 - Encerrar o programa
          """)
    
    opcao = int(input("Escolha: "))
    
    while opcao < 1 or opcao > 4:
        opcao = int(input("Opção inválida, digite um valor entre 1 e 4. "))
        
    match opcao:
        case 1:
            for ind in range (10):
                num_vaga = ind + 1
                if vagas[ind] == 0:
                    print(f"Vaga {num_vaga}: Livre ") 
                else:
                    print(f"Vaga {num_vaga}: Ocupada")
        case 2:
            opcao_ocupa_vaga = int(input("Qual vaga você deseja ocupar? "))
            ind = opcao_ocupa_vaga - 1   
            if vagas[ind] == 0:
                vagas[ind] = 1
                print(f"Vaga ocupada com sucesso!")
                        
            else:
                print(f"Essa vaga já está ocupada.")
                
        
        case 3:
            opcao_libera_vaga = int(input("Qual vaga você deseja liberar? "))
            ind = opcao_libera_vaga - 1
            if vagas[ind] == 1:
                vagas[ind] = 0
                print(f"Vaga liberada com sucesso!")
            else: 
                print(f"Essa vaga já está liberada.")
        case 4:
            break
    