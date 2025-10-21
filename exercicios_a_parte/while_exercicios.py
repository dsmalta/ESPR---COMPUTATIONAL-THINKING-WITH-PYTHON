# Contagem regressiva
num_inicio = 10
num_final = 0

while num_inicio >= num_final:
    print(num_inicio)
    num_inicio -= 1
    
# Soma ate zero
numero = 1
soma = 0
while numero != 0:
    numero = int(input("Digite um numero: "))
    soma = soma + numero
    
print(soma)

# Senha correta

senha = 1234
senha_adivinha = int(input("Tente adivinhar a senha: "))
while senha_adivinha != senha:
    senha_adivinha = int(input("Tente novamente! "))
    
if senha_adivinha == senha:
    print("Parabens, voce acertou a senha")
    
# Numeros pares e impares

nums_escolhidos = int