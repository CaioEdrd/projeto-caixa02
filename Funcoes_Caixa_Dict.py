from time import sleep #importar apenas a função 'sleep' da biblioteca 'time' que é uma espécie de timer para execução da próxima linha

estoque = [] #Lista para adicionar os produtos que serão dicionários
    
qtd_estoque = []

vendas = []
receita = []

def verificar_estoque(): #Função para verificar se há produto no estoque
    if qtd_produtos() is not None: #Verifica se há função qtd_produtos não é None
        if real_estoque > 0:
            return real_estoque
    else:
        print("Estoque vazio!")
        sleep(1)
        
def exibe_estoque(): #Função para exibir o estoque
    if verificar_estoque() is not None: #Verifica se há produto no estoque
        print(f"Estoque com {len(estoque)} produto(s)!")
        sleep(1)
        for i in range(len(estoque)): #vai em cada index da lista estoque, ou seja, cada produto
            print(f"Produto - {estoque[i]['nome-produto']}\t Valor - R$ {estoque[i]['valor']}\t Categoria - {estoque[i]['categoria']}\t Quantidade - {estoque[i]['quantidade']}")
            sleep(1) #O produto é um dicionário, ele é o item da lista e dentro dele há chaves que são as informações sobre ele 
            if estoque[i]['quantidade'] < 5: #Caso a quantidade do produto 'i' esteja abaixo de 5 irá exibir essa mensagem
                print(f"\"{estoque[i]['nome-produto']}\" está com baixo estoque, necessário reabastecimento!")

def verificar_categoria(): #Função para verificar se a categoria é válida
    global categoria
    global nome_categoria
    categoria = input("Digite a primeira letra da categoria do produto ([A]limentos, [B]ebidas, [L]impeza, [H]igiene, [O]utros): ").lower()
    sleep(1)
    if categoria in ['a', 'b', 'l', 'h', 'o']:    #Verifica se a letra digitada é de uma categoria válida
        if categoria == 'a': #Conversão da letra da categoria para o nome
            nome_categoria = "alimento".capitalize()
        elif categoria == 'b':
            nome_categoria = "bebida".capitalize()
        elif categoria == 'l':
            nome_categoria = "limpeza".capitalize()
        elif categoria == 'h':
            nome_categoria = "higiene".capitalize()
        elif categoria == 'o':
            nome_categoria = "outros".capitalize()
        sleep(1)
        return categoria
    else:
        print("Categoria inválida")
        sleep(1)
        return None
        
def verifica_produto_estoque(): #Verifica se o produto está no Estoque e qual o Index daquele produto no Estoque
    for i in range(len(estoque)):
        if nome_produto == estoque[i]['nome-produto']: #Passa pelos elementos do estoque verificando se o nome digitado é igual ao de algum da lista
            global index_produto_estoque
            index_produto_estoque = i #Salva o index do produto digitado
            return index_produto_estoque

                
def adicionar_produto(): #Função para adicionar um produto ao estoque
    if verificar_categoria() is not None: #Verifica se a categoria é válida
        global nome_produto
        nome_produto = input("Qual o produto a ser adicionado? ").capitalize()
        sleep(1)
        if verifica_produto_estoque() is None: #Verifica se o produto não está no estoque
            valor = input(f"Qual o valor do produto: ")
            sleep(1)
            try:#verificação se o preço digitado é válido
                valor = float(valor)# Tente converter para float
                if valor < 0 : #Verifica se o preço é válido
                    print("Preço inválido!")
                    sleep(1)
                    return
            except ValueError:
                print("Não é um preço válido.")
                sleep(1)
                return    
            quantidade = input("Qual a quantidade do produto: ")
            sleep(1)
            if not quantidade.isdigit(): #verificação se a quantidade digitada é válida
                print("Quantidade inválida")
                sleep(1)
                return
            else:
                quantidade = int(quantidade)
            qtd_estoque.append(quantidade)
            nome_produto = {    #Produto que será adicionado ao estoque com as informações digitadas pelo usuário
            'nome-produto' : nome_produto.capitalize(),
            'valor' : f'{valor:.2f}',
            'categoria' : nome_categoria.capitalize(),
            'quantidade' : quantidade,}
            estoque.append(nome_produto)  #Adição do dicionário "nome_produto" na lista 'estoque'             
        else: #caso o produto já esteja no estoque, é solicitado apenas a quantidade para ser atualizada
            if nome_categoria ==  estoque[index_produto_estoque]['categoria'] :  #verifica se a categoria digitada é igual a cadastrada anteriormente
                qtd_produto = input("Qual a quantidade do produto? ")
                sleep(1)
                if not qtd_produto.isdigit(): #verificação se a quantidade digitada é válida
                    print("Quantidade inválida")
                    sleep(1)
                    return
                else:
                    qtd_produto = int(qtd_produto)
                estoque[index_produto_estoque]['quantidade'] += qtd_produto #Atualização da nova quantidade do produto
                qtd_estoque.append(estoque[index_produto_estoque]['quantidade'])
            else:
                print("A categoria do produto não corresponde a ele!")
                sleep(1)

def qtd_produtos(): #Função para verificação de quantidade real de produto no estoque
    global real_estoque
    venda_estoque = 0
    produtos_estoque = 0
    if len(qtd_estoque) > 0: #Só inicia se tiver produto no estoque
        i = 0
        for i in range(len(qtd_estoque)):
            produtos_estoque += qtd_estoque[i]
            i+=1
        for i in range(len(vendas)):
            venda_estoque += vendas[i]
            i+=1
        real_estoque = produtos_estoque - venda_estoque #quantidade geral de produto no estoque
        return real_estoque

def vender(): #Função para vender um produto
    global nome_produto
    if verificar_estoque() is not None:
        exibe_estoque()
        nome_produto = input("Digite qual produto deseja vender: ")
        sleep(1)
        if verifica_produto_estoque() is None: #Verifica se o produto que quer vender não está no estoque
            print("Não há esse produto no estoque!")
            sleep(1)
        else:
            qtd_venda = input(f"Digite a quantidade de {estoque[index_produto_estoque]['nome-produto']} a ser vendida: ")
            #Com o produto no estoque, basta digitar a quantidade que deseja vender
            if not qtd_venda.isdigit(): #verificação se a quantidade digitada é válida
                print("Quantidade inválida")
                sleep(1)
                return
            else:
                qtd_venda = int(qtd_venda)
                verifica_produto_estoque()
                if qtd_venda < 0 or qtd_venda > estoque[index_produto_estoque]['quantidade']: #verifica se é possível vender
                    print("A quantidade digitada não é válida!")
                    sleep(1)
                    return
            estoque[index_produto_estoque]['quantidade'] -= qtd_venda #Atualizando a nova quantidade do produto no estoque
            receita_parcial = qtd_venda * estoque[index_produto_estoque]['valor'] #Atualizando a receita parcial
            receita.append(receita_parcial)
            vendas.append(qtd_venda) 

def mostrar_receita(): #Função para mostrar a receita, as vendas
    if len(vendas) > 0: #verificação se houve vendas 
        receita_total = 0
        nvendas = 0
        for i in range(len(vendas)):
            nvendas += vendas[i] #Soma da quantidade de vendas
        for i in range(len(receita)):
            receita_total += receita[i] #Soma das receitas parciais
        print(f"A quantidade total de vendas foi: {nvendas}")
        sleep(1)
        print(f"A receita total de vendas é: R$ {receita_total}")
        sleep(1)
    else:
        print("Não há vendas!")
        sleep(1)

def valorestoque(): #Função para somar os valores dos produtos do estoque
    if verificar_estoque() is not None:
        valorfinal = 0
        for i in range(len(estoque)):
            valorparcial = estoque[i]['valor'] * estoque[i]['quantidade'] #valores de cada item * cada quantidade no estoque
            valorfinal += valorparcial #Atualização do valor do estoque
        print(f"O valor total do estoque é: R$ {valorfinal}")
        sleep(1)

def categoriaproduto(): #Função para mostrar o produto e sua categoria
    if verificar_estoque() is not None:
        for i in range(len(estoque)):
            print(f"Produto - {estoque[i]['nome-produto']}\t Categoria - {estoque[i]['categoria']}")
            sleep(1)
    