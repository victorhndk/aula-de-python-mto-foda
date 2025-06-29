from alunos import adicAlunos, Aluno, adicNotas, calculaMedia, verificarAluno, alunosExistentes
escolha = int(input("O que deseja fazer today: 1 - Adic. Aluno | 2 - Adic. Nota | 3 - Calc. Média | 4 - Verificar Aluno | 5 - Exibir Tudo \n"))

while True:        
    if escolha  == 1:
        nome = input("Nome do abençoado: ")
        matricula = input("Matrícula do mesmo: ")
        adicAlunos(nome, matricula)

    elif escolha  == 2:
        matricula = input("Matrícula do desgraçado: ")
        nota = float(input("Qual nota deseja adicionar?: "))
        adicNotas(matricula, nota)

    elif escolha  == 3:
        matricula = input("Matrícula do queridinho: ")
        media = calculaMedia(matricula)

    elif escolha  == 4:
        matricula = input("Matrícula do aluninho: ")
        situacao = verificarAluno(matricula)
        print(f"Situação do aluno: {situacao}")

    elif escolha  == 5:
        alunosExistentes()

    else:
        print("Opção inválida!")
        break
