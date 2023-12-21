from datetime import datetime

from petshop.ext.database import db
from petshop.models import Pet,\
    Role,\
    Service,\
    Specie, \
    Status,\
    User


def createdb():
    db.create_all()


def populate():
    data = [
        Role('admin'),
        Role('client'),
        User(
            'admin',
            'admin@petshop.com',
            '123456',
            '11987654321',
            1
        ),
        User(
            'Test User',
             'test_user@petshop.com',
             '123456',
             '11987654321',
             2),
        Specie('Cachorro'),
        Specie('Gato'),
        Status('Agendado'),
        Status('Finalizado'),
        Status('Cancelado'),
        Pet('Maya', 1, 2, datetime.now(), None),
        Pet('Steve', 2, 2, datetime.now(), None),
        Service('Banho', 30, 60, 'banho'),
        Service('Tosa', 30, 60, 'tosa'),
        Service('Corte de unhas', 30, 60, 'corte'),
        Service('Hidratação', 30, 60, 'hidratacao'),
        Service('Penteado', 30, 60, 'penteados'),
        Service('Escovação dos dentes ', 30, 60, 'escovacao'),
    ]

    db.session.bulk_save_objects(data)
    db.session.commit()

    return Service.query.all()


def init_app(app):
    for command in [createdb, populate]:
        app.cli.add_command(app.cli.command()(command))
