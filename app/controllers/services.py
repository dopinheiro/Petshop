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


@app.route('/services', methods=['GET', 'POST'])
def add_services():
    if request.method == 'POST':
        name = request.form['name']
        duration = request.form['duration']
        price = request.form['price']
        icon = request.form['icon']
        
        new_service = Service(name, duration, price, icon)
        db.session.add(new_service)
        db.session.commit()
        return 'Serviço adicionado com sucesso'
    services = Service.query.all()
    return render_template('servicos.html', services=services)
