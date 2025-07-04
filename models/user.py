from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(user):
        return {"id":user.user_id, "name": user.username, "email": user.email, "password": user.password}