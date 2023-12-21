from sqlalchemy.orm import backref
from petshop.app import db

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species = db.relationship('Specie', foreign_keys=species_id)
    proprietary_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    proprietary = db.relationship('User', foreign_keys=proprietary_id)
    birth = db.Column(db.Date)
    note = db.Column(db.Text)
    
    def __init__(self, name, species, proprietary, birth, note):
        self.name = name
        self.species_id = species
        self.proprietary_id = proprietary
        self.birth = birth
        self.note = note
