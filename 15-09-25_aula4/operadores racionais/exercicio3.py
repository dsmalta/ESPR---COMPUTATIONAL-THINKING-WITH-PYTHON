num1 = int(input("Digite o primeiro número"))
num2 = int(input("Digite o segundo número"))
num3 = int(input("Digite o terceiro número"))
maior_num = num1

if num2 > maior_num:
    maior_num = num2

if num3 > maior_num:
    maior_num = num3

print("O maior número é", maior_num)