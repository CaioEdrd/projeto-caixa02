import Funcoes_ProjetoCaixa, time #modularização do arquivo de funções

nome_mercado = input("Digite o nome do seu mercado: ")
time.sleep(1)
print(f"Bem-Vindo ao controle de caixa {nome_mercado}!")
time.sleep(1)

print("0 - Help : Exibe todos os comandos disponíveis, como:\n1 - Estoque\n2 - Adicionar\n3 - Vender\n4 - Receita\n5 - Valor Total do estoque\n6 - Ver produto por categoria\n7 - Sair")
time.sleep(1)

while True:
    print("\nCaso deseje visualizar os comandos novamente, digite 0")
    time.sleep(1)
    comando = input("Digite o número do comando desejado: ")  #O usuário digita o número do comando desejado
    print()
    time.sleep(1)
    
    if comando == "0":  #Se o usuário digitar 0, exibe os comandos disponíveis
        print("Comandos disponíveis:\n1 - Estoque\n2 - Adicionar\n3 - Vender\n4 - Receita\n5 - Valor Total do estoque\n6 - Ver produto por categoria\n7 - Sair")
        time.sleep(1)

    elif comando == "1":  #Se o usuário digitar 1, exibe o estoque
        Funcoes_ProjetoCaixa.exibe_estoque()
    
    elif comando == "2":  #Se o usuário digitar 2, adiciona um produto ao estoque
        Funcoes_ProjetoCaixa.adicionar_produto()    
    
    elif comando == "3":  #Se o usuário digitar 3, vende um produto
        Funcoes_ProjetoCaixa.vender()
    
    elif comando == "4": #Se o usuário digitar 4, mostra a receita e a quantidade das vendas
        Funcoes_ProjetoCaixa.mostrar_receita()            
    
    elif comando == "5": #Mostra o valor total do estoque
        Funcoes_ProjetoCaixa.valorestoque()
    
    elif comando == "6": #Mostra os produtos e categorias
        Funcoes_ProjetoCaixa.categoriaproduto()
    
    elif comando == "7":
        break
    
    else:
        print("Comando inválido!")
        time.sleep(1)