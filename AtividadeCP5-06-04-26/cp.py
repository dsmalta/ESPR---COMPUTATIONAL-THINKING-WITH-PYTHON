def isfloat(v: str) -> bool:
    v = v.strip()
    if v[0] == '-':
        v = v[1:]
    if v and v[0] == '+':
        v = v[1:]
    if '.' in v:
        v = v.replace('.', '', 1)
    return v.isdigit()  

def conta_palavras(texto: str) -> int:
    return len(texto.split())

def conta_digitos(texto: str) -> int:
    digitos = 0
    for d in texto:
        if d.isdigit():
            digitos += 1
    return digitos

def conta_caracteres_especiais(texto: str) -> int:
    especiais = 0
    for c in texto:
        if c == ' ' or c == '!':
            especiais += 1
    return especiais

def conta_vogais(texto: str) -> int:
    vogais = "aeiouAEIOU"
    conta_vogais = 0
    for c in texto:
        if c in vogais:
            conta_vogais += 1
    return conta_vogais  

lista = []
lista_num = []
lista_outros = []

while True:
    print(f'''
0 - SAIR
1 - Exercício Lista 
2 - Exercício String
''')
    escolha = int(input('Escolha: '))

    match escolha:
        case 0:
            break

        case 1:
            lista.clear()
            lista_num.clear()
            lista_outros.clear()
            elem = input("Digite os elementos da lista ou '.' para finalizar... ")
            
            while elem != '.':
                elem = input("Digite os elementos da lista ou '.' para finalizar... ")
                lista.append(elem)
                if isfloat(elem):
                    num = float(elem)
                    lista_num.append(num)
                    lista.append(num)
                else:
                    lista_outros.append(elem)
                    lista.append(elem)

            print(f'''
                a. 
                Lista completa: {lista}
                Numérica: {lista_num}
                Outros: {lista_outros}
            ''')

            soma = sum(lista_num)
            media = soma / len(lista_num)
            maior = lista.num[0]
            menor = lista.num[0]

            for num in lista_num:
                if num > maior:
                    maior = num
                if num < menor:
                    menor = num
                
            print(f'''
                b. Soma da lista numérica: {soma} 
                Média da lista numérica: {media}
                Maior valor: {maior} | 
                Menor: {menor}
            ''')

                
           

        case 2:
            frase = input("Digite uma frase... ")
            print(f"A frase '{frase}' tem:")
            print(f"  a. {conta_palavras(frase)} palavras")
            print(f"  b. {conta_vogais(frase)} vogais")
            print(f"  c. {conta_digitos(frase)} dígitos")
            print(f"  d. {conta_caracteres_especiais(frase)} caracteres especiais")

