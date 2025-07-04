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

# sera se a funcao ta "magica" demais? com o filepath sendo selecionado sozinho?
def load_movies():
    with open("data/movies.json", "r") as file:
        movie_list = json.load(file)
        return movie_list


#fazer uma funcao que le os filmes salvos em json e implementar ela nessa funcao
# nao testei ainda
# acho q a funcao nao retornar nada nao faz muito sentido
def get_movie_by_id(id):
    for filme in load_movies():
        if filme["id"] == id:
            return print(filme["title"])
    return print("deu errado")
