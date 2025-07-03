from bottle import route, run, template, request, redirect
from controllers.user_controller import *
from models.user import User
from models.movie import Movie
from controllers.movie_controller import MovieController


aluno = User("0", "djota", "dota@email", "123")
UserController.create_json_file("teste")
#fazer ela ir para o filepath certo(diretorio data)
aluno_dict = UserController.to_dict(aluno)
UserController.save_user(aluno_dict)




@route('/cadastrar-filme,', method='POST')
def cadastrar_filme():
    title = request.forms.get('title')
    description = request.forms.get('description')
    director = request.forms.get('director')
    img_url = request.forms.get('img_url')

filme = Movie(id, title=title, description=description, director=director, img_url=img_url)


# @route("/") 
# def home():
#     return template("home")

# run(debug=True,reloader=True,)
