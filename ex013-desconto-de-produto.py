preco = float(input('Digite o valor do produto: R$ '))
desconto = preco * 0.05
print('O preço do produto é R${} e com 5% de desconto fica R$ {:.2f} e com desconto fica R$ {:.2f}'.format(preco,desconto,preco - desconto))