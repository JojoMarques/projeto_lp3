from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ #importação

# Aluno aluno = new Aluno ()
# aluno = new Aluno () --> mas não precisa do new
# aluno = Aluno ()>

# instancia um objeto flask que representa a aplicação
app = Flask("minha aplicação") # nome da aplicação passado no construtor

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# página home -/
@app.route("/")
def home ():
    return render_template("home.html")
# "app" (Flask), td vez q vc tiver uma rota, e essa rota for /, execute essa função em seguida (a home)

# página contato - /contato
@app.route("/contato")
def contato():
    return render_template("contato.html")
# "app" (Flask), td vez q vc tiver uma rota, e essa rota for /contato, execute essa função em seguida (a contato)

lista_produtos = [
       {"nome":"Coca-cola", "descricao":"Mata a sede"},
       {"nome":"Doritos", "descricao":"Suja a mão"},
       {"nome":"Chocolate","descricao":"Bom demais"}
   ]
# página produtos - /produtos
@app.route("/produtos")
def produtos():
   return render_template("produtos.html", produtos = lista_produtos)
# "app" (Flask), td vez q vc tiver uma rota, e essa rota for /produtos, execute essa função em seguida (a produtos)
# as funções tem que ser executadas quando forem requisitadas 


#                                               EXERCÍCIO - REPOSIÇÃO (13/06)

# página - /gerar-cpf (deve devolver um cpf aleatório)
@app.route("/gerar-cpf")
def gerar_cpf():
    cpf = CPF ()
    cpf_gerado = cpf.generate(True)
    return render_template("cpf.html", cpf = cpf_gerado)
    #return f"<h1> CPF gerado: {cpf_gerado} </h1>"

# página - /gerar-cnpj (deve devolver um cnpj aleatório)
@app.route("/gerar-cnpj")
def gerar_cnpj():
    cnpj = CNPJ()
    cnpj_gerado = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = cnpj_gerado)
    #return f"<h1> CNPJ gerado: {cnpj_gerado} </h1>"

# página - /servicos (deve devolver um título com "Nossos serviços")
@app.route("/servicos")
def servicos():
    return "<h1>Nossos serviços</h1>"

#                                               EXERCÍCIO - REPOSIÇÃO (20/06)

@app.route("/termos-de-uso")
def termos_de_uso():
    return render_template("termos-de-uso.html")


@app.route("/politica-privacidade")
def politica_privacidade():
    return render_template("politica-privacidade.html")

@app.route("/como-utilizar")
def como_utilizar():
    return render_template("como-utilizar.html")

#                                                           AULA - 25/06
# método GET para obter o formulário (por padrão)
@app.route("/produtos/cadastro")
def cadastro_produtos():
    return render_template("cadastro_produto.html")

#POST para receber os dados do form
#objeto request organiza os dados do formulário em um dicionário chamado form
@app.route("/produtos", methods=['POST'])
def salvar_produtos():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = { "nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos = lista_produtos)
    
# roda direto por aqui
app.run()
