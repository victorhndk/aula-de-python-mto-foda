#Preciso de um aluno, suas notas e sua nota final
nome = str(input('Escreva o nome do aluno em questão: '))
nota1 = float(input('Escreva a primeira nota do aluno: '))
nota2= float(input('Escreva a segunda nota do aluno: '))
notaF = (nota1 + nota2) / 2
print('O aluno', nome,'ficou com ', nota1, ' na primeira prova, ', nota2, ' na segunda prova. Logo, ficou com ', notaF, ' na matéria.')
