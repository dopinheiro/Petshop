from app import db

class Pets(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)
    proprietary = db.Column(db.Integer, db.ForeignKey('clients.id'), unique=True)
    obs = db.Column(db.Text)
    
    def __init__(self, name, breed, proprietary, obs):
        self.name = name
        self.breed = breed
        self.proprietary = proprietary
        self.obs = obs

        