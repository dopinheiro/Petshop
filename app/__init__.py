from datetime import datetime
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
                            appointments, \
                            api


# Este trecho inicia as models
# ( importação realizada neste ponto pois precisa da instância de "app" instanciada )
from app.models import role
from app.models import user
from app.models import service
from app.models import specie
from app.models import pet
from app.models import status
from app.models import appointment
from app.models import appointment_service


@login_manager.user_loader
def load_user(user_id):
    return user.User.query.get(int(user_id))

@app.cli.command('setup')
def setup():
    """
    Para configurar o sistema, rodar: flask db setup
    """
    print('A seguir, insira os dados do usuário admin')
    name = input('Nome: ')
    email = input('Email: ')
    password = input('Senha: ')
    phone = input('Telefone: ')

    if len(user.User.query.all())==0 and len(service.Service.query.all())==0:
        queries = [
            role.Role('admin'),
            role.Role('client'),
            user.User(name, email, password, phone, 1),
            user.User('Test User', 'test_user@gmail.com', '123456', '11987654321', 2),
            specie.Specie('Cachorro'),
            specie.Specie('Gato'),
            status.Status('Agendado'),
            status.Status('Finalizado'),
            status.Status('Cancelado'), 
            pet.Pet('Maya', 1, 2, datetime.now() ,None),
            pet.Pet('Steve', 2, 2, datetime.now() ,None),
            service.Service('Banho', 30, 60, 'banho'),
            service.Service('Tosa', 30, 60, 'tosa'),
            service.Service('Corte de unhas', 30, 60, 'corte'),
            service.Service('Hidratação', 30, 60, 'hidratacao'),
            service.Service('Penteado', 30, 60, 'penteados'),
            service.Service('Escovação dos dentes ', 30, 60, 'escovacao'),
        ]
        for query in queries:
            db.session.add(query)
        db.session.commit()
