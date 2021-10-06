from app import app,db
from flask import request
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']  # TODO: usar hash para senha, usar werkzeug
        phone = request.form['phone']
        address = request.form['address']
        
        is_register = len(Clients.query.filter_by(email=email).all())
        if not is_register:
            new_user = Clients(name, email, password, phone, address)
            db.session.add(new_user)
            db.session.commit()
            return 'Usuário adicionado com sucesso'
        else:
            return 'Email de usuário já cadastrado'
    return 'Tela novo usuário'