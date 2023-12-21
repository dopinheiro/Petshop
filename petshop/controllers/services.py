from datetime import datetime

from petshop.app import app,db
from flask import render_template,request, flash, redirect, url_for
from petshop.models.service import Service
from flask_login import login_required, current_user

@app.route('/services', methods=['GET', 'POST'])
def get_services():
    services = Service.query.all()
    return render_template('servicos.html', services=services)


@app.route('/add-service', methods=['GET', 'POST'])
@login_required
def add_services():
    if current_user.role_id == 1:
        if request.method == 'POST':
            name = request.form['name']
            duration = request.form['duration']
            price = request.form['price']
            icon = request.form['icon']
            
            new_service = Service(name, duration, price, icon)
            db.session.add(new_service)
            db.session.commit()
            flash('Serviço adicionado com sucesso, você será redirecionado', 'success')
            return redirect(url_for('get_services'))
        return render_template('add-service.html')
    else:
        flash('Acesso restrito', 'error')
        return redirect(url_for('get_services'))
