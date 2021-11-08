from app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    pet = db.relationship('Pet', foreign_keys=pet_id)
    finished_at = db.Column(db.Date)
    note = db.Column(db.Text)
    services = db.relationship('Service', secondary='appointments_services', backref='appointments')
    
    def __init__(self, date, pet, finished_at=None, note=None):
        self.date = date
        self.pet_id = pet
        self.finished_at = finished_at
        self.note = note
