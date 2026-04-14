import os 
os.system('cls')

def calc_soma(*args) -> float:
    s = 0
    for num in args:
        s += num
    return s

# Uso
num1 = 6
num2 = 7
soma = calc_soma(num1, num2, 78, 66, 54)
print(soma)