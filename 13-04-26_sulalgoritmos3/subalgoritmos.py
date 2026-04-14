import os 
os.system('cls')

def calc_soma(n1: float, n2: float) -> float:
    s = n1 + n2
    return s

# Uso
num1 = 6
num2 = 7
soma = calc_soma(num1, num2)
print(soma)