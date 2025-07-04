import json

# talvez fazer um controle de erros depois 

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