from app import app,db
from flask import render_template
from app.models.clients import Clients

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth')
def authentication():
    return 'Authentication'

@app.route('/teste')
def teste():
    usuario = Clients('Usuario', 'novo.usuario@gmail.com', '12345678', '11987654321', 'Rua desconhecida')
    db.session.add(usuario)
    db.session.commit()
    return 'usuário adicionado'