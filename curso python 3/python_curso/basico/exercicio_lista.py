import os

lista = []

while True:
 print('selecione uma opção')
 opcao = input('[i]nserir [a]pagar [l]istar: ')

 if opcao == 'i':
  os.system('cls')
  valor = input('Valor: ')
  lista.append(valor)
 elif opcao == 'a':
  indice_str = input(
   'Escolha o índice para apagar: '
  )
  try:
      indice = int(indice_str)
      del lista[indice]
  except:
      print('Não foi possivel apagar este indice.')
 elif opcao == 'l':
   os.system('cls')

   if len(lista) == 0:
     print('Nada para listar')

   for i, valor in enumerate(lista):
     print(i, valor)
