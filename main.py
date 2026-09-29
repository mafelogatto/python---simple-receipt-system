#entries
nome = input('Digite seu nome: ')
idade - input('Digite sua idade: ')
tem_carteirinha = input('Você possui carteirinha? (S/N): ')

valor_base_ingresso = 30.0
idade = int(idade)
tem_carteirinha = tem_carteirinha.lower()

#strings and logical operators
usuario_vip = ''vip'' in nome.lower()

#conditional structure
if idade < 0:
  preco_final = 0.0
  categoria = ''Inválida''
elif idade < 12 or idade >= 60 or tem_carteirinha == ''sim'' or tem_carteirinha == ''s'':
  preco_final = valor_base_ingresso / 2
  if idade < 12:
    categoria = ''Meia-Entrada (Infantil)''
  elif idade >= 60:
    categoria = ''Meia-Entrada (Idoso)''
  else:
    preco_final = valor_base_ingresso
    categoria = ''Inteira''

#math and extra rules
if usuario_vip and categoria == ''Inteira'':
  preco_final = preco_final * 0.9
  categoria = ''Inteira Desconto VIP''

#output

if idade >= 0:
 print('-' * 60)
 print('RECIBO DE COMPRA - CINEMA')
 print(f'Cliente: {nome.title()}')
 print(f'Categoria: {categoria}')
 print(f'Valor total do ingresso: R$ {preco_final:.2f}')
 print('-' * 60)

 if idade < 18:
  print('Aviso: Verifique a classificação indicativa do filme.')
  print('Tenha um bom filme.')
else:
  print('Idade inválida. Digite uma idade válida')
  
