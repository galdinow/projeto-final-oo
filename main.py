from bottle import route, run, template, request, redirect, Bottle
from controllers.user_controller import UserController
from controllers.movie_controller import MovieController
from models.movie import Movie
import random
from data_managers.movie_manager import get_movie_by_id
from data_managers.movie_manager import save_movie
from bottle import static_file
from data_managers.movie_manager import load_movies
from data_managers.movie_manager import avaliar_filme

app = Bottle()
movie_controller = MovieController()
user_controller = UserController()

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
    return movie_controller.process_movie()

@app.route('/listafilmes')
def listar_filmes():
    filmes = load_movies() 
    return template('listafilmes', filmes=filmes)


@app.route('/movie/<id:int>')
def exibir_filme_rota(id):

    return movie_controller.exibe_filme(id)

@app.route('/avaliar-filme', method='POST')
def avaliar_filme_rota():
    return movie_controller.avalia_filme()

@app.route("/login", method="GET")
def login():
    return template("login")

@app.route("/login", method="POST")
def saving_login():
    return user_controller.process_user()


@app.route("/logon", method="GET")
def logon():
    return template("logon")


@app.route("/logon", method="post")
def checking_logon():
    if user_controller.validating_user():
        return redirect("/")
    return template("logon")


run(host='localhost', port=8080, debug=True, reloader=True, app=app)
