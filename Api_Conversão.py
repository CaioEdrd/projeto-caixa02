import json, requests, time # bibliotecas


valor = 20 # simulando valor de um produto qualquer/ puxar do dicionário

while True: # evitando erros de digitação
    print("""Escolha a moeda:
    1.dolar
    2.euro
    3.libra
    4.iene  """)
    time.sleep(1)

    # escolha da moeda
    choice = str(input('Escolha a moeda que você deseja converter:')).strip().upper() #escolha da moeda
    time.sleep(1)

    if choice == 'DOLAR' or choice == '1':
        moeda = 'USDBRL'
        uni = 'dolar'
        break
    elif choice == 'EURO' or choice == '2':
        moeda = 'EURBRL'
        uni = 'euro'
        break
    elif choice == 'LIBRA' or choice == '3':
        moeda = 'GBPBRL'
        uni = 'libra'
        break
    elif choice == 'IENE' or choice == '4':
        moeda = 'JPYBRL'
        uni = 'iene'
        break
    else:
        print('Moeda inválida!')

# buscando infos na api
url = 'https://economia.awesomeapi.com.br/json/last/'+ moeda[0:3] +'-'+ moeda[3:6]
cotacao = requests.get(url)
dic = cotacao.json()

# tratamento de infos
vlr = float(dic[moeda]["bid"]) # convertendo valor de str para float

print(f'O valor atual do {uni} é :{vlr:.2f}') # mostrando valor da unidade da moeda escolhida
time.sleep(1)

cnv = vlr*valor # convertendo moeda

print(f'O valor convertido de real para {uni} é {cnv:.2f}') # mostrando conversão
time.sleep(1)

# informações adicionais
print()
print('Informações adicionais')
time.sleep(1)
print()
data_hora = dic[moeda]["create_date"]
print('Última cotação em:')
time.sleep(1)
print()
print(f'dia: {data_hora[8:10]}/{data_hora[5:7]}/{data_hora[0:4]}')
time.sleep(1)
print()
print(f'Horário:{data_hora[10:19]}')
