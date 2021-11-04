import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)


from app.controllers import default, \
                            users, \
                            pets, \
                            services, \
                            appointments

from app.models import service
from app.models import user
from app.models import role
from app.models import appointment
from app.models import appointment_service
from app.models import pet
from app.models import specie


@login_manager.user_loader
def load_user(user_id):
    return user.User.query.get(int(user_id))


@app.cli.command('setup')
def setup():
    db.session.add( role.Role('admin') )
    db.session.add( role.Role('client') )

    db.session.add ( specie.Specie('cachorro') )
    db.session.add ( specie.Specie('gato') )
    print('A seguir, insira os dados do usuário admin')
    name = input('Nome: ')
    email = input('Email: ')
    password = input('Senha: ')
    phone = input('Telefone: ')

    admin = user.User(name, email, password, phone, 1)
    db.session.add(admin)

    db.session.commit()