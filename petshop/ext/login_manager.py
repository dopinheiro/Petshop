from flask_login import LoginManager
from petshop.models import user


login_manager = LoginManager()


def init_app(app):
    login_manager.init_app(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    return user.User.query.get(int(user_id))
