from app import db

class Clients(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    
    def __init__(self, name, email, password, phone, address):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address

        