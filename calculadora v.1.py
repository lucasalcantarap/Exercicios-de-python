print("--------CALCULADORA V 1.0--------")
sair = False

while sair == False:

  n1 = int(input('Digite o primeiro número: '))
  operador = input("Digite um operador ( + - * /) ")
  n2 = int(input('Digite um segundo número: '))
  
  if operador == '+' :
    print(n1+n2)

  if operador == '-' :
    print(n1-n2)

  if operador == '*' :
    print(n1*n2)

  if operador == '/' :
    print(n1/n2)


  teste = input('Deseja sair(s/n)? ')
  if teste == 's':
    sair = True
    print('Obrigado por usar nossa calculadora!')