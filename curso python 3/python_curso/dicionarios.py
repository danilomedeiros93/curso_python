pessoa = {
    'nome': 'José',
    'sobrenome': 'Aguiar',
    'idade': 21,
    'altura': 1.75,
    'enderecos': [
        {'rua': 'rua qualquer', 'numero': 23242},
        {'rua': 'rua qualquer 2', 'numero': 654},
    ],
}

for chave in pessoa:
    print(chave, '=', pessoa[chave])