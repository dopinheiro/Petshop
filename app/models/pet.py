from app import db

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    specie = db.relationship('Specie', foreign_keys=species_id)
    proprietary_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    proprietary = db.relationship('Client', foreign_keys=proprietary_id)
    obs = db.Column(db.Text)
    
    def __init__(self, name, species, proprietary, obs):
        self.name = name
        self.species_id = species
        self.proprietary_id = proprietary
        self.obs = obs
