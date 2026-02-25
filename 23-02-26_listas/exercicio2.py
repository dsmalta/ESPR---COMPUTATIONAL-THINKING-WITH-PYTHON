import os


while True:
    user_input = int(input('''
MENU

0 - SAIR
1 - Criar / Iniciar uma lista 
2 - Inserir um elemento na lista
3 - Inserir elementos até digitar ponto (.)
4 - Remover elemento pelo índice
5 - Remover elemento pelo conteúdo
6 - Listar a lista
                   
Escolha: '''))
    
    match user_input:
        case 1:
            nova_lista = list()
            print(f'Lista criada com sucesso! {nova_lista}')
        
        case 2:
            novo_elemento = input('Digite um valor a ser adicionado a lista: ')
            nova_lista.append(novo_elemento)
        
        case 3:
            novo_elemento = input('Digite um valor a ser adicionado a lista, caso queira encerrar a lista, digite (.): ')
            while novo_elemento != ".":
                nova_lista.append(novo_elemento)
                novo_elemento = input('Digite um valor a ser adicionado a lista, caso queira encerrar a lista, digite (.): ')
        
        case 4:
            remove_indice = int(input("Escolha um número para remover um elemento pelo seu índice: "))
            nova_lista.pop(remove_indice)
        
        case 5:
            remove_conteudo = input("Escreva o conteúdo de um elemento para ser removido da lista: ")
            nova_lista.remove(remove_conteudo)
            print(nova_lista)
            
        case 6:
            print(nova_lista)
    
        case 0:
            print('Finalizando aplicação...')
            os.system('cls')
            break
            
    