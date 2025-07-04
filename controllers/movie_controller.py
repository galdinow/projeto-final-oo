from models.movie import Movie

class MovieController:

    filmes = [] #depois trocar pra json

    @staticmethod
    def to_dict(movie):
        return {"id":movie.id, "title":movie.title, "description": movie.description, "director":movie.director, "img_url":movie.img_url}
    
    @staticmethod
    def adicionar_filme(movie):
        MovieController.filmes.append(movie)

    @staticmethod
    def get_movie_by_id(id):
        for filme in MovieController.filmes:
            if filme.id == id:
                return filme
        return None
