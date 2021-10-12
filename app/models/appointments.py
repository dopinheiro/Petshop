from app import db

class Appointments(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    pet = db.Column(db.Integer, db.ForeignKey('pets.id'))
    service = db.Column(db.Integer, db.ForeignKey('services.id'))
    finished_at = db.Column(db.Date)
    obs = db.Column(db.String)
    
    def __init__(self, date, pet, service, finished_at=None, obs=None):
        self.date = date
        self.pet = pet
        self.service = service
        self.finished_at = finished_at
        self.obs = obs

        