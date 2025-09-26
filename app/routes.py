from app import app, db
from flask import render_template, url_for, redirect
from app.forms import UserLogin, UserSignin, TripPackageForm
from app.models import User, TripPackage, Reserve
from flask_login import login_user, logout_user, login_required, current_user

print("Routes Working")

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('index.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLogin()

    try:
        if(form.validate_on_submit()):
            user = form.save()
            login_user(user, remember=True)
            return redirect(url_for('home'))
    
    except Exception:
        raise Exception("Error Logging You In!")
    
    return render_template('login.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserSignin()

    if(form.validate_on_submit()):
        try:
            user = form.save()
            login_user(user, remember=True)
            return redirect(url_for('home'))
            
        except Exception:
            raise Exception("Error Signin You In!")
    
    return render_template('signin.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/new/package', methods=['GET', 'POST'])
@login_required
def newPackage():
    form = TripPackageForm()

    if(form.validate_on_submit()):
        try:
            form.save()
            return redirect(url_for('home'))
        
        except Exception:
            raise Exception("There was an error signin your package!")
        
    else:
        print(form.errors)

    return render_template('new_package.html', form=form)