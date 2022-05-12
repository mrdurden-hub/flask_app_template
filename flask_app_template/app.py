from flask import Flask
from flask_app_template.ext.db import database
from flask_app_template.ext.settings import settings
from flask_app_template.ext.bootstrap import bootstrap
from flask_app_template.blueprints.general import general
from flask_app_template.blueprints.auth import auth
from flask_app_template.ext.commands import commands

app = Flask(__name__)

settings.init_app(app)
db = database.init_app(app)
bootstrap.app_init(app)
commands.init_app(app, db)
app.register_blueprint(general.home_bp)
app.register_blueprint(auth.auth_bp)
