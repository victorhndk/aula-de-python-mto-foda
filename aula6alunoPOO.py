class aluno:
    
    def __init__(self, nome, idade, matricula, materia):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.materia = materia
    
    def apresent():
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
    def estudar(materia):
        print(f"Estou estudando {materia}.")

pedro = aluno("Pedro", "19", "566565", "Matemática")
fabricia = aluno("Fabricia", "18", "75756575", "Literatura")

print(pedro.matricula)    
pedro.apresent()
pedro.estudar()
print(fabricia.matricula) 
fabricia.apresent()
pedro.estudar()
