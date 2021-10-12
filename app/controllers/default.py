from datetime import datetime

from app import app,db
from flask import render_template,request
from app.models.clients import Clients
from app.models.pets import Pets
from app.models.services import Services
from app.models.appointments import Appointments

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

@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        proprietary = request.form['proprietary']
        obs = request.form['obs']
        
        is_register = len(Pets.query.filter_by(name=name).all())
        if not is_register:
            new_pet = Pets(name, breed, proprietary, obs)
            db.session.add(new_pet)
            db.session.commit()
            return 'Pet adicionado com sucesso'
        else:
            return 'Erro'
    return 'Tela novo pet'

@app.route('/remove-pet', methods=['GET', 'DELETE'])
def remove_pet():
    if request.method == 'DELETE':
        pet_id = request.form['pet_id']
        proprietary = request.form['proprietary_id']
        pet = Pets.query.filter_by(id=pet_id).all()
        print(pet)
        if pet and pet[0].proprietary == int(proprietary):
            db.session.delete(pet[0])
            db.session.commit()
            return 'Pet removido com sucesso'
        elif not pet:
            return 'Erro, não cadastrado'
        else:
            return 'Erro, este pet não é seu'
    return 'Tela remover pet'

@app.route('/add-services', methods=['GET', 'POST'])
def add_services():
    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']
        price = request.form['price']
        
        new_service = Services(name, duration, price)
        db.session.add(new_service)
        db.session.commit()
        return 'Serviço adicionado com sucesso'
    return 'Tela Adicionar serviços'

@app.route('/appointments', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%d/%m/%Y %H:%M').date()
        pet = request.form['pet']
        service = request.form['service']
        
        new_appointment = Appointments(date, pet, service)
        db.session.add(new_appointment)
        db.session.commit()
        return 'Serviço adicionado com sucesso'
