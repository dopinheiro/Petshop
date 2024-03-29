from petshop.ext.database import db

class Specie(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    
    def __init__(self, description):
        self.description = description