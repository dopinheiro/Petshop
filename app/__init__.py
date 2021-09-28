from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)



from app.controllers import default
from app.models import services
from app.models import clients
from app.models import appointments
from app.models import pets