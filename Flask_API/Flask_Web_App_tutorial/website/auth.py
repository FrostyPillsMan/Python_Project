from flask import Blueprint, redirect, render_template, request, flash, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password): # type: ignore
                flash('Logged in Successfull!!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, try again.", category='error')
        else:
            flash("Email does not exist.", category='error')

    return render_template("login.html", user=current_user) 
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['Get', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4: # type: ignore
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2: # type: ignore
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match.", category="error")
        elif len(password1) < 7: # type: ignore
            flash("Passwords must be at least 7 characters.", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1)) # type: ignore
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category="success")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

