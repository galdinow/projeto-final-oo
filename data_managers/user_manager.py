import json

# talvez fazer um controle de erros depois 

def save_user(user):
    with open("data/users.json", "r") as file:
        existing_json = json.load(file)
        updated_json = existing_json
        updated_json.append(user)
    with open("data/users.json", "w") as file:
        json.dump(updated_json, file, indent=4)

# essa funcao nao tem nada a ver com user, temos que tirar ela daq
def create_json_file(filename):
    json_list = []
    with open("data/" + filename,mode="w") as file:
        json.dump(json_list, file, indent=4)
# tratamento de erros
def load_users():
    with open("data/users.json", "r") as file:
        users_list = json.load(file)
        return users_list
# melgorar o for (i)
# n sei se isso era pra estar aq
# melhorar nome
# n eh possivel q tem varias funcoes so retornando true isso nao pode ta certo
def procura_usuario(user):
    for i in load_users():
        if (i["name"] == user.username and i["password"] == user.password):
            return True