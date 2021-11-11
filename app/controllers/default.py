from datetime import datetime

from app import app,db
from flask import render_template,request, flash, redirect, url_for
from app.models.user import User
from app.models.pet import Pet
from app.models.specie import Specie
from app.models.service import Service
from app.models.role import Role
from flask_login import  current_user
from werkzeug.security import generate_password_hash

@app.route('/')
def index():
    return render_template('home.html')
