from models.movie import Movie

class MovieController:

    @staticmethod
    def to_dict(movie):
        return {"id":movie.id, "title":movie.title, "description": movie.description, "director":movie.director, "img_url":movie.img_url}
