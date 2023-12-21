from datetime import datetime

from petshop.app import app,db
from flask import render_template,request, redirect, url_for
from petshop.models.pet import Pet
from petshop.models.service import Service
from petshop.models.appointment import Appointment
from petshop.models.appointment_service import AppointmentSevice
from flask_login import login_required, current_user
from flask import flash

@app.route('/add-appointments', methods=['GET', 'POST'])
@login_required
def add_appointment():
    if request.method == 'POST':
        full_date = f"{request.form['date']} {request.form['horario']}"
        date = datetime.strptime(full_date, '%Y-%m-%d %H:%M')
        pet_id = request.form['pet']
        services = []
        note = request.form['note']
        
        new_appointment = Appointment(date, pet_id, note=note)
        db.session.add(new_appointment)
        db.session.flush()

        for key in request.form.keys():
            if key.startswith('service'):
                service = int(request.form[key])
                new_appointment_service = AppointmentSevice(new_appointment.id, service)
                db.session.add(new_appointment_service)
                
        db.session.commit()
        flash('Agendamento realizado com sucesso', 'success')
        return redirect(url_for('get_appointments'))
    services = Service.query.all()
    pets = Pet.query.filter_by(proprietary_id=current_user.id).all()
    return render_template('addagendamento.html', services=services, pets=pets, appointment=None)


@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def get_appointments():
    if current_user.role_id==1:
        appointments = Appointment.query.order_by("date").all()
    else:
        appointments = Appointment.query.filter(Appointment.pet.has(proprietary_id=current_user.id)).all()
    return render_template('agendamentos.html', appointments=appointments)


@app.route('/edit-appointment/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_appointments(id):
    if request.method == 'POST':
        full_date = f"{request.form['date']} {request.form['horario']}"
        date = datetime.strptime(full_date, '%Y-%m-%d %H:%M')
        pet_id = request.form['pet']
        services = []
        note = request.form['note']
        
        appointment = Appointment.query.filter_by(id=id).one_or_none()
        appointment.date = date
        appointment.pet_id = pet_id
        appointment.note = note

        appointments_services = AppointmentSevice.query.filter_by(appointment_id=id).all()

        db.session.add(appointment)
        db.session.flush()

        for appointment_service in appointments_services:
            db.session.delete(appointment_service)

        for key in request.form.keys():
            if key.startswith('service'):
                service = int(request.form[key])
                new_appointment_service = AppointmentSevice(appointment.id, service)
                db.session.add(new_appointment_service)
                
        db.session.commit()
        flash('Agendamento realizado com sucesso', 'success')
        return redirect(url_for('get_appointments'))
    
    appointment = Appointment.query.filter_by(id=id).one_or_none()
    if appointment:
        if current_user.id==1:
            appointment.finished_at=datetime.utcnow()
            appointment.status_id=2
            db.session.add(appointment)
            db.session.commit()
            flash(f'Agendamento do/a {appointment.pet.name} foi finalizado', 'success')
            return redirect(url_for('get_appointments'))
        
        services = Service.query.all()
        services = Service.query.all()
        pets = Pet.query.filter_by(proprietary_id=current_user.id).all()
        return render_template('addagendamento.html', appointment=appointment, services=services, pets=pets)
    else:
        flash(f'Agendamento não encontrado...', 'warning')
        return redirect(url_for('get_appointments'))

@app.route('/del-appointment/<int:id>')
def del_appointments(id):
    appointment = Appointment.query.filter_by(id=id).one_or_none()

    if appointment:
        if current_user.id==1:
            appointment.finished_at=None
            appointment.status_id=3
            db.session.add(appointment)
            db.session.commit()
            flash('Agendamento cancelado', 'warning')
            return redirect(url_for('get_appointments'))
            
        db.session.delete(appointment)
        db.session.commit()

    flash('Agendamento excluído', 'warning')
    return redirect(url_for('get_appointments'))
