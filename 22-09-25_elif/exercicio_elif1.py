venda_user = float(input("Digite um valor: "))
escolha_pagamento = int(input("Escolha uma forma de pagamento: 1- Pix ou Dinheiro 2- Cartao de Debito 3- Cartao de Credito"))

if escolha_pagamento == 1:
    reajuste = venda_user * 0.88 # 12% de desconto
elif escolha_pagamento == 2:
    venda_user = venda_user # Nenhum desconto
else:
    reajuste = venda_user * 1.0375 # 3.75% de acrescimo
    
if escolha_pagamento == 1:
    tipo_pagamento = "Pagamento por Pix ou Dinheiro"
elif escolha_pagamento == 2:
    tipo_pagamento = "Pagamento por Cartao de Debito"
else:
    tipo_pagamento = "Pagamento por Cartao de Credito"
    
print(f"Valor: {venda_user:.2f}")
print(f"Forma de pagamento: {escolha_pagamento}")
print(tipo_pagamento)
print(f"Valor: {venda_user:.2f}")
print(f"Valor Reajustado: {reajuste}")

