salario_funcionario = float(input("Qual o salário do funcionário?"))
qtd_falta = int(input("Quantas vezes o funcionário faltou?"))

if qtd_falta == 0:
   salario_funcionario = salario_funcionario + 500

print("O salário do funcionário é", salario_funcionario)