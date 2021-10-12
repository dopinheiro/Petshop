from app import db

class Services(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    duration = db.Column(db.Integer)
    price = db.Column(db.Float)
    
    def __init__(self, name, duration, price):
        self.name = name
        self.duration = duration
        self.price = price
        