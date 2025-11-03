# REVISÃO LAÇOS CONDICIONAIS

# EXEMPLO 
# Exibir os números de 1 a 10.

# laço pré-condicional - enquanto - while <condicao>
# Situações 0,N. Analisa primeiro depois executa uma ação
print("Com o while")
volta = 1
while volta <= 10:
    print(volta)
    volta = volta + 1

# laço pós condicional - repita - while True
# Situação 1,N. Executa uma ação depois analisa
print("Com o while True")
volta = 1
while True:
    print(volta)
    volta = volta + 1
    if volta > 10:
        break

# laço contador - para - for 
# Situações onde o numéro de voltas é previsível
print("Com o for")
for volta in range (1, 11, 1):
    print(volta)