#pedir ao querido usuario escrever seu peso, altura e calcular o imc dele em outro file
peso = float(input('Olá. Teu peso, mano:'))
altura = float(input('Tua altura agora, valeu:'))
def  calcular_imc(imc):
    print(f'O teu IMC aí, mano: {imc}')
calcular_imc(peso / altura ** 2)
