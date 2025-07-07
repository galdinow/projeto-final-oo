from models.movie import Movie
from bottle import request, redirect, template
import random
from data_managers.movie_manager import save_movie, get_movie_by_id, calculo_avaliacoes, avaliar_filme
from controllers.base_controller import BaseController
class MovieController(BaseController):
    def __init__(self):
        pass

    def setup_routes(self,app):
        app.route('/cadastrofilme', method='GET', callback=self.exibir_formulario_cadastro)
        app.route('/cadastrofilme', method='POST', callback=self.process_movie)
        app.route("/movie/<id:int>", method="GET", callback=self.exibe_filme)
        app.route('/listafilmes', method="GET", callback=self.listar_filmes)
        app.route('/avaliar-filme', method="POST", callback=self.avalia_filme)



    
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
        from data_managers.movie_manager import calculo_avaliacoes
        filme = get_movie_by_id(id)
        calculo_avaliacoes(filme)
        return  self.render('movie', filme=filme)
    
    def avalia_filme(self):
        from data_managers.movie_manager import avaliar_filme
        filme_id = int(request.forms.get('filme_id'))
        nota = int(request.forms.get('nota'))
        avaliar_filme(filme_id, nota)  
        return redirect(f'/movie/{filme_id}')
    

    def exibir_formulario_cadastro(self):
        return self.render(template='cadastrofilme')

    def listar_filmes(self):
        from data_managers.movie_manager import load_movies
        filmes = load_movies() 
        return self.render('listafilmes', filmes=filmes)

