"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o total para uma variável e mostre o valor da variável
"""
def soma(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicando_args_nao_nomeados = soma(2, 4, 5, 6, 7)

print(multiplicando_args_nao_nomeados)

"""
Crie uma função que fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.
"""

def par_ou_impar(*args):
    for numero in args:
        
        if numero % 2 == 0:
            print(f'{numero = } \nNúmero é par!')
        
    return f'{numero = } \nNúmero é ímpar!'
    

resultado_resto_divisao = par_ou_impar(1, 2, 3, 4, 6, 7, 8, 9)
print(resultado_resto_divisao)
