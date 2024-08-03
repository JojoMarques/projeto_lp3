print("teste")
#ler o arquivo (read)

# OPEN
# open: abre o arquivo. carrega os dados do arquivo oem memória
arquivo = open("projeto_lp3/dados.txt")
print(arquivo)
print(arquivo.read()) #função p ler aqruivos
#esse obj representa os dados do arquivo em memória

# READ
#read lê todo o conteudo do arquivo que está em memória
#read leu o conteudo e acabou (se der dnv n tem mais conteúdo p ler)
# --> chamar o arquivo duas vezes não vai funcionar, em que armazenar em uma variavel
#print(f"não vai imprimir {arquivo.read()}")
conteudo = arquivo.read()
print(conteudo)

# CLOSE
arquivo.close()

# WITH 
# abre algum tipo de recurso/estrutura/arquivo e fecha automaticamente quando o codigo sai do escopo do bloco (o que tá dentro))
# abrir sem precisar dar o .close no final
# o arquivo será fechado quando a execução sair do escopo do bloco

with open ("projeto_lp3/dados.txt") as arquivo2:
    print(arquivo2.read())

print("4")
#arquivo2.read() n funfa pq tá fora

with open("projeto_lp3/dados.txt") as arquivo3:
    linhas = arquivo3.readlines() #devolve uma lista de string (a gnt csg manipular ela)
    #readlines retorna uma lista com as linhas
    print(linhas)

with open("projeto_lp3/dados.txt", "r") as arquivo4:
# abre o arquivo dados,txt em modo leitura
# # existe um segundo argumento no with, o mode
# não omite.
    linhas = []
    for linha in arquivo4:
        # ele considera a lista de linhas do arquivo
        linhas.append(linha.strip()) #strip tira os espaços antes e depois
    print(linhas)

# escrever no arquivo
'''
with open("projeto_lp3/dados.txt", "w") as arquivo5:
    arquivo5.write("Abacaxi") #substitui todo o conteúdo
'''

with open("projeto_lp3/dados.txt", "a") as arquivo5:
    #arquivo5.write("Abacaxi") #substitui todo o conteúdo
    arquivo5.write("\nAbacaxi")
    # o problema não é o write, e sim o modo. tem que abrir com "a" de append

'''
# arquivo csv
with open("projeto_lp3/produto.csv","r") as arquivo_produtos:
    produtos = []
    for produto in arquivo_produtos:
        # cada linha é uma string
        produtos.append(produto.strip().split(",")) #usando o sep--> separdaor como vírgula
        #aí fica uma lista de listas (lista com os ddaos das linhas)
    print(produtos)
'''
def obter_produto ():
    with open("projeto_lp3/produto.csv","r") as arquivo_produtos:
        produtos = []
        for produto in arquivo_produtos:
            dados_produto = produto.strip().split(",")
            # tirou o \n, separou por vírgula e retornou uma lista de listas, onde cada linha é uma lista
            produto = {
                "nome": dados_produto[0],
                "descricao": dados_produto[1],
                "preco": float (dados_produto[2]), 
                "imagem": dados_produto[3]
            }
            produtos.append(produto)
        return produtos   
    
print(obter_produto())  

def salvar_produto(nome, descricao, preco, imagem):
        # 1: abrir o arquivo em modo append
    with open ("projeto_lp3/produto.csv", "a") as arquivo_produtos:
        # 2: montar a string com os dados separados por virgula
        texto_produto = f"\n{nome}, {descricao}, {preco}, {imagem}"
        # 3: escrever no arquivo
        arquivo_produtos.write(texto_produto)

print(salvar_produto("Banana", "frutinha", 6.00, "banana.jpg"))  
print(obter_produto())  

