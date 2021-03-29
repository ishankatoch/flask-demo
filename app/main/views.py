from . import main
from flask import render_template, session, redirect, url_for, flash
from .forms import NameForm


@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("You have changed your name", "warning")
        session["name"] = form.name.data
        print(session["name"])
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form, name=session.get("name"))


@main.route("/about")
def about():
    return render_template("about.html")
