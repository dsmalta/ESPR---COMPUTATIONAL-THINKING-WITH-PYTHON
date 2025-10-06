"""
Peça ao usuário que digite uma temperatura.
- Se ela for menor do que 15, exiba: "Está frio"
- Se ela estiver entre 15 e 25, exiba: "Temperatura Normal"
- Se ela estiver acima de 25 até 40, exiba "Está muito quente"
- Se ela estiver acima de 40, exibir "Torrei!"

"""

temp = float(input("Temperatura: "))
if temp < 15:
    print("Está frio")
elif temp >= 15 and temp <= 25: # 15 <= temp <= 25
    print("Temperatura Normal")
elif temp > 25 and temp <= 40:
    print("Está muito quente")
else:
    print("Torrei")