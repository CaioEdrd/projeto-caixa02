from glob import glob
import json, requests, time,Funcoes_Caixa_Dict # bibliotecas

def verificacao_moeda():
    global uni
    global moeda

    print("""Escolha a moeda:
    1.Dolar
    2.Euro
    3.Libra
    4.Iene  """)
    time.sleep(1)

    # escolha da moeda
    choice = str(input('Escolha a moeda que você deseja converter:')).strip().upper() #escolha da moeda
    time.sleep(1)

    if choice == 'DOLAR' or choice == '1':
        moeda = 'USDBRL'
        uni = 'dolar'
        return moeda
    elif choice == 'EURO' or choice == '2':
        moeda = 'EURBRL'
        uni = 'euro'
        return moeda

    elif choice == 'LIBRA' or choice == '3':
        moeda = 'GBPBRL'
        uni = 'libra'
        return moeda

    elif choice == 'IENE' or choice == '4':
        moeda = 'JPYBRL'
        uni = 'iene'
        return moeda

    else:
        print('Moeda inválida!')
        return None
        #Buscando infos na api

def conversao(): # evitando erros de digitação
    global valor_moeda
    global dic
    
    url = 'https://economia.awesomeapi.com.br/json/last/'+ moeda[0:3] +'-'+ moeda[3:6]

    #Capturando a cotação
    cotacao = requests.get(url)

    #Extraindo a cotação e jogando no JSON
    dic = cotacao.json()

    #Tratamento de infos
    valor_moeda = float(dic[moeda]["bid"]) # convertendo valor de str para float    
    print(f'O valor atual do {uni} é :{valor_moeda:.2f}') # Mostrando valor da unidade da moeda escolhida
    time.sleep(1)

    Funcoes_Caixa_Dict.verifica_produto_estoque()
    global conversao_moeda
    #conversão da moeda do usuário com o REAL
    conversao_moeda = Funcoes_Caixa_Dict.estoque[Funcoes_Caixa_Dict.index_produto_estoque]['valor'] / valor_moeda
    
    print(f'O valor a ser pago é R$ {conversao_moeda:.2f} cada') # mostrando conversão
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
    print(f'Data: {data_hora[8:10]}/{data_hora[5:7]}/{data_hora[0:4]}')
    time.sleep(1)
    print()
    print(f'Horário:{data_hora[10:19]}')
