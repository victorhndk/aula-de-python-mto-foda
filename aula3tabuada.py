#criar um input que o usuario pode escolher um numero de 1 a 10 e mostrar a tabuada dele
number = int(input('Escreve um número de 1 a 10 ai man:'))
tabuada = 0 
for beicola in range(11):
    tabuada = number * beicola
    print(tabuada)
