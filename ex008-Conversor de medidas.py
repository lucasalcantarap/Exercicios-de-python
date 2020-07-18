nmetro = float(input('Digite um número: '))
cm = nmetro*100
mili = cm/0.10000
print('Você digitou {}, que corresponde à {}cm e a {:.0f} mm'.format(nmetro,cm,mili))