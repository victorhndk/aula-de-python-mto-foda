class Carrinho:
    def __init__(self, velocidade_atual):
        self._velocidade_atual = velocidade_atual
        self.set_velocidade_atual(nova_velocidade)
        
    def set_velocidade_atual(self, nova_velocidade):
        if (nova_velocidade >= 0 and 200 >= nova_velocidade):
            self._velocidade_atual = nova_velocidade
            
        elif (nova_velocidade < 0):
            
            print("O carro ta parado ja pia tlk")
            
        else:
            
            print("O carro ta turbinado ja pai tlk")
            
    def get_velocidade_atual(self):
        return self._velocidade_atual
        
            
carro = Carrinho(10)

print(carro.get_velocidade_atual())
carro.set_velocidade_atual(180)
print(carro.get_velocidade_atual())
carro.set_velocidade_atual(210)
print(carro.get_velocidade_atual())
carro.set_velocidade_atual(-10)
