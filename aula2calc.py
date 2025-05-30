#Dois valores, 6 op aritméticas e inputs. Por fim, um print da resposta.
valor1 = int(input('Escreva seu primeiro valor:'))
valor2 = int(input('Escreva seu segundo valor:'))
operacao = int(input('Escolha a operação: 1 - Adiçao, 2 - Divisao, 3 - Multiplicaçao ou 4 - Divisao:'))
if operacao == 1:
    resultado = valor1 + valor2
    print('O resultdo é: ', resultado)
elif operacao == 2:
    resultado2 = valor1 - valor2
    print('O resultado é: ', resultado2)
elif operacao == 3:
    resultado3 = valor1 * valor2
    print('O resultdo é: ', resultado3)
elif operacao == 4:
    resultado4 = valor1 / valor2
    print('O resultdo é: ', resultado4)
else:
    print('Operação Inválida')


    
