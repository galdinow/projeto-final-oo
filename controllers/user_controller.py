import json
import random
from models.user import User
from controllers.base_controller import BaseController
from bottle import route, run, template, request, redirect, Bottle
from data_managers import user_manager

class UserController(BaseController):
    def __init__(self):
        pass
    def setup_routes(self, app):
        app.route('/login', method="GET", callback=self.login)
        app.route('/login', method="POST", callback=self.process_user)
        app.route('/logon', method="GET", callback=self.logon)

    def logon(self):
        return self.render("logon")

    def login(self):
        return self.render("login")
    def process_user(self):
        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")
        id = random.randint(1000, 9999)

        user = User(id, username, email, password)
        dict_user = user.to_dict()
        user_manager.save_user(dict_user)
        return redirect("/")
    def validating_user(self):
        username = request.forms.get("username")
        email = request.forms.get("email")
        password = request.forms.get("password")

        if (user_manager.procura_usuario(username, password)):
            return True
        else:
            return False