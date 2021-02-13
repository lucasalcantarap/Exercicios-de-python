
lista = [10,10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
    
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero.')
except IndexError:
    print('Erro ao acessar um indíce inválido da lista.')
except BaseException as ex:
    print('Erro desconhecido.Erro: {}'.format(ex))
else:
    print('Executa quna do não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
    