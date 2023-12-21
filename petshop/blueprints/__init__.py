from .appointments import appointments
from .auth import auth
from .default import webui
from .pets import pets
from .services import services


def init_app(app):
    app.register_blueprint(appointments)
    app.register_blueprint(auth)
    app.register_blueprint(webui)
    app.register_blueprint(pets)
    app.register_blueprint(services)
