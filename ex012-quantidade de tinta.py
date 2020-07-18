print('Olá ! Esse programa calcula a quantidade de tinta necessaria.')
larg = float(input('Digite a largura: '))
altura= float(input('Digite a altura: '))

area = larg*altura
print('Sua parede tem a dimensão de {}x{} e sua parede é de {}m²'.format(larg,altura,area))
tinta = area/2
print('Para pintar essa parede você precisara de {} litros de tinta '.format(tinta))
