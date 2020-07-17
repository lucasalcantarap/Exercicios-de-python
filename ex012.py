print('Olá ! Esse programa calcula a quantidade de tinta necessaria.')
b = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))

area = b*h
quantidadePintada = area/2
print('Serão necessários {} litros de tinta.'.format(quantidadePintada))
