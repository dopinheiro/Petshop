from datetime import datetime
from ast import literal_eval

from petshop.app import app,db
from flask import request, jsonify
from petshop.models.pet import Pet
from petshop.models.service import Service
from petshop.models.appointment import Appointment
from petshop.models.appointment_service import AppointmentSevice
from flask_login import login_required, current_user


@app.route('/api/add-appointment', methods=['POST'])
@app.route('/api/edit-appointment/<int:id>', methods=['PUT'])
def api_add_appointment(id=None):

    full_date = request.form['date']
    date = datetime.strptime(full_date, '%Y-%m-%d %H:%M')
    pet_id = request.form['pet']
    note = request.form['note']
    
    if request.method == 'PUT':
        appointment = Appointment.query.filter_by(id=id).one_or_none()
        appointment.date = date
        appointment.pet_id = pet_id
        appointment.note = note

        appointments_services = AppointmentSevice.query.filter_by(appointment_id=id).all()
        for appointment_service in appointments_services:
            db.session.delete(appointment_service)
    else:
        appointment = Appointment(date, pet_id, note=note)
    db.session.add(appointment)
    db.session.flush()



    for service in literal_eval(request.form['service']):
        appointment_service = AppointmentSevice(appointment.id, service)
        db.session.add(appointment_service)
            
    db.session.commit()
    return jsonify(msg='Agendamento realizado com sucesso'), 200

@app.route('/api/get-appointments/', methods=['GET'])
@app.route('/api/get-appointments/<int:id>', methods=['GET'])
def api_get_appointments(id=None):
    if id==None:
        appointments = Appointment.query.all()
        all_appointments = []
        if appointments:
            for appointment in appointments:
                all_appointments.append({
                    'id': appointment.id,
                    'date': str(appointment.date),
                    'pet': {
                        'id': appointment.pet.id,
                        'name': appointment.pet.name,
                        'specie': appointment.pet.species.description,
                        'proprietary': appointment.pet.proprietary.name
                    },
                    'note': appointment.note,
                    'finished_at': appointment.finished_at,
                    'status': appointment.status.description
                })
            return jsonify({'appointments': all_appointments}), 200
    elif id!=None:
        appointment = Appointment.query.filter_by(id=id).first()
        if appointment:
            services = [ {'id': service.id, 'name':service.name} for service in appointment.services]
            services_json = {
                'id': appointment.id,
                'date': str(appointment.date),
                'pet': {
                    'id': appointment.pet.id,
                    'name': appointment.pet.name,
                    'specie': appointment.pet.species.description,
                    'proprietary': appointment.pet.proprietary.name
                },
                'services': services,
                'note': appointment.note,
                'finished_at': appointment.finished_at,
                'status': appointment.status.description
            }
            return jsonify(services_json), 200
    
    return 'Nenhum dado encontrado'


@app.route('/api/end-appointment/<int:id>', methods=['PUT'])
def api_end_appointments(id):
    appointment = Appointment.query.filter_by(id=id).one_or_none()

    if appointment:
        appointment.finished_at=datetime.utcnow()
        appointment.status_id=2
        db.session.add(appointment)
        db.session.commit()
        return jsonify(msg='Agendamento encerrado'), 200
    else:
        return jsonify(msg='Nenhum agendamento encontrado'), 200


@app.route('/api/cancel-appointment/<int:id>', methods=['PUT'])
def cancel_end_appointments(id):
    appointment = Appointment.query.filter_by(id=id).one_or_none()

    if appointment:
        appointment.finished_at=None
        appointment.status_id=3
        db.session.add(appointment)
        db.session.commit()
        return jsonify(msg='Agendamento cancelado'), 200
    else:
        return jsonify(msg='Nenhum agendamento encontrado'), 200


@app.route('/api/del-appointment/<int:id>', methods=['DELETE'])
def del_end_appointments(id):
    appointment = Appointment.query.filter_by(id=id).one_or_none()

    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return jsonify(msg='Agendamento excluído'), 200
    else:
        return jsonify(msg='Nenhum agendamento encontrado'), 200