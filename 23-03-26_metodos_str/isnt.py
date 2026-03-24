import os 
os.system("cls")

digito = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "-"]
def isint(n: int) -> bool:
    inicio = 0
    fim = len(n)
    lista_digito = list()
    while True:
        indice = n.find(inicio,fim)
        if n < 0 and "-" is not len(n[0]):
            n = False
        else: 
            n = True
    return lista_digito


n = "5"
print(n.isdigit()) # True
n = "A"
print(n.isdigit()) # False
n = "-9"
print(n.isdigit()) # False



