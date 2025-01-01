produtos = [
    {'nome': 'Arroz', 'preco': 5.45},
    {'nome': 'Macarão', 'preco': 2.20},
    {'nome': 'Café', 'preco': 9.99},
]

novos_produtos = [
    {**produto, 'preco': produto['preco' ] * 1.5}
    if produto ['preco'] > 5 else {**produto}
    for produto in produtos
]

print(novos_produtos)