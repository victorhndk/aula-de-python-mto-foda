#Criar um input que leia quantas vogais tem 
#na frase do usuario com loop e if
#print das vogais presentes (numero e quais sao)
frase = input('Escreva sua opinião fodastica sobre o colega marcelo:')
vogais = 'a', 'e', 'i', 'o', 'u'
total_vogais = 0
for vogalizar in frase:
    if vogalizar in vogais:
        total_vogais += 1

print('O total das vogais', vogais, 'é de:', total_vogais)
