from flask import Blueprint, render_template


webui = Blueprint('webui', __name__,
                  template_folder='templates',
                  static_folder='static',
                  url_prefix='')


@webui.route('/')
def index():
    return render_template('home.html')


@webui.route('/contato')
def contact():
    return render_template('contato.html')
