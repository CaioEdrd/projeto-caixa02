def conversão_de_moedas():  
  #Importando as bibliotecas
  import requests #deve fazer um pip install requests
  import json

  #Escolha a moeda que se deseja buscar a cotação
  while True:
    print("""Escolha a moeda:
      1. Dólar
      2. Euro
      3. Bitcoin""")

    escolha = int(input("Digite aqui: "))

    if escolha == 1:
      moeda = 'USDBRL'
      break
    elif escolha == 2:
      moeda = 'EURBRL'
      break
    elif escolha == 3:
      moeda = 'BTCBRL'
      break
    else:
      print('Moeda inválida!')

  #Url da API
  url = 'https://economia.awesomeapi.com.br/json/last/'+ moeda[0:3] +'-'+ moeda[3:6]

  #Capturando a cotação
  # cotacao = requests.get(url).content #essa funciona com a (1)
  cotacao = requests.get(url)

  #Extraindo a cotação e jogando no JSON
  # dic = json.loads(cotacao) (1)
  dic = cotacao.json()

  #Exibindo a informação extraida como dicionário
  print(dic)

  #Exibindo os resultados em tela
  print()
  print(dic[moeda]["name"]) #extraindo a informação do JSON
  data_hora = dic[moeda]["create_date"]
  print('Última cotação em:')
  print(f'dia: {data_hora[8:10]}/{data_hora[5:7]}/{data_hora[0:4]}')
  print(f'Horário:{data_hora[10:19]}')
  print(f'Cotação: {dic[moeda]["bid"]}')