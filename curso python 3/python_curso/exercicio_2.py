"""
Crie funções que duplicam, triplicam e quadriplicam o numero recebido como parâmetro
"""

def multiplicador_de_numeros(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplicar = multiplicador_de_numeros(4)
triplicar = multiplicador_de_numeros(5)
quadruplicar = multiplicador_de_numeros(7)

print(duplicar(4))
print(triplicar(4))
print(quadruplicar(4))