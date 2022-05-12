import os


def init_app(app):
    app.config['SECRET_KEY'] = os.urandom(12).hex()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
