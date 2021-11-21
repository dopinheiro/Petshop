from datetime import datetime

from app import app,db
from flask import render_template,request, redirect, url_for
from app.models.pet import Pet
from app.models.service import Service
from app.models.appointment import Appointment
from app.models.appointment_service import AppointmentSevice
from flask_login import login_required, current_user




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
        return 'Serviço adicionado com sucesso'
    services = Service.query.all()
    pets = Pet.query.filter_by(proprietary_id=current_user.role_id).all()
    print(pets)
    return render_template('addagendamento.html', services=services, pets=pets)


@app.route('/appointments', methods=['GET', 'POST'])
@login_required
def get_appointments():
    # appointment_id = request.args.get('id')
    appointments = Appointment.query.order_by("date").all()
    print(appointments)
    if appointments:
        return render_template('agendamentos.html', appointments=appointments)
    else:
        return 'Nenhum dado encontrado'

@app.route('/del-appointment/<int:id>')
def del_appointments(id):
    appointment = Appointment.query.filter_by(id=id).one_or_none()

    if appointment:
        db.session.delete(appointment)
        db.session.commit()

    return redirect(url_for('get_appointments'))