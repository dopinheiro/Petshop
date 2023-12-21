from datetime import datetime

from petshop.app import app, db
from flask import render_template,request, flash, redirect, url_for
from petshop.models.user import User
from petshop.models.pet import Pet
from petshop.models.specie import Specie
from petshop.models.service import Service
from petshop.models.role import Role
from flask_login import  current_user
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contato')
def contact():
    return render_template('contato.html')
