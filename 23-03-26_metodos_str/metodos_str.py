import os 
os.system("cls")

# Métodos para Strings
#        0123456789012345678901234567890123456789012345678901
# Método find() - encontra um substring e retorna o índice dela 
frase = "Veremos agora como funciona o fatiamento com strings"
print(frase.find("agora"))
print(frase.find("m"))
print(frase.find("fiap"))
print(frase.find("o"))
print(frase.find("o", 10, 20))

# Método join() - junta as strings em uma só
nome = ["Edson", "de", "Oliveira"]
nome_str = " ".join(nome) # o que estiver entre as aspas é o que será printado na hora de juntar as strings
print(nome, nome_str)
nome_str = "".join(nome)
print(nome, nome_str)
nome_str = ".".join(nome)
print(nome, nome_str)

# Método split() - divide as strings
os.system("cls")
nome = "Edson de Oliveira"
print(nome)
print(nome.split(), "tem", len(nome.split()), "palavras.")
print(nome.split('e'))
print(nome.split('de'))

# Método replace() - Substitui um elemento pelo outro
os.system("cls")
nome = "Edson de Oliveira"
nome1 = nome.replace("e", "E")
print(nome1)

nome2 = nome.replace("e", "?")
print(nome2)

nome2 = nome.replace("e", "?", 1)
print(nome2)

# Método strip()
os.system("cls")
texto = "     strip elimina os espaços"
print(f"|{texto}|")
texto = texto.strip()
print(f"|{texto}|")

# Operador in
num = 3
if num in [1,2,3,4,5]:
    print(f"{num} está na lista.")
else:
    print(f"{num} não está na lista.")

nome = "Edson de Oliveira"
if "de" not in nome:
    print(f"'de' não está em {nome}.")
else:
    print(f"'de' está em nome.")

# Exercício
# 1. Utilizando somente os métodos apresentados nessa apresentação, faça
# um subalgoritmo de nome vogal_maiuscula(string) que passe uma string por 
# paraâmetro e retorne-a com as vogais convertidas em maiúsculas.

def volga_maiuscula(texto: str) -> str:
    new_texto = list()
    vogais = "aeiou"
    for i in range(len(texto)):
        if texto[i] in vogais:
            volga_maiuscula = vogais.upper()
            new_texto.append(volga_maiuscula)
        else:
            new_texto.append(texto[i])
    return new_texto

texto = "Edson de Oliveira"
new_texto = volga_maiuscula(texto)
print(new_texto)

# 2. Dada uma lista e um caractere pro parâmetro, faça
# uma função que retorno em uma lista com os índices 
# onde os caracteres foram encontrados

def retorna_indices(nome: str, caracter: str) -> list:
    inicio = 0
    fim = len(nome)
    lista_indice = list()
    while True:
        indice = nome.find(caracter,inicio,fim)
        if indice == -1:
            break
        else:
            lista_indice.append(indice)
            inicio = indice + 1
    return lista_indice

nome = "Edson de Oliveira"
caracter = "i"

print(retorna_indices(nome, caracter))


