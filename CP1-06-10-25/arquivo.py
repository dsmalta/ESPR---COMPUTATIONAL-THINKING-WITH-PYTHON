salario_min = 1302
salario = int(input("Salário: "))
qtd_faltas = int(input("Qtd. de Faltas: "))

# Salário reajustado
if salario <= salario_min * 2:
    salario_reajuste = salario * 1.0645
    print(salario)

if salario > salario_min * 2 or salario <= salario_min * 5:
    salario_reajuste = salario * 1.0455
    print(salario)

if salario > salario_min * 5 or salario <= salario_min * 10:
    salario_reajuste = salario * 1.0289
    print(salario)

if salario > salario_min * 10:
    salario_reajuste = salario
    print(salario)

# Bônus
if qtd_faltas == 0:
    bonus_faltas = 1302

elif qtd_faltas == 1:
    bonus_faltas = 500

elif qtd_faltas > 1:
    bonus_faltas = 0

else:
    bonus_faltas = 1302

# Ganho Total
ganho_total = salario_reajuste + bonus_faltas

# Prints
print(f"Salário: R$ {salario} \nQtd. de faltas: {qtd_faltas}")
print("\nRelatório:")
print(f"Salário............: R$ {salario:.2f}")
print(f"Salário Reajustado.: R$ {salario_reajuste:.2f}")
print(f"Bônus..............: R$ {bonus_faltas:.2f}")
print(f"Ganho Total........: R$ {ganho_total:.2f}")