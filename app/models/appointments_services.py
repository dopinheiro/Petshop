from app import db

class Appointments_Services(db.Model):
    __tablename__ = 'appointments_services'

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    service = db.Column(db.Integer, db.ForeignKey('services.id'))
    
    def __init__(self, appointments, service):
        self.appointment_id = appointments
        self.service = service
        