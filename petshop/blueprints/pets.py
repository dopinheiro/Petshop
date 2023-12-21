from datetime import datetime

from petshop.ext.database import db
from flask import Blueprint, render_template,request, flash, redirect, url_for
from petshop.models.pet import Pet
from flask_login import login_required, current_user


pets = Blueprint('pets', __name__,
                  template_folder='templates',
                  static_folder='static',
                  url_prefix='')


@pets.route('/edit-pet/<int:id>', methods=['GET', 'POST'])
@pets.route('/add-pet', methods=['GET', 'POST'])
@login_required
def add_pet(id=None):
    pet = None
    if id:
        pet=Pet.query.filter_by(id=id).one_or_none()
    if request.method == 'POST':
        name = request.form['name']
        specie = request.form['specie']
        proprietary = current_user.id
        birth = request.form['birth']
        formated_birth = datetime.strptime(birth, '%Y-%m-%d')
        note = request.form['note'] if 'note' in request.form else None
        
        is_register = len(Pet.query.filter_by(name=name).all())
        if pet:
            pet.name=name
            pet.species_id = specie
            print(specie)
            pet.birth = formated_birth
            db.session.add(pet)
            db.session.commit()
            flash('Pet editado com sucesso.')
        elif not is_register:
            new_pet = Pet(name, specie, proprietary, formated_birth, note)
            db.session.add(new_pet)
            db.session.commit()
            flash('Pet adicionado com sucesso.')
        else:
            return 'Erro'
        return redirect(url_for('pets.get_pet'))
    return render_template('addpet.html', pet=pet)



@pets.route('/pets', methods=['GET', 'POST'])
@login_required
def get_pet():
    pets = Pet.query.filter_by(proprietary_id=current_user.id).all()
    return render_template('pets.html', pets=pets)


@pets.route('/del-pet/<int:id>', methods=['GET'])
@login_required
def remove_pet(id):
    pet = Pet.query.filter_by(id=id).all()
    if pet and pet[0].proprietary_id == current_user.id:
        db.session.delete(pet[0])
        db.session.commit()
        flash('Pet removido com sucesso.')
    elif not pet:
        flash('Pet não cadastrado.', 'error')
    else:
        flash('Você só pode excluir um pet seu.', 'error')
    return redirect(url_for('pets.get_pet'))
