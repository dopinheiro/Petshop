from petshop.app import db

class AppointmentSevice(db.Model):
    __tablename__ = 'appointments_services'

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    appointment = db.relationship('Appointment', foreign_keys=appointment_id)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    Service = db.relationship('Service', foreign_keys=service_id)

    def __init__(self, appointment_id, service_id):
        self.appointment_id = appointment_id
        self.service_id = service_id