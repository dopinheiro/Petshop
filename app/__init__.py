from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)


from app.controllers import default, \
                            user_route, \
                            pet_route, \
                            service_route, \
                            appointment_route

from app.models import service
from app.models import user
from app.models import role
from app.models import appointment
from app.models import appointment_service
from app.models import pet
from app.models import specie


@login_manager.user_loader
def load_user(user_id):
    return user.User.query.get(int(user_id))
