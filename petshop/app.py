from flask import Flask
from petshop.ext import commands, login_manager, database
from petshop import blueprints, api


def create_app(app):
    app = Flask(__name__)
    app.config.from_object('config')
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    database.init_app(app)
    login_manager.init_app(app)

    commands.init_app(app)
    blueprints.init_app(app)
    api.init_app(app)
    return app


#
# @login_manager.py.user_loader
# def load_user(user_id):
#     return user.User.query.get(int(user_id))
#
