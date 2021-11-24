from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        is_register = len(User.query.filter_by(email=email).all())

        if not is_register:
            new_user = User(name, email, password, phone, role=2)
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
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash('Você está logado', 'success')
            if current_user.id == 1:
                return redirect(url_for('get_appointments'))
            else:
                return redirect(url_for('add_appointment'))
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


