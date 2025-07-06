import json
import random
from models.user import User
from controllers.base_controller import BaseController
# ver se eu uso tudo isso msm dps
from bottle import route, run, template, request, redirect
from data_managers import user_manager

class UserController:
    def __init__(self):
        pass
    
# ver dps se as rotas na verdade ficam aq
    
    def cadastro_usuario(self):
        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")
        #tem um jeito melhor de fazer isso
        id = random.randint(1000, 9999)

        user = User(id, username, email, password)
        dict_user = user.to_dict()
        user_manager.save_user(dict_user)
        return redirect("/")