from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.user import User
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']  # TODO: usar hash para senha, usar werkzeug
        phone = request.form['phone']
        role = request.form['role']
        is_register = len(User.query.filter_by(email=email).all())

        if not is_register:
            new_user = User(name, email, password, phone, role)
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
            return redirect(url_for('add_appointment'))
    return render_template('login.html')


