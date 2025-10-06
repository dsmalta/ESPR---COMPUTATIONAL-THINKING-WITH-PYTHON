valor_inicial = int(input("Valor Inicial: "))
valor_final = int(input("Valor Final: ")) 

if valor_inicial <= valor_final:  
    while valor_inicial <= valor_final:
        print(valor_inicial)
        valor_inicial = valor_inicial + 1

if valor_final <= valor_inicial:
   while valor_final <= valor_inicial:
       print(valor_final)
       valor_final = valor_final + 1