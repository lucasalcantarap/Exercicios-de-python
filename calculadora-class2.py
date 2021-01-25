class Calculadora:
   # def __init__(self):
      #pass 


    def soma (self, valor_a, valor_b):
        return valor_a + valor_b
    
    def sub(self,valor_a, valor_b):
        return valor_a - valor_b
        
    def multi(self, valor_a, valor_b):
        return valor_a * valor_b
        
    def div(self,valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10,25))
print(calculadora.sub(50,25))
print(calculadora.div(100,3))
print(calculadora.multi(7,8))