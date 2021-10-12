from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)



from app.controllers import default
from app.models import services
from app.models import clients
from app.models import appointments
from app.models import appointments_services
from app.models import pets