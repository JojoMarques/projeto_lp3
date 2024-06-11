from flask import Flask

# Aluno aluno = new Aluno ()
# aluno = new Aluno () --> mas não precisa do new
# aluno = Aluno ()

# instancia um objeto flask que representa a aplicação
app = Flask("minha aplicação") # nome da aplicação passado no construtor

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# página home -/
@app.route("/")
def home ():
    return "<h1>Home page</h1>"
# "app" (Flask), td vez q vc tiver uma rota, e essa rota for /, execute essa função em seguida (a home)

# página contato - /contato
@app.route("/contato")
def contato():
    
    return "<h1>Contato</h1>"
# "app" (Flask), td vez q vc tiver uma rota, e essa rota for /contato, execute essa função em seguida (a contato)

# página produtos - /produtos
@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>"
# "app" (Flask), td vez q vc tiver uma rota, e essa rota for /produtos, execute essa função em seguida (a produtos)


# as funções tem que ser executadas quando forem requisitadas 