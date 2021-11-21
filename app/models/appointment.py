from app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    pet = db.relationship('Pet', foreign_keys=pet_id)
    finished_at = db.Column(db.DateTime)
    note = db.Column(db.Text)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    status = db.relationship('Status', foreign_keys=status_id)

    services = db.relationship('Service', secondary='appointments_services', backref='appointments')
    
    def __init__(self, date, pet, note=None):
        self.date = date
        self.pet_id = pet
        self.note = note
        self.finished_at = None
        self.status_id = 1
