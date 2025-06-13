#permita que o usuario possa escolher a sua forma geometrica e os valores da altura e base do mesmo
from geometria import calcular_area_circulo, calcular_area_retangulo, calcular_area_triangulo
forma = int(input('Escolha a forma geométrica - Círculo(1), Retângulo(2) ou Triângulo(3)'))

if forma == 1:
    raio = float(input('Qual o raio do seu círculo?'))
    area = calcular_area_circulo(raio)
    print('A área do seu círculo é:', area)
elif forma == 2:
    altura = float(input('Qual a altura do retângulo?'))
    base = float(input('Qual a base do retângulo?'))
    area = calcular_area_retangulo(base, altura)
    print('A área do seu retângulo é:', area)
    
elif forma == 3:
    altura = float(input('Qual a altura do triângulo?'))
    base = float(input('Qual a base do triângulo?'))
    area = calcular_area_triangulo(base, altura)
    print('A área do seu triângulo é:', area)

else:
    print('Forma inválida!')

