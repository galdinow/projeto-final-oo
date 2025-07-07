import json


def save_user(user):
    with open("data/users.json", "r") as file:
        existing_json = json.load(file)
        updated_json = existing_json
        updated_json.append(user)
    with open("data/users.json", "w") as file:
        json.dump(updated_json, file, indent=4)

def create_json_file(filename):
    json_list = []
    with open("data/" + filename,mode="w") as file:
        json.dump(json_list, file, indent=4)
def load_users():
    with open("data/users.json", "r") as file:
        users_list = json.load(file)
        return users_list

def procura_usuario(username, password):
    for i in load_users():
        if (i["name"] == username and i["password"] == password):
            return True