from petshop.ext.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    phone = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', foreign_keys=role_id)
    pets = db.relationship('Pet', backref='pets')

    def __init__(self, name, email, password, phone, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone
        self.role_id = role

        db.session.add(self)
        db.session.commit()
