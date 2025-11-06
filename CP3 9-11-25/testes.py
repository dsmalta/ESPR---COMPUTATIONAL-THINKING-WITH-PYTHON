v = [1,0,0,0,0,1,0,1,0,0]

# Mostrar estado das vagas
# for ind in range (10):
#     num_vaga = ind + 1
    
#     if v[ind] == 0:
#         print(f"Vaga {num_vaga}: Livre ")
        
#     else:
#         print(f"Vaga {num_vaga}: Ocupada")
        
# Pedir ao usuario o numero da vaga que deseja ocupar
# opcao_num_vaga = int(input("Qual vaga voce deseja ocupar? "))

# ind = opcao_num_vaga - 1
    
# if v[ind] == 0:
#     v[ind] = 1
#     print(f"Vaga ocupada com sucesso!")
        
# else:
#     print(f"Essa vaga já está ocupada.")

# Pedir ao usuario o numero da vaga que deseja ocupar
opcao_libera_vaga = int(input("Qual vaga você deseja liberar? "))
    
ind = opcao_libera_vaga - 1

if v[ind] == 1:
    v[ind] = 0
    print(f"Vaga liberada com sucesso!")

else: 
    print(f"Essa vaga já está liberada.")
    
