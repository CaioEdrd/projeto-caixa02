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
        if produto["produto"] in estoque[0]: #verifica se o produto já faz parte do estoque
           index_produto = estoque[0].index(produto["produto"]) #relaciona o produto com o index
           if categoria ==  estoque[2][index_produto][0] : #verifica se a categoria digitada corresponde ao produto já adicionado
            produto['quantidade'] = input("Qual a quantidade do produto? ")
            if not produto["quantidade"].isdigit(): #verifica se a quantidade digitada é um número
                print("Quantidade inválida! ")
                return
            else:
                produto["quantidade"] = int(produto["quantidade"]) 
                estoque[3][index_produto] += produto["quantidade"] #atualiza a quantidade do produto que já estava no estoque
           else:
               print("A categoria do produto não corresponde a ele!")         
        else: #caso seja um produto novo
            produto['valor'] = input("Qual o valor do produto? ")
            try: #tratamento de erro para o valor do produto
                produto["valor"] = float(produto["valor"])
                if produto["valor"] < 0:
                    print("Preço inválido!")
                    return
            except ValueError: #caso dê erro de valor
                print("Preço inválido!")
                return
                
            produto['quantidade'] = input("Qual a quantidade do produto? ")
            if not produto["quantidade"].isdigit():
                print("Quantidade inválida! ")
                return
            else:
                produto["quantidade"] = int(produto["quantidade"])
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
        if produto["produto"] not in estoque[0]: #verifica se o produto digitado não está no estoque
            print("Não há esse produto no estoque!")
        else: #Caso esteja no estoque executa isso:
            index_produto = estoque[0].index(produto["produto"]) #verifica qual o index do produto
            qtd_venda = input(f"Digite a quantidade de {produto['produto']} a ser vendida: ")
            if not qtd_venda.isdigit(): #Verifica se a quantidade digitada não é um número inteiro
                print("Quantidade inválida!")
                return
            else: #Caso for um número inteiro:
                qtd_venda = int(qtd_venda)
                if qtd_venda > estoque[3][index_produto]: #Verifica se a quantidade é maior que o estoque
                    print(f"Quantidade a ser vendida é maior que estoque do produto {estoque[0][index_produto]}!")
                    return
                else:
                    estoque[3][index_produto] -= qtd_venda #diminui a quantidade do estoque com a quantidade vendida
                    receita_parcial = qtd_venda * estoque[1][index_produto] #atualiza a receita parcial de vendas
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
        