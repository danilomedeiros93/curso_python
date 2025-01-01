produto = {
    'nome': 'Caneta Azul',
    'preco': 3,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

print(dc)