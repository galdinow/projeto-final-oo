import json

# talvez fazer um controle de erros depois 
# ver se isso realmente tem que existir


def save_movie(movie):
    with open("data/movies.json", "r") as file:
        existing_json = json.load(file)
        updated_json = existing_json
        updated_json.append(movie)
    with open("data/movies.json", "w") as file:
        json.dump(updated_json, file, indent=4)