from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import CSRFProtect

#csrf = CSRFProtect()

def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)    
 #   csrf.init_app(app) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////stadistic.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)

    from .public import public
    app.register_blueprint(public)

    from .api import api
    app.register_blueprint(api)

    register_error_handlers(app)
    return app

