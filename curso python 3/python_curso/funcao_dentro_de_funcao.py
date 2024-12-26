def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'bom dia', 'Danilo')
)
print(
    executa(saudacao, 'bom dia', 'João')
)