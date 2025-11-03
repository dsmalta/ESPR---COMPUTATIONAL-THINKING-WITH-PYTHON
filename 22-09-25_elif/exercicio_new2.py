venda_user = float(input("Digite um valor: "))
escolha_pagamento = input("Qual sera a forma de pagamento? 1- A vista 2- Cartao ")

if escolha_pagamento == "1":
    reajuste = venda_user * 0.035 # 3.5% de desconto
else:
    reajuste = venda_user * 0.0275 # 2.75% de acrescimo
    
reajuste = venda_user + reajuste

print(f"Venda: {venda_user}")
print(f"Reajustado: {reajuste}")
    

