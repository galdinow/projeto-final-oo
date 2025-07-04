from models.base_model import BaseModel

class Movie(BaseModel):
    def __init__(self, id, title, description,director,img_url):
        self.id = id
        self.title = title
        self.description = description
        self.director = director
        self.img_url = img_url
    

    
    def to_dict(movie):
        return {"id":movie.id, "title":movie.title, "description": movie.description, "director":movie.director, "img_url":movie.img_url}
