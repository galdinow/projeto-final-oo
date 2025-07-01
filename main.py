from bottle import route, run, template
from controllers.user_controller import *
from models.user import User


aluno = User("0", "djota", "dota@email", "123")
UserController.create_json_file("teste")
#fazer ela ir para o filepath certo(diretorio data)
aluno_dict = UserController.to_dict(aluno)
UserController.save_user(aluno_dict)


# @route("/") 
# def home():
#     return template("home")

# run(debug=True,reloader=True,)
