m = 380

cedulas_cem = m // 100
m = m % 100

cedulas_cinquenta = m // 50
m = m % 50

cedulas_vinte = m // 20
m = m % 20

cedulas_dez = m // 10
m = m % 10

# print("O montante vai ser distribuido em", cedulas_cem, "cedulas de 100 reais,", cedulas_cinquenta, "cedulas de 50 reais,", cedulas_vinte, "cedulas de 20 reais e", cedulas_dez, "cedulas de 10 reais.")
print(f"R$ 100 = {cedulas_cem} R$ 50 = {cedulas_cinquenta} R$ 20 = {cedulas_vinte} R$ 10 = {cedulas_dez}")
print()
print(f"""
R$ 100 = {cedulas_cem}
R$ 50 = {cedulas_cinquenta}
R$ 20 = {cedulas_vinte}
R$ 10 = {cedulas_dez}""")

"""
Comentários
"""