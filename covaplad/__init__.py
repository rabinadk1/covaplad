from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
"""
NOTE: instance_relative_config if set to true,
opens config relative to instance folder
"""
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
migrate = Migrate(app,db)
from . import models
from . import routes