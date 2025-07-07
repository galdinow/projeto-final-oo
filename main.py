from bottle import route, run, template, request, redirect, Bottle
from controllers.user_controller import UserController
from models.movie import Movie
import random
from data_managers.movie_manager import get_movie_by_id
from data_managers.movie_manager import save_movie
from bottle import static_file

# Quando tudo estiver funcionando:
# organizar as rotas dentro das controllers
# fazer autenticacao de usuario
# separar o css de dentro dos templates
# usar o base.tpl em todos os templates
# ver o quao nescessario eh criar uma instancia do bottle
# apagar os templates nao utilizados
# padronizar o codigo em uma unica lingua
# conferir se tudo esta onde deveria estar(base controller tbm)
# fazer diagrama de classes
# verificar os 4 pilares de oo
# ver o quao viavel eh fazer um hash da senha
app = Bottle()
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@app.route('/')
def index():
    return template('index') 

@app.route('/cadastrofilme', method='GET')
def exibir_formulario_cadastro():
    return template('cadastrofilme')


@app.route('/cadastrofilme', method='POST')
def cadastrar_filme():
    title = request.forms.get('title')
    description = request.forms.get('description')
    director = request.forms.get('director')
    img_url = request.forms.get('img_url')


    id = random.randint(1000, 9999)
    filme = Movie(id=id, title=title, description=description, director=director, img_url=img_url)
    # passar essa logica para dentro do save_movie/save_user
    filme_dict = filme.to_dict()  # converte para dict
    save_movie(filme_dict)


    return redirect("/")

@app.route('/movie/<id:int>')
def exibir_filme(id):
    filme = get_movie_by_id(id)
    if filme:
        return template('movie', filme=filme)
    return "Filme não encontrado"


user_controller = UserController()
#talvez mudar o nome dps
@app.route("/login", method="GET")
def login():
    return template("login")

@app.route("/login", method="POST")
def saving_login():
    return user_controller.process()


@app.route("/logon", method="GET")
def logon():
    return template("logon")


@app.route("/logon", method="post")
def checking_logon():
    if user_controller.validating_user():
        return redirect("/")
    #ver como faz pra aparecer a mensagem de erro
    return template("logon")
# pra q serve setup routing?


run(host='localhost', port=8080, debug=True, reloader=True, app=app)
