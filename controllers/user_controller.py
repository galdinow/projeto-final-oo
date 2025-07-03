import json
from models.user import User
from controllers.base_controller import BaseController

class UserController(BaseController):
    
    # talvez fazer um controle de erros depois e arrumar identacao
    @staticmethod
    def save_user(user):
        with open("teste", "r") as file:
            existing_json = json.load(file)
            updated_json = existing_json
            updated_json.append(user)
        with open("teste", "w") as file:
            json.dump(updated_json, file)

    

    # mudar esse metodo depois para 
    @staticmethod
    def to_dict(user):
        return {"id":user.user_id, "name": user.username, "email": user.email, "password": user.password}