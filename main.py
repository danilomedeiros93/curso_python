caminho_arquivo = 'C:\\Users\\USER\\Desktop\\atencao_aula_arquivos\\'
caminho_arquivo += 'exercicio_arquivo.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo,'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('teste \n')
    arquivo.write('teste \n')
