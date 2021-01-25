class Televisao:
    
    def __init__(self):
        self.ligada = False
        

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


televisao = Televisao()
print('Televisão está ligada? {}'.format(televisao.ligada))
televisao.power()
print('Televisao está ligada ?{}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada ? {}'.format(televisao.ligada))