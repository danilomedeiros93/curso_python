try:
    a = 18
    b = 0

    print(b[0])
    print('Teste 1') 
    c = a / b
    print('Teste 2') 
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Variavel b não está definida.')
except TypeError:
    print('TypeError.')
except Exception:
    print('Erro desconhecido.')
