# exercicio_new1.py
# Calculo de desconto baseado no valor da venda
venda_user = float(input("Digite o valor da venda: "))

if venda_user > 1000:
    desconto = venda_user * 0.1
    print(f"O valor do desconto e: {desconto}")
else:
    desconto = venda_user * 0.05
    print(f"O valor do desconto e: {desconto}")
    
valor_final = venda_user - desconto
print(f"Venda.........: R$ {venda_user:8.2f}")
print(f"Desconto......: R$ {desconto:8.2f}")
print(f"Valor Final...: R$ {valor_final:8.2f}")
    