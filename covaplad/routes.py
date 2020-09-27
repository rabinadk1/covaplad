from . import app,db
from flask import Flask, render_template,request,redirect,url_for
from covaplad.forms import UserRegistrationForm
from . import models

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register",methods=["GET","POST"])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = models.User(name=form.name.data,username=form.username.data,email=form.email.data,password=form.password.data,address=form.address.data,phone_number=form.phone_number.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("register.html", form=form)
