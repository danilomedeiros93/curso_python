perguntas =[ {
    'pergunta': 'quanto é 3+3?',
    'opções': ['1', '2', '3', '4', '5', '6'],
    'Resposta': '6',
},
{
    'pergunta': 'quanto é 6*6?',
    'opções': ['24', '48', '36', '49', '56', '64'],
    'Resposta': '36',
},
{
    'pergunta': 'quanto é 10/2?',
    'opções': [ '2', '3', '5', '6'],
    'Resposta': '5',
},
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['pergunta'])
    print()
    
    opcoes = pergunta['opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    convertido_escolha_para_inteiro = None
    qtd_opcoes = len(opcoes)
    
    

    if escolha.isdigit():
        convertido_escolha_para_inteiro = int(escolha)
    


    if convertido_escolha_para_inteiro is not None:
        if convertido_escolha_para_inteiro >= 0 and convertido_escolha_para_inteiro < qtd_opcoes:
            if opcoes[convertido_escolha_para_inteiro] == pergunta['Resposta']:
                acertou = True
    
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou ')
    else:
        print("Errou")

print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')

