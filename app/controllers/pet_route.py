from datetime import datetime

from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.user import User
from app.models.pet import Pet
from app.models.specie import Specie
from app.models.service import Service
from app.models.appointment import Appointment
from app.models.appointment_service import AppointmentSevice
from flask_login import login_required, current_user

@app.route('/add-pet', methods=['GET', 'POST'])
@login_required
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        specie = request.form['specie']
        proprietary = request.form['proprietary']
        birth = request.form['birth']
        note = request.form['note']
        
        is_register = len(Pet.query.filter_by(name=name).all())
        if not is_register:
            new_pet = Pet(name, specie, proprietary, birth, note)
            db.session.add(new_pet)
            db.session.commit()
            return 'Pet adicionado com sucesso'
        else:
            return 'Erro'
    return render_template('addpet.html')



@app.route('/get-pet', methods=['GET', 'POST'])
@login_required
def get_pet():
    pet_id = request.args.get('id')
    pet = Pet.query.filter_by(id=pet_id).first()
    if pet:
        return f'O/A {pet.specie.description} chamado/a {pet.name} pertence à {pet.proprietary.name}'
    else:
        return 'Nenhum dado encontrado'


@app.route('/remove-pet', methods=['GET', 'DELETE'])
@login_required
def remove_pet():
    if request.method == 'DELETE':
        pet_id = request.form['pet_id']
        proprietary = request.form['proprietary_id']
        pet = Pet.query.filter_by(id=pet_id).all()
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
