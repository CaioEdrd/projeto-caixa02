from time import sleep

estoque = []    
    
qtd_estoque = []

vendas = []
receita = []

def verificar_estoque():
    if qtd_produtos() is not None:
        if real_estoque > 0:
            return real_estoque
    else:
        print("Estoque vazio!")
        sleep(1)
        
def exibe_estoque():
    if verificar_estoque() is not None:
        print(f"Estoque com {len(estoque)} produto(s)!")
        sleep(1)
        for i in range(len(estoque)):
            print(f"Produto - {estoque[i]['nome-produto']}\t Valor - R$ {estoque[i]['valor']}\t Categoria - {estoque[i]['categoria']}\t Quantidade - {estoque[i]['quantidade']}")
            sleep(1)
            if estoque[i]['quantidade'] < 5:
                print(f"\"{estoque[i]['nome-produto']}\" está com baixo estoque, necessário reabastecimento!")

def verificar_categoria():
    global categoria
    categoria = input("Digite a primeira letra da categoria do produto ([A]limentos, [B]ebidas, [L]impeza, [H]igiene, [O]utros): ").lower()
    sleep(1)
    if categoria in ['a', 'b', 'l', 'h', 'o']:    
        print("Categoria válida")
        sleep(1)
        return categoria
    else:
        print("Categoria inválida")
        sleep(1)
        return None
        
def verifica_produto_estoque():
    for i in range(len(estoque)):
        if nome_produto == estoque[i]['nome-produto']:
            global index_produto_estoque
            index_produto_estoque = i
            return index_produto_estoque

                
def adicionar_produto():
    if verificar_categoria() is not None:
        global nome_produto
        nome_produto = input("Qual o produto a ser adicionado? ")
        sleep(1)
        if verifica_produto_estoque() is None:
            valor = input("Qual o valor do produto: ")
            sleep(1)
            try:#verificação se o preço digitado é válido
                valor = float(valor)  # Tente converter para float
                if valor < 0 :
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
            nome_produto = {    
            'nome-produto' : nome_produto,
            'valor' : valor,
            'categoria' : categoria,
            'quantidade' : quantidade,}
            estoque.append(nome_produto)               
        else:
            if categoria ==  estoque[index_produto_estoque]['categoria'] : 
                qtd_produto = input("Qual a quantidade do produto? ")
                sleep(1)
                if not qtd_produto.isdigit(): #verificação se a quantidade digitada é válida
                    print("Quantidade inválida")
                    sleep(1)
                    return
                else:
                    qtd_produto = int(qtd_produto)
                estoque[index_produto_estoque]['quantidade'] += qtd_produto
                qtd_estoque.append(estoque[index_produto_estoque]['quantidade'])
            else:
                print("A categoria do produto não corresponde a ele!")
                sleep(1)

def qtd_produtos():
    global real_estoque
    venda_estoque = 0
    produtos_estoque = 0
    if len(qtd_estoque) > 0:
        i = 0
        for i in range(len(qtd_estoque)):
            produtos_estoque += qtd_estoque[i]
            i+=1
        for i in range(len(vendas)):
            venda_estoque += vendas[i]
            i+=1
        real_estoque = produtos_estoque - venda_estoque
        return real_estoque

def vender():
    global nome_produto
    if verificar_estoque() is not None:
        exibe_estoque()
        nome_produto = input("Digite qual produto deseja vender: ")
        sleep(1)
        if verifica_produto_estoque() is None:
            print("Não há esse produto no estoque!")
            sleep(1)
        else:
            qtd_venda = input(f"Digite a quantidade de {estoque[index_produto_estoque]['nome-produto']} a ser vendida: ")
            if not qtd_venda.isdigit(): #verificação se a quantidade digitada é válida
                print("Quantidade inválida")
                sleep(1)
                return
            else:
                qtd_venda = int(qtd_venda)
                verifica_produto_estoque()
                if qtd_venda < 0 or qtd_venda > estoque[index_produto_estoque]['quantidade']:
                    print("A quantidade digitada não é válida!")
                    sleep(1)
                    return
            estoque[index_produto_estoque]['quantidade'] -= qtd_venda
            receita_parcial = qtd_venda * estoque[index_produto_estoque]['valor']
            receita.append(receita_parcial)
            vendas.append(qtd_venda) 

def mostrar_receita():
    if len(vendas) > 0:
        receita_total = 0
        nvendas = 0
        for i in range(len(vendas)):
            nvendas += vendas[i]
        for i in range(len(receita)):
            receita_total += receita[i]
        print(f"A quantidade total de vendas foi: {nvendas}")
        sleep(1)
        print(f"A receita total de vendas é: R$ {receita_total}")
        sleep(1)
    else:
        print("Não há vendas!")
        sleep(1)

def valorestoque():
    if verificar_estoque() is not None:
        valorfinal = 0
        for i in range(len(estoque)):
            valorparcial = estoque[i]['valor'] * estoque[i]['quantidade']
            valorfinal += valorparcial
        print(f"O valor total do estoque é: R$ {valorfinal}")
        sleep(1)

def categoriaproduto():
    if verificar_estoque() is not None:
        for i in range(len(estoque)):
            print(f"Produto - {estoque[i]['nome-produto']}\t Categoria - {estoque[i]['categoria']}")
            sleep(1)
       