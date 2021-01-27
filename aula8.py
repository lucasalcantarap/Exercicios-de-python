#importacao

from calculadoraclass1 import Calculadora
from aula8_contador_letras import contador_letras


if __name__ == '__main__':
        
    calc = Calculadora(10,2)

    print(calc.soma())
    print(calc.div())
    lista = ['Lucas','Kauana','Bia']
    print(contador_letras(lista))