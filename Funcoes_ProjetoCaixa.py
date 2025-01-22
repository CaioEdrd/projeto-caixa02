produto = {
    'produto' : '',
    'valor' : 0.0,
    'categoria' : '',
    'quantidade' : 0,
}

estoque = [
    [], #produto 0
    [], #valor 1
    [], #categoria 2
    [], #quantidade 3
]

vendas = []
receita = []

def verificar_estoque():
    if len(estoque[0]) > 0:
        return estoque
    else:
        print("Estoque vazio!")
        
def exibe_estoque():
    if verificar_estoque() is not None:
        print(f"Estoque com {len(estoque[0])} produto(s)!")
        for i in range(len(estoque[0])):
            print(f"Produto - {estoque[0][i]}\t Valor - R$ {estoque[1][i]}\t Categoria - {estoque[2][i]}\t Quantidade - {estoque[3][i]}")
    
def verificar_categoria():
    global categoria
    categoria = input("Digite a primeira letra da categoria do produto ([A]limentos, [B]ebidas, [L]impeza, [H]igiene, [O]utros): ").lower()
    if categoria in ['a', 'b', 'l', 'h', 'o']:    
        if categoria == 'a':
            produto["categoria"] = "alimento"
        elif categoria == 'b':
            produto["categoria"] = "bebidas"
        elif categoria == 'l':
            produto["categoria"] = "limpeza"
        elif categoria == 'h':
            produto["categoria"] = "higiene"
        elif categoria == 'o':
            produto["categoria"] = "outros"
        return categoria
    else:
        print("Categoria inválida")
        

def adicionar_produto():
    if verificar_categoria() is not None:
        produto['produto'] = input("Qual o produto a ser adicionado? ")
        if produto["produto"] in estoque[0]:
           index_produto = estoque[0].index(produto["produto"])
           if categoria ==  estoque[2][index_produto][0] : 
            produto['quantidade'] = int(input("Qual a quantidade do produto? "))
            estoque[3][index_produto] += produto["quantidade"]
           else:
               print("A categoria do produto não corresponde a ele!")         
        else:
            produto['valor'] = float(input("Qual o valor do produto? "))
            produto['quantidade'] = int(input("Qual a quantidade do produto? "))
            estoque[0].append(produto['produto'])    
            estoque[1].append(produto['valor'])
            estoque[2].append(produto["categoria"])    
            estoque[3].append(produto['quantidade'])    
    else:
        return
    
def vender():
    if verificar_estoque() is not None:
        exibe_estoque()
        produto["produto"] = input("Digite qual produto deseja vender: ")
        if produto["produto"] not in estoque[0]:
            print("Não há esse produto no estoque!")
        else:
            index_produto = estoque[0].index(produto["produto"])
            qtd_venda = int(input(f"Digite a quantidade de {produto['produto']} a ser vendida: "))
            estoque[3][index_produto] -= qtd_venda
            receita_parcial = qtd_venda * estoque[1][index_produto]
            receita.append(receita_parcial)
            vendas.append(qtd_venda)
            
    else:
        print("Não há produtos para ser vendidos!")
    
def mostrar_receita():
    if len(vendas) > 0:
        receita_total = 0
        nvendas = 0
        for i in range(len(vendas)):
            nvendas += vendas[i]
        for i in range(len(receita)):
            receita_total += receita[i]
        print(f"A quantidade total de vendas foi: {nvendas}")
        print(f"A receita total de vendas é: R$ {receita_total}")
    else:
        print("Não há vendas!")

def valorestoque():
    if verificar_estoque() is not None:
        valorfinal = 0
        for i in range(len(estoque[1])):
            valorparcial = estoque[1][i] * estoque[3][i]
            valorfinal +=valorparcial
        print(f"O valor total do estoque é: R$ {valorfinal}")
    else:
        print("Não há produtos no estoque!")

def categoriaproduto():
    if verificar_estoque() is not None:
        for i in range(len(estoque[2])):
            print(f"Produto - {estoque[0][i]}\t Categoria - {estoque[2][i]}")
    else:
        print("Não há produto no estoque!")
        