import json

# talvez fazer um controle de erros depois 
# ver se isso realmente tem que existir


def save_movie(movie):
    with open("data/movies.json", "r", encoding="utf-8") as file:
        existing_json = json.load(file)
        updated_json = existing_json
        updated_json.append(movie)
    with open("data/movies.json", "w", encoding="utf-8") as file:
        json.dump(updated_json, file, indent=4,ensure_ascii=False)

# sera se a funcao ta "magica" demais? com o filepath sendo selecionado sozinho?
def load_movies():
    with open("data/movies.json", "r", encoding="utf-8") as file:
        movie_list = json.load(file)
        return movie_list


# mudar "deu errado " dps
def get_movie_by_id(id):
    for filme in load_movies():
        if filme["id"] == id:
            return filme
    return None


def avaliar_filme(id, nota):
    nota = int(nota)
    filmes = load_movies()
    for filme in filmes:
        if filme["id"] == id:
            if "avaliacoes" not in filme:
                filme["avaliacoes"] = []
            filme["avaliacoes"].append(nota)
            break
    with open("data/movies.json", "w") as file:
        json.dump(filmes, file, indent=4)


def calculo_avaliacoes(filme):
    if not filme:
        return "Filme não encontrado"
    if 'avaliacoes' in filme and filme['avaliacoes']:
        soma_notas = sum(filme['avaliacoes'])
        num_avaliacoes = len(filme['avaliacoes'])   
        filme['media_avaliacoes'] = f"{soma_notas / num_avaliacoes:.1f}"
        filme['num_avaliacoes'] = num_avaliacoes
    else:
        filme['media_avaliacoes'] = None
        filme['num_avaliacoes'] = 0

