from flask import Flask, render_template
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
    return render_template("index.html")
