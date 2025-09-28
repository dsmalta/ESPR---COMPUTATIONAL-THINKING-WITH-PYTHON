t = int(input("Fazem quantos anos que a pessoa fuma?"))
numMacos = int(input("Quantos maços ela fuma por dia?"))
valorMaco = float(input("Qual o valor do maço?"))

conversorAnosDias = t * 365 # convertendo anos em dias
totalMacos = numMacos * conversorAnosDias # calculando quantos maços forma fumados ao longo dos anos
dinheiroGastoAnos = totalMacos * valorMaco
print(f"A pessoa já gastou R${dinheiroGastoAnos:.2f} em maços ao longo de {t} anos.")