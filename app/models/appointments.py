from app import db

class Appointments(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    pet = db.relationship('Pets', foreign_keys=pet_id)
    finished_at = db.Column(db.Date)
    obs = db.Column(db.String)
    services = db.relationship('Services', secondary='appointments_services', backref='appointments')
    
    def __init__(self, date, pet, finished_at=None, obs=None):
        self.date = date
        self.pet_id = pet
        self.finished_at = finished_at
        self.obs = obs
