from app import db

class Appointments(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    client = db.Column(db.String, db.ForeignKey('clients.id'), unique=True)
    service = db.Column(db.String, db.ForeignKey('services.id'), unique=True)
    finished_at = db.Column(db.String)
    obs = db.Column(db.String)
    
    def __init__(self, date, client, service, finished_at, obs):
        self.date = date
        self.client = client
        self.service = service
        self.finished_at = finished_at
        self.obs = obs

        