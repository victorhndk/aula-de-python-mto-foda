class aluno:
    def __init__(self, nome, idade, matricula, materia):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.materia = materia
        
    def apresent(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
    def estuda(self):   
        print(f"Estou estudando {self.materia}")
        
pessoa = Aluno("marcelo", "17", "242424", "em como ser um desgraçado")      
pessoa_dois = Aluno("felipinho", "17", "242324", "variola")    

print(pessoaum.matricula)
pessoaum.apresentar()
pessoaum.estudar()
print(pessoadois.matricula)
pessoadois.apresentar()
pessoadois.estudar()
