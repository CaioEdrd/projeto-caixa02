from time import sleep
import Funcao_Conversão, datetime
import json

estoque = []    
    
qtd_estoque = []

#categorias

alimentos = []
bebidas = []
limpeza = []
higiene = []
outros = []

vendas = []
receita = []

def saudacao(mercado): #Verificará a hora e mostrará uma das saudações
    hora_agora = datetime.datetime.now().hour
    int(hora_agora)
    if hora_agora > 00 and hora_agora < 12:
        print(f"\nBom dia!\nBem-Vindo ao controle de caixa {mercado.capitalize()}!\n")
    elif hora_agora >= 12 and hora_agora < 18:
        print(f"\nBoa tarde!\nBem-Vindo ao controle de caixa {mercado.capitalize()}!\n")
    elif hora_agora >= 18 and hora_agora <= 23:
        print(f"\nBoa noite!\nBem-Vindo ao controle de caixa {mercado.capitalize()}!\n")
    


def verificar_estoque(): #Verifica os produtos do estoque
    if qtd_produtos() is not None:
        if real_estoque > 0:
            return real_estoque
    else:
        print("Estoque vazio!")
        sleep(1)
        
def exibe_estoque(): #Mostra os produtos do estoque
    if verificar_estoque() is not None: #verifica se o estoque não está vazio
        print(f"Estoque com {len(estoque)} produto(s)!")
        sleep(1)
        for i in range(len(estoque)): #Mostra cada produto
            print(f"Produto - {estoque[i]['nome-produto']}\t Valor - R$ {estoque[i]['valor']}\t Categoria - {estoque[i]['categoria']}\t Quantidade - {estoque[i]['quantidade']}")
            sleep(1) 
            if estoque[i]['quantidade'] < 5: #Caso a quantidade seja menor que 5 mostrará essa mensagem
                print(f"\"{estoque[i]['nome-produto']}\" está com baixo estoque, necessário reabastecimento!")
    else:
        print("Estoque sem produtos!")

def verificar_categoria(): #Verifica se a categoria é válida
    global categoria
    global nome_categoria
    categoria = input("Digite a primeira letra da categoria do produto ([A]limentos, [B]ebidas, [L]impeza, [H]igiene, [O]utros): ").lower()
    sleep(1)
    if categoria in ['a', 'b', 'l', 'h', 'o']: #verifica se a categoria digitada está na lista   
        print("Categoria válida")
        if categoria == 'a':
            nome_categoria = "Alimento"
        sleep(1)

        if categoria == 'b':
            nome_categoria = "Bebida"
        sleep(1)

        if categoria == 'l':
            nome_categoria = "Limpeza"
        sleep(1)

        if categoria == 'h':
            nome_categoria = "Higiene"
        sleep(1)

        if categoria == 'o':
            nome_categoria = "Outros"
        sleep(1)       

        return categoria       
    else:
        print("Categoria inválida")
        sleep(1)
        return None
        
def verifica_produto_estoque(): #Verifica se o produto digitado já está no estoque
    global index_produto_estoque
    for i in range(len(estoque)): #Passa em cada produto para verificar se o produto já está no estoque
        if nome_produto == estoque[i]['nome-produto']:
            index_produto_estoque = i 
            return index_produto_estoque #Salva o index do produto na lista 'estoque'

                
def adicionar_produto(): #Adicionar um produto ao estoque
    if verificar_categoria() is not None: #Verifica se a categoria é válida
        global nome_produto
        nome_produto = input("Qual o produto a ser adicionado? ").capitalize().strip()
        sleep(1)
        if verifica_produto_estoque() is None: #Verifica se já tem o produto no estoque
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
            nome_produto = {    #Dicionário do produto
            'nome-produto' : nome_produto.capitalize().strip(),
            'valor' : valor,
            'categoria' : nome_categoria,
            'quantidade' : quantidade,}
            estoque.append(nome_produto)
            if categoria == "a":
                alimentos.append(nome_produto)
            elif categoria == "b":
                bebidas.append(nome_produto)
            elif categoria == 'l':
                limpeza.append(nome_produto)
            elif categoria == 'h':
                higiene.append(nome_produto)
            elif categoria == 'o':
                outros.append(nome_produto)
            
        else: #Caso já tenha o produto no estoque só solicita a quantidade
            if nome_categoria ==  estoque[index_produto_estoque]['categoria'] : #Verifica se a categoria digitada é igual a do produto que já está no estoque com o mesmo nome
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
            else: #Caso seja uma categoria que não corresponde ao produto já adicionado anteriormente e que seria apenas atualizada a sua quantidade
                print("A categoria do produto não corresponde a ele!")
                sleep(1)

def qtd_produtos(): #Verifica a quantidade de produtos no estoque
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
        real_estoque = produtos_estoque - venda_estoque #Quantidade mais atualizada do produto
        return real_estoque


def vender(): #Vender um produto do estoque
    global nome_produto
    global qtd_venda
    if verificar_estoque() is not None: #Verifica se há produto no estoque
        exibe_estoque()
        nome_produto = input("Digite qual produto deseja vender: ").capitalize().strip()
        sleep(1)
        if verifica_produto_estoque() is None: #Verifica se o produto digitado está no estoque
            print("Não há esse produto no estoque!")
            sleep(1)
        else: #Caso o produto esteja no estoque
            qtd_venda = input(f"Digite a quantidade de {estoque[index_produto_estoque]['nome-produto']} a ser vendida: ")
            if not qtd_venda.isdigit(): #verificação se a quantidade digitada não é válida
                print("Quantidade inválida")
                sleep(1)
                return
            else:
                qtd_venda = int(qtd_venda)
                verifica_produto_estoque()
                if qtd_venda < 0 or qtd_venda > estoque[index_produto_estoque]['quantidade']: #Verifica se a quantidade é válida
                    print("A quantidade digitada não é válida!")
                    sleep(1)
                    return
                else:
                    while True:
                        moeda_usuario = input("Sua moeda é o REAL ?\n [S]im\t[N]ão : ").upper() #solicita a moeda do usuário para conversão
                        if moeda_usuario == 'N' or moeda_usuario == 'NAO' or moeda_usuario == 'NÃO':
                            if Funcao_Conversão.verificacao_moeda() is not None: #verifica se a moeda digitada é válida
                                Funcao_Conversão.conversao()
                                estoque[index_produto_estoque]['quantidade'] -= qtd_venda
                                receita_parcial = (qtd_venda * Funcao_Conversão.conversao_moeda) #atualiza a receita parcial já com o valor convertido
                                print(f"A receita obtida com essa venda foi de: R$ {receita_parcial}")
                                receita.append(receita_parcial)
                                vendas.append(qtd_venda)
                                break
                        if moeda_usuario == 'S' or moeda_usuario == 'SIM': #Caso a moeda seja o Real
                            estoque[index_produto_estoque]['quantidade'] -= qtd_venda
                            receita_parcial = qtd_venda * estoque[index_produto_estoque]['valor']
                            receita.append(receita_parcial)
                            vendas.append(qtd_venda)
                            break
                        else:
                            print("Resposta inválida")
def mostrar_receita(): #Mostra as vendas
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

def valorestoque(): #Mostra o valor do estoque
    if verificar_estoque() is not None:
        valorfinal = 0
        for i in range(len(estoque)):
            valorparcial = estoque[i]['valor'] * estoque[i]['quantidade']
            valorfinal += valorparcial
        print(f"O valor total do estoque é: R$ {valorfinal}")
        sleep(1)

def categoriaproduto(): #Mostra os produtos e suas categorias
    if verificar_estoque() is not None:
        if len(alimentos) > 0:
            print('Categoria dos alimentos:')
            for i in range(len(alimentos)):
                print(alimentos[i]['nome-produto'])
            sleep(1)
        if len(bebidas) > 0:
            print('Categoria das bebidas:')
            for i in range(len(bebidas)):
                print(bebidas[i]['nome-produto'])
            sleep(1)
        if len(limpeza) > 0:
            print('Categoria dos limpeza:')
            for i in range(len(limpeza)):
                print(limpeza[i]['nome-produto'])
            sleep(1)
        if len(higiene) > 0:
            print('Categoria dos higiene:')
            for i in range(len(higiene)):
                print(higiene[i]['nome-produto'])
            sleep(1)
        if len(outros) > 0:
            print('Itens de outras categorias:')
            for i in range(len(outros)):
                print(outros[i]['nome-produto'])
            sleep(1)
       