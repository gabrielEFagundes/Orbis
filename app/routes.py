from app import app, db
from flask import render_template, url_for, redirect
from app.forms import UserLogin, UserSignin
from app.models import User, TripPackage, Reserve
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if(current_user.is_authenticated):
        return render_template('index.html', user=current_user)
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLogin()

    if(form.validate_on_submit()):
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('home'))
        
        return render_template('login.html', form=form, error="Invalid email or password!")
    
    return render_template('login.html', form=form, error="Error validating form!")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserSignin()

    if(form.validate_on_submit()):
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('home'))
    
    return render_template('signin.html', form=form, error="Error validating form!")