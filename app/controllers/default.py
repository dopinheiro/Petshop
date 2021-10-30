from datetime import datetime

from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.user import User
from app.models.pet import Pet
from app.models.specie import Specie
from app.models.service import Service
from app.models.role import Role
from flask_login import  current_user
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/config')
def config():
    if len(User.query.all())==0 and len(Service.query.all())==0:
        queries = [
            # Role('admin'),
            # Role('client'),
            User(
                'Diego de Oliveira',
                'diego.olliveirap@gmail.com',
                generate_password_hash('123456'),
                '11961858580',
                1
            ),
            Specie('Cachorro'),
            Specie('Gato'),
            Pet('Maya', 1, 1, datetime.now() ,None),
            Service('Banho', 30, 60, 'banho'),
            Service('Tosa', 30, 60, 'tosa'),
            Service('Corte de unhas', 30, 60, 'corte'),
            Service('Hidratação', 30, 60, 'hidratacao'),
            Service('Penteado', 30, 60, 'penteados'),
            Service('Escovação dos dentes ', 30, 60, 'escovacao'),
        ]
        for query in queries:
            db.session.add(query)
        db.session.commit()
        return 'configurado'
    else:
        return 'Não necessita configuração'