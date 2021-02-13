class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x= int(input('Enre com uma nota de 0 a 10: '))
        print(x) 
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        break
    except ValueError:
        print('Valor invalido, digitar apenas números.')
