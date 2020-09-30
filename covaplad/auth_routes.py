from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from is_safe_url import is_safe_url

from . import app, db, login_manager
from .forms import LoginForm, UserRegistrationForm
from .models import User


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            address=form.address.data,
            # phone_number=form.phone_number.data,
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user is not None and user.password == form.password.data:
            login_user(user, form.remember_me.data)
            next_page = request.args.get("next")
            # !Redirect only if the url is safe
            # TODO: Change allowed_hosts and require_https later on
            return redirect(
                next_page
                if is_safe_url(next_page, ("localhost:5000", "127.0.0.1:5000"))
                else url_for("index")
            )
        else:
            flash("Invalid credentials. Please check again and enter.", "danger")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
