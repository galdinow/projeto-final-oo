from bottle import route, run, template, request, redirect
from controllers.user_controller import *
from models.user import User
from models.movie import Movie
from controllers.movie_controller import MovieController
from data_managers.user_manager import save_user, create_json_file
import random


aluno = User("0", "djota", "dota@email", "123")
create_json_file("teste")
#fazer ela ir para o filepath certo(diretorio data)
aluno_dict = aluno.to_dict()
save_user(aluno_dict)




@route('/cadastrar-filme', method='POST')
def cadastrar_filme():
    title = request.forms.get('title')
    description = request.forms.get('description')
    director = request.forms.get('director')
    img_url = request.forms.get('img_url')


    id = random.randint(1000, 9999)
    filme = Movie(id=id, title=title, description=description, director=director, img_url=img_url)

    MovieController.adicionar_filme(filme)
#depois adicionar
#return redirect("/")

@route('/filme/<id:int>')
def exibir_filme(id):
    filme = MovieController.get_movie_by_id(id)
    if filme:
        return template('filme_detalhes', filme=filme)
    return "Filme não encontrado"





# @route("/") 
# def home():
#     return template("home")

# run(debug=True,reloader=True,)
