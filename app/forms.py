from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange
from app import bcrypt, db
from app.models import User, TripPackage, Reserve

class UserLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def save(self):
        password = bcrypt.generate_password_hash(self.password.data).encode('utf-8')
        
        user = User(
            email = self.email.data,
            password = password.decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()

        return user
    
class UserSignin(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    type = SelectField('Type', choices=[('customer', 'Customer'), ('worker', 'Worker')], validators=[DataRequired()])
    submit = SubmitField('Sign In!')

    def save(self):
        password = bcrypt.generate_password_hash(self.password.data).encode('utf-8')

        user = User(
            name = self.name.data,
            email = self.email.data,
            password = password.decode('utf-8'),
            type = self.type.data
        )

        db.session.add(user)
        db.session.commit()

        return user