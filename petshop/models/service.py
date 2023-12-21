from petshop.app import db

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    duration = db.Column(db.Integer)
    price = db.Column(db.Float)
    icon = db.Column(db.String)
    
    def __init__(self, name, duration, price, icon):
        self.name = name
        self.duration = duration
        self.price = price
        self.icon = icon
        