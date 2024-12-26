"""
Closure e funções que retornam outras funções
"""

def criar_funcao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}'
    return saudar

saudar_bom_dia = criar_funcao('Bom dia')
saudar_boa_noite = x=criar_funcao('Boa noite')

for nome in ['Danilo', 'Maria', 'José']:
    print(saudar_bom_dia(nome))
    print(saudar_boa_noite(nome))
