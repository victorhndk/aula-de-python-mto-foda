aluno = {
    "nome": "Bruno", 
    "matricula": "1209786",
    "idade": "20",
    "curso": ["PPO", "Banco de Dados"]
}
print(aluno)
aluno["nome"] = "Bartolomeu" #adiciona um novo nome ao dicionario
print(aluno)
aluno.pop("nome") #tira um elemnto do dicionario
print(aluno)
aluno["curso"].append("Estrutura de Dados") #adiciona um item na lista
print(aluno)
