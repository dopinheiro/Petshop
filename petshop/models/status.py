from petshop.app import db

class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    
    def __init__(self, description):
        self.description = description