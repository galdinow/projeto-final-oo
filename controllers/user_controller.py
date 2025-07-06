import json
import random
from models.user import User
from controllers.base_controller import BaseController
# ver se eu uso tudo isso msm dps
from bottle import route, run, template, request, redirect, Bottle
from data_managers import user_manager

class UserController:
    def __init__(self):
        pass
    
# ver dps se as rotas na verdade ficam aq
    # def setup_routes(self, app):
    #     app.route("/login", method="GET")


    def process_user(self):
        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")
        #tem um jeito melhor de fazer isso
        id = random.randint(1000, 9999)

        user = User(id, username, email, password)
        dict_user = user.to_dict()
        user_manager.save_user(dict_user)
        return redirect("/")
    #ver se o nome faz sentido
    def validating_user(self):
        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")
        # dps ver como usar a id correta, esse metodo nao pode ta certo
        user = User("1", username, email, password)
        if (user_manager.procura_usuario(user)):
            return True
        else:
            return False