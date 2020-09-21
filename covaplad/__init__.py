from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
NOTE: instance_relative_config if set to true,
opens config relative to instance folder
"""
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hello There!"
