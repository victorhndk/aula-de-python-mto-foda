#Preciso de um numero, algo que identifique se o numero é positivo, negativo ou 0
numero = int(input('Digite o seu queridíssimo número : '))
if numero > 0:
    print('O seu número é positivo.')
elif numero == 0:
    print('O seu número é o zero absoluto.')
else:
    print('O seu número é negativo.')
    
