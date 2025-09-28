# Davi de Souza Malta RM560327

# Perguntas ao usuários sobre o preço de cada bloco e o preço da mão de obra

pergunta_valor_bloco = float(input("Qual será o valor dos blocos?")) # Pergunta ao usuário qual será o valor dos blocos e dá print nesse valor
perguntaValor_mao_obra = float(input("Qual será o valor da mão de obra por metro quadrado?")) # Pergunta ao usuário qual será o valor da mão de obra e dá print nesse valor

# Item 1
# Calcular a área do muro
altura_muro = float(input("Qual é a altura do muro?")) # altura do muro em metros
largura_muro = float(input("Qual é a largura do muro?")) # largura do muro em metros
area_muro = largura_muro * altura_muro # área de um retângulo é igual a base * altura
print(f"A área do muro é de {area_muro} metros.")

# Item 2 
# Quantidade de blocos
altura_bloco = 0.2 # altura de cada bloco em metros 
largura_bloco = 0.4 # largura de cada bloco em metros
area_bloco = largura_bloco * altura_bloco # área de cada bloco 
qtd_blocos = area_muro/area_bloco # divisão da área de cada bloco pela área do muro para saber a quantidade necessária de blocos
print(f"São necessários {qtd_blocos} blocos para cobrir a área do muro.")

# Item 3
# Perda de Blocos
qtd_blocos_emendas = qtd_blocos + (qtd_blocos * 0.1) # Aqui achamos quantos blocos teremos considerando emendas ou quebras, multiplicar por 0.1 é o mesmo que multiplicar por 10% 
print(f"Considerando quebras e emendas, a quantidade de blocos necessária é {qtd_blocos_emendas}.")

# Item 4
# Custo dos Blocos
custo_blocos = qtd_blocos_emendas * pergunta_valor_bloco # multiplicação da nova quanitdade de blocos pelo preço por bloco para acharmos o preço total
print(f"O valor total gasto com a compra de cada bloco é de R${custo_blocos}.")

# Item 5
# Custo da Mão de Obra
custo_mao_obra = perguntaValor_mao_obra * area_muro
print(f"O valor total gasto com a mão de obra é de {custo_mao_obra}")
 
# Item 6
# Orçamento Final

orcamento_final = custo_blocos + custo_mao_obra
print(f"O valor final do orçamento é de R$ {orcamento_final}.") 