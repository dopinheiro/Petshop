from datetime import datetime

from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.user import User
from app.models.pet import Pet
from app.models.specie import Specie
from app.models.service import Service
from app.models.appointment import Appointment
from app.models.appointment_service import AppointmentSevice
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def add_appointment():
    if request.method == 'POST':
        full_date = f"{request.form['date']} {request.form['horario']}"
        date = datetime.strptime(full_date, '%Y-%m-%d %H:%M')
        pet_id = request.form['pet']  # TODO: Precisa inserir no formulário
        services = []
        note = request.form['note']
        
        new_appointment = Appointment(date, pet_id, obs=note)
        db.session.add(new_appointment)
        db.session.flush()

        for key in request.form.keys():
            if key.startswith('service'):
                service = int(request.form[key])
                new_appointment_service = AppointmentSevice(new_appointment.id, service)
                db.session.add(new_appointment_service)
                
        db.session.commit()
        return 'Serviço adicionado com sucesso'
    services = Service.query.all()
    print()
    pets = Pet.query.filter_by(proprietary_id=current_user.role_id).all()
    return render_template('addagendamento.html', services=services, pets=pets)


@app.route('/get-appointments', methods=['GET', 'POST'])
@login_required
def get_appointments():
    appointment_id = request.args.get('id')
    appointment = Appointment.query.filter_by(id=appointment_id).first()
    if appointment:
        services = [ service.name for service in appointment.services]
        return f'''O agendamento possui os seguintes serviços: {str(services).replace("[", "").replace("]", "").replace("'", "")}'''
    else:
        return 'Nenhum dado encontrado'
