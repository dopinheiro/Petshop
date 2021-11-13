from datetime import datetime
from ast import literal_eval

from app import app,db
from flask import request, jsonify
from app.models.pet import Pet
from app.models.service import Service
from app.models.appointment import Appointment
from app.models.appointment_service import AppointmentSevice
from flask_login import login_required, current_user


@app.route('/api/add-appointment', methods=['POST'])
def api_add_appointment():
    full_date = f"{request.form['date'].replace('00:00:00.000', '')} {request.form['time'].replace('TimeOfDay(', '').replace(')','')}"
    print(full_date)
    date = datetime.strptime(full_date, '%Y-%m-%d %H:%M')
    print(date)
    pet_id = request.form['pet']
    note = request.form['note']
    
    new_appointment = Appointment(date, pet_id, note=note)
    db.session.add(new_appointment)
    db.session.flush()

    for service in literal_eval(request.form['service']):
        service = service
        new_appointment_service = AppointmentSevice(new_appointment.id, service)
        db.session.add(new_appointment_service)
            
    db.session.commit()
    return jsonify(msg='Agendamento realizado com sucesso'), 200

@app.route('/api/get-appointments/', methods=['GET'])
@app.route('/api/get-appointments/<int:id>', methods=['GET'])
def api_get_appointments(id=None):
    if id==None:
        appointments = Appointment.query.all()
        print(appointments)
        all_appointments = {}
        if appointments:
            for appointment in appointments:
                all_appointments[appointment.id] = {
                    'date': appointment.date,
                    'pet': {
                        'id': appointment.pet.id,
                        'name': appointment.pet.name,
                        'specie': appointment.pet.species.description,
                        'proprietary': appointment.pet.proprietary.name
                    },
                    'note': appointment.note,
                    'finished_at': appointment.finished_at,
                    'status': appointment.status.description
                }
            return jsonify(all_appointments), 200
    elif id!=None:
        appointment = Appointment.query.filter_by(id=id).first()
        if appointment:
            services = [ service.name for service in appointment.services]
            services_json = {
                'id': appointment.id,
                'date': appointment.date,
                'pet': {
                    'id': appointment.pet.id,
                    'name': appointment.pet.name,
                    'specie': appointment.pet.species.description,
                    'proprietary': appointment.pet.proprietary.name
                },
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