alunos = []
def adicAlunos(nome, matricula):
    aluno = {
        'nome': nome,
        'matricula': matricula,
        'notas': []
    }
    alunos.append(aluno)
    print(f"Aluno {nome} adicionado com sucesso.")

def Aluno(matricula):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None

def adicNotas(matricula, nota):
    aluno = Aluno(matricula)
    if aluno:
        aluno['notas'].append(nota)
        print(f"Nota {nota} adicionada ao aluno {aluno['nome']}.")
    else:
        print("Aluno não encontrado.")

def calculaMedia(matricula):
    aluno = Aluno(matricula)
    if aluno:
            media = sum(aluno['notas']) / len(aluno['notas'])
            return media
    else:
        print("Aluno não encontrado.")
        return None

def verificarAluno(matricula):
    media = calculaMedia(matricula)
    if media is None:
        return
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def alunosExistentes():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        media = calculaMedia(aluno['matricula'])
        situacao = verificarAluno(aluno['matricula'])
        print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']}")
        print(f"Notas: {aluno['notas']} | Média: {media:.2f} | Situação: {situacao}")
        print("-" * 40)
