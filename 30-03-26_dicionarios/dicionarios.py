aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "DS",
}

print(aluno)

# Método get
# Não dá falha caso a key ou o value não existam

print(aluno.get("curso"))
print(aluno.get("nota"))
print(aluno["nota"])