class Carrinho:
    def __init__(self, velocidade_atual):
        self._velocidade_atual = velocidade_atual
        
    def acelerar(self):
        self._velocidade_atual =+ 10
        print(f"O carrinho acelerou, galera (tipo uns {self._velocidade_atual})")
        
    def frear(self):
        if (self._velocidade_atual > 0):
            self._velocidade_atual -= 5
            print(f"O carro diminuiu sua velocidade, pessoal (tipo uns {self._velocidade_atual})")
        else:
            print("O carro já está parado, minha galera (pare imediatamente)")
            
    def mostrar_velocidade_atual(self):
            return self._velocidade_atual
            
carro = Carrinho(10)

carro.acelerar()
carro.acelerar()
carro.mostrar_velocidade_atual()
carro.frear()
carro.frear()
carro.mostrar_velocidade_atual()
carro.frear()
