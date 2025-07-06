from bottle import route, run, template, request, redirect
from controllers.user_controller import UserController
from models.user import User
from models.movie import Movie
from data_managers.user_manager import save_user, create_json_file
import random
from data_managers.movie_manager import get_movie_by_id
from data_managers.movie_manager import save_movie
from bottle import static_file


# Quando tudo estiver funcionando:
# organizar as rotas dentro das controllers
# fazer autenticacao de usuario

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def index():
    return template('index') 

@route('/cadastrar-filme', method='POST')
def cadastrar_filme():
    title = request.forms.get('title')
    description = request.forms.get('description')
    director = request.forms.get('director')
    img_url = request.forms.get('img_url')


    id = random.randint(1000, 9999)
    filme = Movie(id=id, title=title, description=description, director=director, img_url=img_url)

    save_movie(filme)

    return redirect("/")

@route('/filme/<id:int>')
def exibir_filme(id):
    filme = get_movie_by_id(id)
    if filme:
        return template('filme_detalhes', filme=filme)
    return "Filme não encontrado"


user_controller = UserController()
#talvez mudar o nome dps
@route("/login", method="GET")
def login():
    return template("login")

@route("/login", method="POST")
def saving_login():
    return user_controller.cadastro_usuario()

# pra q serve setup routing?


run(host='localhost', port=8080, debug=True, reloader=True)
