from models.movie import Movie
from bottle import request, redirect, template
import random
from data_managers.movie_manager import save_movie, get_movie_by_id, calculo_avaliacoes, avaliar_filme
class MovieController:
    def __init__(self):
        pass


    def process_movie(self):
        title = request.forms.get('title')
        description = request.forms.get('description')
        director = request.forms.get('director')
        img_url = request.forms.get('img_url')


        id = random.randint(1000, 9999)
        filme = Movie(id=id, title=title, description=description, director=director, img_url=img_url)
        # passar essa logica para dentro do save_movie/save_user
        filme_dict = filme.to_dict()  # converte para dict
        save_movie(filme_dict)
        return redirect("/")
    
    def exibe_filme(self, id):
        filme = get_movie_by_id(id)
        calculo_avaliacoes(filme)
        return template('movie', filme=filme)
    
    def avalia_filme(self):
        filme_id = int(request.forms.get('filme_id'))
        nota = int(request.forms.get('nota'))
        avaliar_filme(filme_id, nota)  
        return redirect(f'/movie/{filme_id}')