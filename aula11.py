
lista = [10,10]
try:
    divisao = 10 / 1
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero.')
except IndexError:
    print('Erro ao acessar um indíce inválido da lista.')
except BaseException as ex:
    print('Erro desconhecido.Erro: {}'.format(ex))
    
    #11:22