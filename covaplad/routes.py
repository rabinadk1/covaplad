from flask import redirect, render_template, url_for
from flask_login import login_required

from . import app, db
from .forms import DonationVenueRegistrationForm, EventResistrationForm
from .models import DonationVenue, Event


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register_event", methods=["GET", "POST"])
@login_required
def register_event():
    form = EventResistrationForm()
    if form.validate_on_submit():
        event = Event(
            name=form.name.data,
            start=form.start.data,
            end=form.end.data,
            address=form.address.data,
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("register_event"))
    return render_template("register_event.html", form=form)


@app.route("/register_venue", methods=["GET", "POST"])
@login_required
def register_venue():
    form = DonationVenueRegistrationForm()
    if form.validate_on_submit():
        venue = DonationVenue(
            name=form.name.data,
            email=form.email.data,
            address=form.address.data,
            phone_number=form.phone_number.data,
        )
        db.session.add(venue)
        db.session.commit()
        return redirect(url_for("register_venue"))
    return render_template("register_venue.html", form=form)
