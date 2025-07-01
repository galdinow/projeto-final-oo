import json
from models.user import User
class UserController:

    @staticmethod
    def to_dict(user):
        return {"id":user.user_id, "name": user.username, "email": user.email, "password": user.password}
    
    @staticmethod
    def create_json_file(filename):
        json_list = []
        with open(filename,mode="w") as file:
            json.dump(json_list, file)
        
    

    # talvez fazer um controle de erros depois
    @staticmethod
    def save_user(user):
        with open("teste", "r") as file:
            existing_json = json.load(file)
            updated_json = existing_json
            updated_json.append(user)
        with open("teste", "w") as file:
            json.dump(updated_json, file)