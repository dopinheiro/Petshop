from datetime import datetime

from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.clients import Clients
from app.models.pets import Pets
from app.models.species import Species
from app.models.services import Services
from app.models.appointments import Appointments
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/config')
def config():
    if len(Clients.query.all())==0 and len(Services.query.all())==0:
        queries = [
            Clients(
                'Diego de Oliveira',
                'diego.olliveirap@gmail.com',
                generate_password_hash('123456'),
                '11961858580',
                None
            ),
            Species('Cachorro'),
            Species('Gato'),
            Pets('Maya', 1, 1, None),
            Services('Banho', 30, 60, 'banho'),
            Services('Tosa', 30, 60, 'tosa'),
            Services('Corte de unhas', 30, 60, 'corte'),
            Services('Hidratação', 30, 60, 'hidratacao'),
            Services('Penteado', 30, 60, 'penteados'),
            Services('Escovação dos dentes ', 30, 60, 'escovacao'),
        ]
        for query in queries:
            db.session.add(query)
        db.session.commit()
        return 'configurado'
    else:
        return 'Não necessita configuração'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']  # TODO: usar hash para senha, usar werkzeug
        phone = request.form['phone']
        address = request.form['address'] if 'address' in request.form else None
        is_register = len(Clients.query.filter_by(email=email).all())
        if not is_register:
            hashed_password = generate_password_hash(password)
            new_user = Clients(name, email, hashed_password, phone, address)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuário cadastrado com sucesso, você será redirecionado', 'success')
            return redirect(url_for('login'))
        else:
            flash('Email de usuário já cadastrado', 'error')
    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Clients.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('add_appointment'))
    return render_template('login.html')


@app.route('/get-pet', methods=['GET', 'POST'])
def get_pet():
    pet_id = request.args.get('id')
    pet = Pets.query.filter_by(id=pet_id).first()
    if pet:
        return f'O/A {pet.species.description} chamado/a {pet.name} pertence à {pet.proprietary.name}'
    else:
        return 'Nenhum dado encontrado'

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
    return render_template('addpet.html')

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

@app.route('/services', methods=['GET', 'POST'])
def add_services():
    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']
        price = request.form['price']
        icon = request.form['icon']
        
        new_service = Services(name, duration, price, icon)
        db.session.add(new_service)
        db.session.commit()
        return 'Serviço adicionado com sucesso'
    services = Services.query.all()
    
    print(services[0].icon)
    return render_template('servicos.html', services=services)

@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def add_appointment():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%d/%m/%Y %H:%M').date()
        pet = request.form['pet']
        service = request.form['service']
        
        new_appointment = Appointments(date, pet, service)
        db.session.add(new_appointment)
        db.session.commit()
        return 'Serviço adicionado com sucesso'
    services = Services.query.all()
    return render_template('addagendamento.html', services=services)

